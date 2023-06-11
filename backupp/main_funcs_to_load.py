"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
import sys
from pathlib import Path

from backupp.onload_parser import get_parameters_from_console

# from backupp.onload_parser import main_parser
from backupp.template_on_load import create_git_ignore_file_onload
from backupp._options import set_backup_folder, display_options


"""
ignore template file on load 
"""
create_git_ignore_file_onload()


def main_parser():
    from backupp.backup_with_path import adres_ile_yedekle_command 

    folder, dest = get_parameters_from_console()
    if folder == "--setup":
        return set_backup_folder(dest)

    if folder == "--check":
        return check()

    if Path(folder).is_dir():
        return adres_ile_yedekle_command(folder, dest)
    else:
        print("coult find directory ...{folder}")
        raise NotADirectoryError

def check():
    display_options()


def console_main(args_=None):
    main_parser()
