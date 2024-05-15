from os import listdir
from os.path import isfile, join
from datetime import date, datetime
from typing import Tuple, List
from .Backup_base import BackupClassBase
from .copy_ops import Operation_sadece_guncelle, OperationKopyala
from backupp.colors import *
from functools import wraps

today = datetime.now()
from .Directory import *
from .type_defs import *
from backupp.github_actions import *


class NoInternetConnection(BaseException):
    """NoInternetConnection"""


############################## main ##########################


def go_back_for_R_Projects(full_path: Path):
    folder = Path(full_path).stem
    if "html" in str(full_path):
        return True
    # raise NotImplementedError
    if str(folder) in ("html", "man", "data", ".Rproj.user"):
        return True
    return False


def starts_with_underscore(full_path: Path):
    folder = Path(full_path).stem
    if str(folder).startswith("_"):
        return True
    return False


import os
from dataclasses import field


import traceback


@dataclass
class BackupClass(BackupClassBase):
    proje: DirectoryClass
    newDestinationFolderFinal: any
    fileChecker: FileChecks
    kopyala: bool
    operation: callable
    root: Path
    dest_adres_full: Path
    onay: bool
    dest: Path
    copiedFiles: List[FileItem] = field(default=list)

    def __init__(
        self,
        proje=None,
        kopyala=False,
        createFolder=False,
        deepCopy=False,
        fileChecker=None,
        sadeceGuncelle=True,
        *args,
        **kw,
    ):
        self.proje = proje
        self.newDestinationFolderFinal = False
        self.fileChecker = self.proje.fileChecker
        self.kopyala = kopyala
        self.kw = kw
        self.args = args
        if sadeceGuncelle:
            self.operation = Operation_sadece_guncelle()
        else:
            self.operation = OperationKopyala()
        self.initials()
        ##
        self.proje.ignore_checker.check_ignore_file()
        if createFolder:
            self.create_directory(self.proje.destDir)

    def initials(self):
        self.copiedFiles: List[FileItem] = []
        self.onay = self.proje.onay
        self.root = self.proje.sourceDir
        self.dest = self.proje.destDir
        self.dest_adres_full = self.proje.destDir
        self.stop = False
        self.set_destination(Path() / "test")

    def name_format(self, folder_name: Path) -> Path:
        f = folder_name
        if self.kopyala:
            # f = folder_name
            raise NotImplementedError
        else:
            today = datetime.now()
            tarih_name = TarihTemizle(str(today))
            self.back_up_folder_name_no_date = Path() / folder_name
            self.back_up_folder_name_no_date_static = (
                self.back_up_folder_name_no_date / "static"
            )
            self.back_up_folder_name_full = f = os.path.join(folder_name, tarih_name)
            self.back_up_folder_name = tarih_name
        return Path(f)

    def set_destination(self, dest_adres: Path = False):
        if dest_adres is not False:
            self.dest_adres = dest_adres
        self.dest_adres_full = (
            str(self.name_format(self.dest)) + "_" + self.fileChecker.name_format()
        )
        self.newDestinationFolderFinal = self.dest_adres_full
        self.create_directory(self.back_up_folder_name_no_date_static)

    def check_conn(self):
        return True  # used to be Request class here. For local backups no need a connection

    def check_dest_and_backup(self):
        if self.check_conn():
            print("internet connection works ")
        else:
            if "http:" in self.dest_adres:
                print(
                    True,
                    "backup_src 118 : No internet connection",
                )
                raise NoInternetConnection
        self.dest = self.dest_adres_full
        self.do_backup()

    def create_directory(self, address: Path) -> None:
        if not Path(address).exists():
            print("*" * 50)
            print_with_success_style(address)
            print("*" * 50)
            os.makedirs(address, exist_ok=True)

    def get_info(self):
        dec = "=" * 50 + "Project information " + "=" * 50 + "\n"
        dec += f"Source folder :{self.proje.sourceDir} \n"
        dec += f"Destination Folder :{self.proje.destDir} \n\n\n"
        dec += "=" * 120
        print_with_success_style(dec)
        if not self.onay:
            return True
        ans = get_input("continue (y/n)?", default="y")
        if ans in ("y", "Y"):
            return True
        else:
            return False

    def do_backup(self, source=None, onay: bool = True, *args, **kwargs):
        """yedekle"""
        self.onay = onay
        if not self.get_info():
            return
        if self.root is None:
            raise NotImplementedError

        folders = self.getFolderNames(self.root)
        self.show_files(self.root)
        from rich.progress import Progress

        with Progress() as progress:
            task1 = progress.add_task("[cyan]Copying...", total=1000)
            last_adv = 0
            for index, item in enumerate(folders):
                adv = (index + 1) / len(folders)
                proc = (adv - last_adv) * 1000
                last_adv = adv
                progress.update(task1, advance=proc)
                if not self.check_if_ignore_nec_folder(item):
                    self.show_files(self.root / item)
                if self.check_if_ignore_nec_folder(item) is False:
                    self.search_recursively(self.root / item)
        self.result_report()

    def result_report(self):
        """result_report"""
        template = create_template_backup(self)
        yaz_file(
            template,
            Path() / str(self.back_up_folder_name_no_date_static) / "fileTree.txt",
        )
        print_with_creating_style("creating backup history file...")
        backup_hist_dir = Path() / self.proje.sourceDir / "Backup_history"
        self.create_directory(backup_hist_dir)
        tarih = get_date_as_str()
        if backup_hist_dir.is_dir():
            yaz_file(template, backup_hist_dir / f"fileTree{tarih}.txt")
            pop_folder(Path() / self.proje.sourceDir)
            pop_folder(Path() / self.back_up_folder_name_no_date_static)

    def show_files(self, folder: Path) -> bool:
        """show_files"""
        folder = str(folder)
        dest = self.dest_adres_full
        relFolder = folder.replace(str(self.root), "")

        print_with_success_style("created {} ".format(folder))
        print_with_info_style(folder.split(r"\\")[-1], ">>")
        files = self.getFileNames(folder)
        checked_file = self.check_get_ignore_first(Path() / folder)
        if checked_file:
            """IGNORE"""
            print("Ignoring top level ")
            import time

            time.sleep(2)
            return True
        file_items = [
            FileItem(name, folder, self.proje.destDir, relFolder, self)
            for name in files
        ]
        _ = list(map(self.add_for_operation, file_items))
        if len(files):
            files_str = "files were" if len(files) > 1 else "file was"
            print_with_success_style(f"{len(files)} {files_str}   copied.")
            print("*" * 50)
        else:
            print_with_success_style(f"No file was copied.")
            print("*" * 50)

    def add_for_operation(self, file_item: FileItem):
        """add_for_operation"""
        if self.check_if_ignore_necessary(file_item):
            return
        try:
            self.operation.action(file_item=file_item, copiedFiles=self.copiedFiles)
            self.copiedFiles.append(file_item)
        except Exception as exc:
            print(file_item)
            traceback.print_exc()

    def check_if_ignore_nec_folder(self, folder: Path) -> bool:
        """check_if_ignore_nec_folder"""
        return self.check_get_ignore_first(Path() / self.root / folder)

    def check_get_ignore_first(self, file_item_whatever: str_path_f) -> bool:
        """check_get_ignore_first"""
        return self.proje.ignore_checker.ignore_this(file_item_whatever)

    def check_if_ignore_necessary(
        self, file_item: FileItem = get_empty_file_item()
    ) -> bool:
        """check_if_ignore_necessary"""
        return self.check_get_ignore_first(file_item)

    def search_recursively(self, adres: Path) -> None:
        """search_recursively"""
        folders = self.getFolderNames(adres)
        if not self.check_if_ignore_nec_folder(adres):
            self.show_files(adres)
        for folder in folders:
            print_with_info_style("===>{}".format(folder))
            if self.check_if_ignore_nec_folder(folder):
                continue
            if go_back_for_R_Projects(Path(adres) / folder):
                continue
            self.show_files(Path(adres) / folder)
            if not self.stop:
                self.search_recursively(adres / folder)

    def getFileNames(self, adres: str) -> list:
        onlyfiles = [f for f in listdir(adres) if isfile(join(adres, f))]
        # print(onlyfiles)
        return onlyfiles

    def getFolderNames(self, adres: Path) -> list:
        folders = [f for f in listdir(adres) if not isfile(join(adres, f))]
        return folders


def create_template_backup(self):
    def display(item: FileItem):
        return rf"{item.rel_folder}/{item.name}"

    files = "\n".join(tuple(map(display, self.copiedFiles)))
    template_ignore = self.proje.ignore_checker.get_content_setup_file()
    template = f"""
Son yedekleme :
----------------------------------
{get_date_as_str(False)}
==================================
{self.proje.sourceDir}
{self.proje.destDir}
==================================
___________________________________ Files
{files}
___________________________________ gitignore template
{template_ignore}
 """
    return template


if "__main__" == __name__:
    backup = BackupClass()
    backup.set_destination(Path() / "test")
    # backup.do_backup()
