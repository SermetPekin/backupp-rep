

"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from .file_checks import FileChecks_for_Matlab_Projects, FileChecks
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable
from gitignore_parser import parse_gitignore
from ._options import *
from .file_classes import *
import json
from .read_ignore import get_checker, IgnoreCheckParseGitignore, IgnoreCheck
from .utils import *
all_directories = []
output_folder = r"out"
# ignore_check = get_checker()
from .read_ignore import get_checker_
@dataclass
class DirectoryClass_limited:
    name: str
    sourceDir: str
    destDir: str
    fileChecker: str
@dataclass
class DirectoryClass(object):
    sourceDir: Path
    destDir: Path
    fileChecker: FileChecks = FileChecks_for_Matlab_Projects()
    ignore_folders: tuple = ()
    mutlaka_ekle_file_types: tuple = ()
    ignore_file_types: str = ()
    ignore_file_names: str = ()
    onay: bool = True
    instances: list = field(default_factory=list)
    ignore_checker: IgnoreCheck = False
    def __post_init__(self):
        self.ignore_checker = get_checker_(self.sourceDir)
        # exit()
        # "\u005c" karakteri backslash Unicode
        Escaped_backslash = "\u005c"
        self.name = str(self.sourceDir).split(Escaped_backslash)[-1]
        self.limited_instance = DirectoryClass_limited(
            self.name, self.sourceDir, self.destDir, self.fileChecker.__class__.__name__
        )
        self.instances.append(self)
        all_directories.append(self)
        # print("inserted ::" + self.name)
    def get_all_instances(self):
        return self.instances
    @staticmethod
    def print_nicely(instances):
        for item in instances:
            print(item.sourceDir)
    def get_repr_json(self):
        item = self.name
    @staticmethod
    def yaz_json(instances):
        json_icerik = {}
        # dosya_yaz("data.txt", "content")
        for index, item in enumerate(instances):
            item_json = json.dumps(item.limited_instance.__dict__, indent=4)
            json_icerik[index + 1] = item_json
        json_data = json_icerik
        with open(output_folder + r"\\data.json", "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False)
    @staticmethod
    def read_json():
        f = open(output_folder + r"\\" + "data.json", encoding="utf-8")
        data = json.loads(f.read())
        for item in data.items():
            b = json.loads(item[1])
            print(b["name"], b["fileChecker"])