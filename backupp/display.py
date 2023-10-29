
#filename:display.py
#folder:backupp
"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from backupp.backup_with_path import adres_ile_yedekle
from backupp.file_checks import *
# ------------------------------------************************************
from .utils import *
from .menu import *
from dataclasses import dataclass
from typing import Optional
@dataclass
class MenuMaker:
    name: str
    secenekler_: list
    names_: list
    root: Optional[str] = False
    def __post_init__(self):
        self.make()
    def make(self):
        self.secenekler_prod = {
            (index + 1): func for index, func in enumerate(self.secenekler_)
        }
        self.names__prod = {(index + 1): name for index, name in enumerate(self.names_)}
        num = len(self.names__prod.keys()) + 1
        self.secenekler_prod.update({num: self.exit_})
        self.names__prod.update({num: "exit"})
    def exit_(self):
        if self.root:
            exit()
        return
    def display(self):
        template = "*" * 50 + f"\n        {self.name}       \n" + "*" * 50 + "\n"
        for index, item in self.names__prod.items():
            template += f"{index}  :  {item} \n"
        template += "your choice ? "
        ans = get_input(template, default="exit")
        if str(ans).isnumeric() and int(ans) in self.secenekler_prod.keys():
            func = self.secenekler_prod[int(ans)]
            if callable(func):
                func()
            else:
                print(ans)
                print("Seçenek uygun değil")
    def get_choice(self):
        template = "*" * 50 + f"\n        {self.name}       \n" + "*" * 50 + "\n"
        for index, item in self.names__prod.items():
            template += f"{index}  :  {item} \n"
        template += "your choice ? "
        ans = get_input(template, default="exit")
        if str(ans).isnumeric() and int(ans) in self.secenekler_prod.keys():
            func = self.secenekler_prod[int(ans)]
            if callable(func):
                return func
            else:
                print(ans)
                print("Not a valid choice!")
class DisplayFileChecker:
    def secenekler(self):
        def general_picker():
            return FileChecks_for_CommonLangs
        def js_picker():
            return FileChecks_for_JS_Projects
        def matlab_picker():
            return FileChecks_for_Matlab_Projects
        def py_picker():
            return FileChecks_for_Python_Projects
        def r_picker():
            return FileChecks_for_RProjects
        menuM = MenuMaker(
            "File Checker ",
            [
                general_picker,
                js_picker,
                matlab_picker,
                py_picker,
                r_picker,
            ],
            [
                "general_FileCheck",
                "js_FileCheck",
                "matlab_FileCheck",
                "py_FileCheck",
                "r_FileCheck",
            ],
        )
        menuM.make()
        return menuM.get_choice()
class DisplayBackup:
    def secenekler(self):
        menuM = MenuMaker("Backup ", [adres_ile_yedekle], ["Adresle Yedekle"])
        menuM.make()
        menuM.display()