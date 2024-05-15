

import os
from dataclasses import dataclass
from backupp.files import Read, Write
from pathlib import Path
class OptionsCouldNotRead(BaseException):
    """OptionsCouldNotRead"""

@dataclass
class Options:
    backup_folder: Path = Path().resolve().parent / "backup_default"
    last_read: Path = Path() / "None"
    options_file: Path = (
        Path() / os.path.realpath(os.path.dirname(__file__)) / "options.cfg"
    )
    def __str__(self) -> str:
        return f"""
Options
===================================================
self.backup_folder : {self.backup_folder}
self.options_file : {self.options_file}
setup : {'ok' if self.options_file.exists()  else  'not ok'}
        """
    def str_dev__(self) -> str:
        return f"""
Options
===================================================
self.backup_folder : {self.backup_folder}
self.last_read : {self.last_read}
self.options_file : {self.options_file}
setup : {self.options_file.exists()}
        """
    def set(self, folder)->None :
        self.set_write(folder)
    def set_write(self, folder)->None:
        if folder != self.last_read:
            self.backup_folder = folder
            self.write(folder)
    def read(self) -> Path :
        content = Read(self.options_file)
        lines = content.splitlines()
        for line in lines:
            if "backup_folder" in line and line.startswith("backup_folder"):
                folder = line.split(":")[1]
                # print(f"Read on load {folder}")
                self.last_read = folder
                return Path() / folder
        raise OptionsCouldNotRead
    def write(self, folder: Path) -> None:
        print("Options file was created")
        Write(self.options_file, f"backup_folder:{folder}")
    def read_onload(self)->Path :
        self.backup_folder = Path() /  self.read()
        return self.backup_folder
    def set_onload(self)-> None:
        if not self.options_file.exists():
            self.set(self.backup_folder)
    def create(self)-> None:
        if not self.backup_folder.is_dir :
            os.makedirs(self.backup_folder)
    def clear(self)-> None:
        if self.options_file.exists():
            os.remove(self.options_file)
def get_options()->Options :
    options = Options()
    options.create()
    # options.clear()
    options.set_onload()
    options.read_onload()
    return options
def get_default_backup_folder() -> Path :
    options = get_options()
    return options.backup_folder

def set_backup_folder(folder):
    from backupp import GithubActions
    options = get_options()
    if Path(folder).is_dir():
        options.set(folder)
        options.read_onload()
        return
    print(f'Directory could not be found {folder}')
    if GithubActions().is_testing:
        return
    raise NotADirectoryError
def display_options():
    options =get_options()
    print(options)
