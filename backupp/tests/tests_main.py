import pytest
from backupp import *
from backupp import BackupClass
from pathlib import Path

import tempfile



# def test_copy(capsys):
#     with tempfile.TemporaryDirectory() as dir:
#         dir = Path(dir)
#         project = DirectoryClass(".", dir)

#         with capsys.disabled():

#             backup = BackupClass(project)
#             # backup.set_destination()
#             backup.do_backup()
