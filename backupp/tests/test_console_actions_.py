# filename:test_ignore.py
# folder:backup\tests
from pathlib import Path

from backupp import adres_ile_yedekle_command
from backupp.backup_with_path import child_directory

# from backupp import *
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
    items = (( Path()/ 'ab/cd' , Path() / 'ab/cdx/xyz')  , )
    items_neg =  (( Path()/ 'ab/cd' , Path() / 'ab/cd/xyz')  , )
    def x(tuple_):
        return child_directory(*tuple_ )
    with capsys.disabled():

        _ = tuple(map( x  , items ))
        print(_)
        
        assert (not any( _ ))
        _ = tuple(map( x  , items_neg ))
        print(_)
        assert (all( _ ))