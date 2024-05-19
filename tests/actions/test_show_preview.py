from pro_filer.actions.main_actions import show_preview  # NOQA

import pytest

pytestmark = pytest.mark.dependency()

@pytest.fixture
def base_context():
    return {
        "all_dirs": [
            "/path/to",
            "/path",
            "/path-to",
        ],
        "all_files": [
            "/path/to/file.sql",
            "/path/to/file.txt",
            "/path/to/file2.txt",
            "/path/to/FILE.txt",
            "/path/to/FILE2.TXT",
            "/path/to/something.txt",
            "/path-to/file.txt",
        ],
    }

def test_show_preview_default_with_files(base_context, capsys):
    show_preview(base_context)
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out.strip() == """Found 7 files and 3 directories
First 5 files: ['/path/to/file.sql', '/path/to/file.txt', '/path/to/file2.txt', '/path/to/FILE.txt', '/path/to/FILE2.TXT']
First 5 directories: ['/path/to', '/path', '/path-to']"""

def test_show_preview_empty_arrays(base_context, capsys):
    base_context["all_files"] = []
    base_context["all_dirs"] = []
    show_preview(base_context)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Found 0 files and 0 directories"