from pro_filer.actions.main_actions import show_details  # NOQA

import pytest
from datetime import datetime


@pytest.mark.parametrize("file_name, expect_out", [
    ("text.txt", "File 'text.txt' does not exist\n"),
    ("test1.py", (
        'File name: test1.py\n'
        'File size in bytes: 0\n'
        'File type: file\n'
        'File extension: .py\n'
        f"Last modified date: {datetime.today().strftime('%Y-%m-%d')}\n")),
    ("test2", (
        'File name: test2\n'
        'File size in bytes: 0\n'
        'File type: file\n'
        'File extension: [no extension]\n'
        f"Last modified date: {datetime.today().strftime('%Y-%m-%d')}\n"))
])
def test_show_details(file_name, expect_out, tmp_path, capsys):
    tmp_p = tmp_path / file_name

    if "test" in file_name:
        tmp_p.touch()

    cxt = {"base_path": tmp_p.__str__()}

    show_details(cxt)

    assert capsys.readouterr().out == expect_out