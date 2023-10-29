
#filename:file_classes.py
#folder:backupp
"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from dataclasses import dataclass
from abc import ABC, abstractmethod
from pathlib import Path
# ******************************************
#           FileItem                    *
# ******************************************
@dataclass
class FileItem:
    name: str
    source_full_path: Path
    dest_folder_: Path
    relFolder: str
    backupInstance: any
    extension: str
    dest_full_path: Path
    def __init__(self, name, source_full_path, dest_folder_, relFolder, backupInstance):
        self.backupInstance = backupInstance
        self.name = name
        self.get_folders(relFolder, source_full_path, dest_folder_)
        self.extension = self.get_extension(self.name)
    def __str__(self):
        create_repr_fileitem(self)
    def get_extension(self, name):
        a = name.split(".")
        if len(a) == 2:
            return a[1]
        return "--notFILE"
    def get_folders(self, relFolder, source_full_path, dest_folder_):
        self.rel_folder = relFolder
        if str(self.rel_folder).startswith("\\") or str(self.rel_folder).startswith(
            "/"
        ):
            self.rel_folder = str(self.rel_folder)[1:]
        self.source_full_path = Path() / source_full_path
        self.real_source_full_path: Path = Path() / source_full_path / self.name
        self.real_dest_folder = Path() / dest_folder_ / self.rel_folder
        self.dest_full_path = self.real_dest_folder / self.name
        # print(f"{ self.dest_full_path }{ dest_folder_ }")
def get_empty_file_item():
    return FileItem("empty.empty", "", "", "", "")
def create_repr_fileitem(self: any):
    return f"""
FILEITEM
===================================================
NAME : {self.name}
source : {self.real_source_full_path}
dest full path : {self.dest_full_path}
real_dest_folder : {self.real_dest_folder}
ext : {self.extension}
rel_folder : {self.rel_folder}
==================================================="""