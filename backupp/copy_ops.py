"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""

import shutil
from datetime import datetime
import sys
from typing import List
import traceback

today = datetime.now()
from .Directory import *
from .type_defs import *


class OperationClass(ABC):
    def names(self, copiedFiles: List[FileItem]):
        return tuple(x.source_full_path for x in copiedFiles)

    @abstractmethod
    def action(self, file_item: FileItem, copiedFiles: List[FileItem]):
        """action"""


class OperationMock(OperationClass):
    """OperationMock"""

    @abstractmethod
    def action(self, file_item: FileItem, copiedFiles: List[FileItem]):
        """action"""
        print(file_item.name, " .. not copied just checking ..")


class OperationBasic(OperationClass):
    def action(self, file_item: FileItem, copiedFiles: list):
        DEST_FOLDER = (
            file_item.backupInstance.back_up_folder_name_no_date_static
            / file_item.rel_folder
        )
        # source full
        file_SOURCE_full_name = file_item.source_full_path / file_item.name
        # dest full
        file_DEST_full_name = DEST_FOLDER / file_item.name
        if file_SOURCE_full_name in copiedFiles:
            return
        try:
            self.process(
                file_item, DEST_FOLDER, file_SOURCE_full_name, file_DEST_full_name
            )

        except Exception as exc:
            traceback.print_exc(exc)

    def process_mock(
        self, file_item, DEST_FOLDER, file_SOURCE_full_name, file_DEST_full_name
    ):
        """MOCK"""

        print(
            f"""
============================================================        
file_item:         {file_item} 
DEST_FOLDER       {DEST_FOLDER} 
file_SOURCE_full_name :   {file_SOURCE_full_name}   
file_DEST_full_name:     {file_DEST_full_name} 
dest_full_path (Currently Not Used):     {file_item.dest_full_path} 
============================================================    
        """
        )

    def process(
        self, file_item, DEST_FOLDER, file_SOURCE_full_name, file_DEST_full_name
    ):

        file_item.backupInstance.create_directory(DEST_FOLDER)
        # copy
        shutil.copyfile(file_SOURCE_full_name, file_DEST_full_name)
