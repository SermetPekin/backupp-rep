from backupp import BackupClass
from pathlib import Path


def b():
    backup = BackupClass()
    backup.set_destination(Path() / "test")
    backup.do_backup()


if "__main__" == __name__:
    # b()
    ...
