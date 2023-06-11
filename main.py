
"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from backupp import console_main
# from backupp.adres_ile_yedekle import adres_ile_yedekle_command
# ------------------------------------************************************
from backupp.display import *
from backupp.template_on_load import create_git_ignore_file_onload
from backupp.onload_parser import main_parser


def main():
    DisplayBackup().secenekler()
if __name__ == '__main__':
    # main()
    print("start")
    create_git_ignore_file_onload()

    # main_parser()
    main()


