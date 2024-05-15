

"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from pathlib import Path
# DEFAULT_PROJECT_YEDEK_ADRES =  get_default_backup_folder() #Path(r"test2")
ignore_file_name_for_test = Path() / "test1" / ".gitignore"
from backupp.files import create_dirs
# create_dirs(DEFAULT_PROJECT_YEDEK_ADRES)
create_dirs(Path() / "test1")