

import os
import shutil
from os import listdir
from os.path import isfile, join
from datetime import date, datetime
import sys
from pathlib import Path
from typing import List
from .copy_ops import Operation_sadece_guncelle, OperationKopyala
sys.path.append(".")
sys.path.append("..")
from functools import wraps
today = datetime.now()
from .Directory import *
from .type_defs import *
@dataclass
class BackupClassBase(ABC):  # ***************************
    proje: DirectoryClass
    newDestinationFolderFinal: any
    fileChecker: FileChecks
    kopyala: bool
    operation: callable
    root: Path
    dest_adres_full: Path
    onay: bool
    dest: Path