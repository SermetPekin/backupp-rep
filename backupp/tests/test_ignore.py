

from pathlib import Path
from backupp.backup_with_path import child_directory ,adres_ile_yedekle_command

from backupp.file_classes import FileItem
from backupp.file_checks import FileChecks
from backupp.read_ignore import get_checker, get_checker_
from backupp.read_ignore_helpers import create_git_ignore_file
backup_folder = Path()
some_folder_for_test = Path() / "test1"
BACKUP_FOLDER = Path() / "test2"
import os
from backupp.files import create_dirs
create_dirs(some_folder_for_test)
create_dirs(BACKUP_FOLDER)
def some_items():
    items = ("asdf.RData", "sadf.R", "asdf.xlsx", "__pycache__", ".RData")
    return tuple(map(lambda x: some_folder_for_test / x, items))
def test_setup_content(capsys):
    c = get_checker_(some_folder_for_test, force=True)
    with capsys.disabled():
        s = c.get_content_setup_file()
        assert s
        # print(s)
def test_check(capsys):
    c = get_checker_(some_folder_for_test)
    with capsys.disabled():
        s = c.ignore_this(str(some_folder_for_test / ".RData"))
        print(s)
        s = c.ignore_this(str(some_folder_for_test / ".R"))
        print(s)
        _ = tuple(map(c.ignore_this, some_items()))
        print(_)
        _ = tuple(map(c.ignore_this, some_items()))
        print(_)
def get_some_file_items():
    def create_file_item(name):
        return FileItem(
            name,
            str(some_folder_for_test),
            str(Path() / some_folder_for_test / "xx"),
            str(some_folder_for_test),
            False,
        )
    names = (".RData", "xx.xlsx", "a.csv", "b.txt", "x.R", "a.py")
    return tuple(map(create_file_item, names))
def test_check_file_item(capsys):
    c = get_checker_(some_folder_for_test)
    with capsys.disabled():
        s = tuple(map(c.ignore_this, get_some_file_items()))
        print(s)
def test_check_ignore_file(capsys):
    """test_check_ignore_file"""
    c = get_checker_(some_folder_for_test)
    with capsys.disabled():
        r = c.check_ignore_file()
        print(f"test_check_ignore_file : {r}")
def test_write_check_ignore_file(capsys):
    c = get_checker_(some_folder_for_test)
    with capsys.disabled():
        create_git_ignore_file(Path(some_folder_for_test))
