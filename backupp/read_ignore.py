

from pathlib import Path
from gitignore_parser import parse_gitignore
from abc import ABC, abstractmethod
from typing import Callable
from dataclasses import dataclass
from .files import Read, ReadBytes
from .file_classes import FileItem
# from .globals import ignore_file_name_for_test
from .type_defs import *
from .read_ignore_helpers import get_global_ignore_file_name
from .read_ignore_helpers import create_git_ignore_file
class IgnoreCheckFailed(BaseException):
    """IgnoreCheckFailed"""
class IgnoreCheck(ABC):
    """IgnoreCheck"""
    matches_instance: Callable
    setup_file: str = None
    def __init__(self, matches_instance: Callable, setup_file=None):
        self.matches_instance = matches_instance
        self.setup_file = setup_file
    def get_content_setup_file(self) -> bytes:
        return ReadBytes(self.setup_file)
    def get_content_as_str_safe(self):
        try:
            str_bytes = self.get_content_setup_file()
            return str(str_bytes, encoding="utf-8")
        except:
            return "{str_bytes content bytes error.}"
    def check_ignore_file(self) -> True:
        # if not Path(self.setup_file).is_file() or \
        #         not ReadBytes(Path(self.setup_file)).splitlines()[0] in (
        #                 b'#GlobalTemplateModified'):  # "#GlobalTemplateModifiedx"
        #     raise IgnoreCheckFailed
        return True
    def display_format(self, path_, res):
        ...
        res_ = "  .  " if res else "     "
        p = Path(path_)
        print(f"{res_}   {p.stem}  ")
    def ignore_this(self, file_maybe: str_path_f):
        """file_is_not ok"""
        if isinstance(file_maybe, FileItem):
            res = self.ignore_this_with_file_item(file_maybe)
            self.display_format(file_maybe.real_source_full_path, res)
        else:
            res = self.ignore_this_with_full_path(file_maybe)
            self.display_format(file_maybe, res)
        return res
    def ignore_this_with_file_item(self, file_item: FileItem):
        """ignore_this_with_file_item"""
        # return self.matches(str(Path() / file_item.source_full_path / file_item.name))
        return self.matches_instance(str(file_item.real_source_full_path))
    def ignore_this_with_full_path(self, file_name: str_path):
        """file_is_not ok"""
        return self.matches_instance(str(file_name))
class IgnoreCheckParseGitignore(IgnoreCheck):
    """IgnoreCheck_parse_gitignore"""
    matches_instance: Callable = parse_gitignore
    setup_file: Path = None
def get_checker():
    """Test için"""
    ignore_file_name = ignore_file_name_for_test
    matches_instance = parse_gitignore(ignore_file_name)
    ignore_check = IgnoreCheckParseGitignore(matches_instance, ignore_file_name)
    return ignore_check
from backupp.github_actions import get_input
def asked_and_created(folder, force=False):
    msg = ".gitignore file could not be found. Should script create a template for you? y/n"
    create_git_ignore_file(folder)
    # return True
    if force:
        create_git_ignore_file(folder)
        return True
    ans = get_input(msg , default = 'y')
    if ans.lower() != "n":
        create_git_ignore_file(folder)
        return True
    return False
def get_checker_(folder, force=False) -> IgnoreCheckParseGitignore:
    ignore_file_name = Path(folder) / ".gitignore"
    if not ignore_file_name.is_file():
        if asked_and_created(str(folder), force):
            assert ignore_file_name.is_file()
            ...
        else:
            raise NotImplementedError
            # return False
    # print("SETTING IGNORE CHECK...", ignore_file_name)
    matches_instance = parse_gitignore(ignore_file_name)
    ignore_check = IgnoreCheckParseGitignore(matches_instance, ignore_file_name)
    return ignore_check
def get_checker_with_global_template() -> IgnoreCheckParseGitignore:
    ignore_file_name = get_global_ignore_file_name()
    matches = parse_gitignore(ignore_file_name)
    ignore_check = IgnoreCheckParseGitignore(matches)
    return ignore_check
def ignore_this_global(file_name) ->bool :
    # print(f"checking {file_name} ...")
    ignore_check_fnc = get_checker_with_global_template()
    res = ignore_check_fnc.ignore_this(file_name)
    # print(f"checking {res} ...")
    return res
def check_all_files()->tuple :
    files = ("main.py", "main.txt", "sadf.R", "xx.R", "xxy.Rd")
    files = tuple(map(lambda x: Path() / x, files))
    # return tuple(map(ignore_this, files))
    return tuple(map(ignore_this_global, files))
if "__main__" == __name__:
    s = check_all_files()
    print(s)