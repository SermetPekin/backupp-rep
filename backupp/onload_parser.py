
"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from pathlib import Path
from backupp._options import set_backup_folder
def get_parameters_from_console():
    import sys
    args = sys.argv
    return get_parameters_from_console_helper(args)
from backupp._options import get_default_backup_folder
def get_parameters_from_console_helper(args):
    """for testing"""
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