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
    return main_parser_helper( folder ,dest )

def main_parser_helper(folder ,dest ):
    '''for test separated'''
    from backupp.backup_with_path import adres_ile_yedekle_command

    if not folder :
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
# back up some folder to backup folder
backupp some_folder/some some/backupfolder

# back up current folder to backup folder
backupp . some/backupfolder

# saves your favorite backup storage 
backupp --setup some/backupfolder
 
# so that next time you can easily back up current folder with the following 
# back ups your current folder to your favorite storage folder
backupp . 

# back ups your some folder to your favorite storage folder
backupp pathto/somefolder
    '''
    print(template)