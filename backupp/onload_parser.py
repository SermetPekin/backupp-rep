from pathlib import Path
from backupp._options import set_backup_folder
from backupp._options import get_default_backup_folder
import sys


def get_parameters_from_console():
    args = sys.argv
    return get_parameters_from_console_helper(args)


def get_parameters_from_console_helper(args):
    """
    get_parameters_from_console_helper for testing

    """
    folder = False
    dest = get_default_backup_folder()
    if len(args) == 2:
        folder = args[1]
    if len(args) == 3:
        folder = args[1]
        dest = args[2]
    if folder == ".":
        import os

        folder = os.getcwd()
    if folder == "..":
        import os

        folder = os.getcwd()
        folder = Path(folder).resolve().parent
    return folder, dest
