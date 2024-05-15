
"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
import sys
from pathlib import Path
from backupp.github_actions import GithubActions
from backupp.onload_parser import get_parameters_from_console
# from backupp.onload_parser import main_parser
from backupp.template_on_load import create_git_ignore_file_onload
from backupp._options import set_backup_folder, display_options

"""
ignore template file on load
"""
create_git_ignore_file_onload()


def main_parser():
    folder, dest = get_parameters_from_console()
    return main_parser_helper(folder, dest)


def main_parser_helper(folder, dest):
    '''for test separated'''
    from backupp.backup_with_path import adres_ile_yedekle_command
    if not folder:
        return help_display()
    if folder == "--setup":
        return set_backup_folder(dest)
    if folder == "--check":
        return check()
    if Path(folder).is_dir():
        return adres_ile_yedekle_command(folder, dest)
    else:
        print(f"could not find directory ...{folder}")
        if GithubActions().is_testing:
            return
        raise NotADirectoryError


def check():
    display_options()


def console_main(args_=None):
    main_parser()


def help_display():
    template = f'''
.......................................................................................................
.........................................    B A C K U P P    .........................................
.......................................................................................................

    
$ backupp some_folder/some some/backupfolder
    ... backups some_folder/some to some/backupfolder


$ backupp . some/backupfolder
    ... backups current folder to some/backupfolder 

    
$ backupp --setup some/backupfolder
    ... remembers some/backupfolder as your default storage folder 
    ... so that next time you can easily back up by giving only source folder's path


$ backupp .
    ... backups your current folder to your favorite storage folder


$ backupp pathto/somefolder
    ... backups some folder to your favorite storage folder


$ backupp --check 
    ... you may check your installation and favorite backup location
    
    
.......................................................................................................
.......................................................................................................

    '''
    print(template)
