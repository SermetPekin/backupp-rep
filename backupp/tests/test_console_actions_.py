from pathlib import Path
from backupp.backup_with_path import (
    child_directory,
    adres_ile_yedekle_command,
    get_commit_from_source,
)
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
from backupp.github_actions import get_input


def test_backup_complete(capsys):
    with capsys.disabled():
        adres_ile_yedekle_command(str(some_folder_for_test), BACKUP_FOLDER, force=True)


def test_get_parameters_from_console_helper(capsys):
    from backupp.onload_parser import get_parameters_from_console_helper

    items = (
        ("x.py", ".", "some_folderx"),
        ("y.py", "some_folderx", "some_foldery"),
        ("y.py", "..", "some_foldery"),
        ("y.py", ".."),
    )
    with capsys.disabled():
        items = tuple(map(str, (map(get_parameters_from_console_helper, items))))
        print("\n")
        print("\n".join(items))


def test_get_input(capsys):
    with capsys.disabled():
        ans = get_input("test", default="y")
        print(ans)
        assert ans == "y"
        ans = get_input("test")
        print(ans)
        assert ans == False


from backupp.github_actions import GithubActions


def test_github_actions(capsys):
    with capsys.disabled():
        ans = GithubActions().is_testing()
        print(ans)


def test_check_test(capsys):
    with capsys.disabled():
        import sys

        print(sys.argv)


def test_child_directory(capsys):
    items = ((Path() / "ab/cd", Path() / "ab/cdx/xyz"),)
    items_neg = ((Path() / "ab/cd", Path() / "ab/cd/xyz"),)

    def x(tuple_):
        return child_directory(*tuple_)

    with capsys.disabled():
        _ = tuple(map(x, items))
        print(_)
        assert not any(_)
        _ = tuple(map(x, items_neg))
        print(_)
        assert all(_)


from backupp._options import get_options, Options, set_backup_folder


def test_setoptions(capsys):
    with capsys.disabled():
        options = get_options()
        isinstance(options, Options)


from backupp.utils import get_random_hash


def test_set_backup_folder(capsys):
    folder = Path() / "test_test1" / get_random_hash(5)
    import os

    if not folder.is_dir():
        os.makedirs(folder)
    options = get_options()
    set_backup_folder(folder)
    options = get_options()
    assert str(folder) == str(options.backup_folder)
    assert str(folder) == str(options.read_onload())


def test_get_commit_from_source(capsys):
    some_folders: tuple = (
        Path(r"C:\\Users/somefolder/some_commit_xx"),
        Path("de_commit_test"),
        "folder",
        Path() / "folder_commit_some",
    )
    with capsys.disabled():
        x = tuple(map(get_commit_from_source, some_folders))
        print("*" * 50)
        print("\n".join(map(str, x)))
        print("*" * 50)


from backupp import *
from backupp import BackupClass
from pathlib import Path
from backupp.Directory import DirectoryClass

import tempfile


def test_copy(capsys):
    with tempfile.TemporaryDirectory() as dir:
        dir = Path(dir)
        project = DirectoryClass(Path('.') ,  dir)
        with capsys.disabled():

            backup = BackupClass(project)
            backup.do_backup()
