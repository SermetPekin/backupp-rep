
from backupp.github_actions import get_input
from .Directory import *
from .file_classes import *
from .Directory import DirectoryClass
from .file_checks import (
    FileChecks_for_RProjects,
    FileChecks_for_Python_Projects,
    FileChecks_for_CommonLangs,
    FileChecks,
)
from .menu import yedekle_this, yedekle_this_onayisteme
from datetime import datetime


def get_date_as_str():
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H_%M")
    return f"{day}{month}{year}_{time}"


def guess_file_checker(source_folder: Path):
    if "R_Projects" in str(source_folder):
        return FileChecks_for_RProjects
    return FileChecks_for_Python_Projects


from .read_ignore import get_checker_


def dynamic_project_yedekle(
        source_folder: Path,
        dest_folder: Path,
        commit: bool,
        onay_isteme=False
):
    from .display import DisplayFileChecker
    dest_folder = Path(dest_folder)
    if commit:
        dest_folder = (
                dest_folder
                / source_folder.stem
                / f"{source_folder.stem}_{commit}_{get_date_as_str()}"
        )
    else:
        dest_folder = dest_folder / source_folder.stem
    file_checker = FileChecks_for_CommonLangs
    if not get_checker_(source_folder):
        file_checker = DisplayFileChecker().secenekler()()
    funcs = {True: yedekle_this_onayisteme, False: yedekle_this}
    backup_func = funcs[onay_isteme]
    projects = [DirectoryClass(source_folder, dest_folder, fileChecker=file_checker())]
    backup_func(projects)


def adres_ile_yedekle_command(source_folder_, dest_folder, force=False):
    """for console"""
    source_folder_, commit = get_commit_from_source(source_folder_)
    return adres_ile_yedekle_helper(source_folder_, dest_folder, commit=commit)


def adres_ile_yedekle():
    """for the menu"""
    dest_folder: Path = get_default_backup_folder()
    source_folder_ = get_input(
        r"Project address ? (Commit mesajı e.g.: "
        r"folder1\folder|unit_test1)  or exit => ",
        default=False
    )
    return adres_ile_yedekle_helper(source_folder_, dest_folder)


def adres_ile_yedekle_helper(source_folder_, dest_folder, commit=False):
    """adres_ile_yedekle_helper"""
    if "exit" == str(source_folder_).lower():
        return
    source_folder_, commit = get_commit_from_source(source_folder_)
    if not source_folder_.is_dir():
        print("Directory error type exit to exit")
        return NotADirectoryError  
    if child_directory(source_folder_, dest_folder):
        raise ChildDirectoyCannotBeBackupAddress

    # YEDEKLE
    dynamic_project_yedekle(source_folder_, dest_folder, commit)


def child_directory(source_folder_: Path, dest_folder: Path):
    return Path(dest_folder).is_relative_to(source_folder_)


class ChildDirectoyCannotBeBackupAddress(BaseException):
    """Child directory cannot be given as a backup directory"""


def get_commit_from_source(source_folder_: Path) -> tuple:
    commit = False
    if "|" in str(source_folder_):
        source_folder_, commit = str(source_folder_).split("|")
    elif "_commit_" in str(source_folder_):
        source_folder_, commit = str(source_folder_).split("_commit_")
    source_folder = Path(source_folder_)
    return source_folder, commit
