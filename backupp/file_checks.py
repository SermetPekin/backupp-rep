
#filename:file_checks.py
#folder:backupp
"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from abc import ABC, abstractmethod
from .file_classes import FileItem
# ******************************************
#           FileChecks                    *
#
class FileChecks(ABC):  # ******************
    fileExtensions: tuple
    sadeceProjectExtensions: bool = True
    def file_should_move(self, file_item: FileItem) -> bool:
        return file_item.extension in self.fileExtensions
    def name_format(self):
        return "ltd_types"
class FileChecks_for_Matlab_Projects(FileChecks):
    def __init__(self):
        self.fileExtensions = ("m", "txt", "json", "mat")
class FileChecks_for_Matlab_Projects_min(FileChecks):
    """minimum version of my Matlab projects"""
    def __init__(self):
        self.fileExtensions = ("m",)
class FileChecks_for_Python_Projects(FileChecks):
    def __init__(self):
        self.fileExtensions = ("py", "md", "txt", "js", "css", "json", "html")
class FileChecks_for_RProjects(FileChecks):
    def __init__(self):
        self.fileExtensions = (
            "R",
            "gz",
            "r",
            "h",
            "c",
            "py",
            "md",
            "txt",
            "js",
            "css",
            "json",
            "html",
        )
class FileChecks_for_CommonLangs(FileChecks):
    def __init__(self):
        self.fileExtensions = (
            "m",
            "c",
            "cpp",
            "h",
            "hpp",
            "R",
            "gz",
            "r",
            "h",
            "c",
            "py",
            "md",
            "txt",
            "js",
            "css",
            "json",
            "html",
        )
class FileChecks_for_JS_Projects(FileChecks):
    def __init__(self):
        self.fileExtensions = ("js", "json", "txt", "py", "md", "css", "html")