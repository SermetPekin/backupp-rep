
"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
import typing as t
from pathlib import Path
from backupp.file_classes import FileItem
str_path = t.Union[str, Path]
str_path_f = t.Union[str, Path, FileItem]