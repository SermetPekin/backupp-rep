
#filename:template_on_load.py
#folder:backupp
"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from backupp.files import WriteBytes, ReadBytes
from pathlib import Path
def create_git_ignore_file_onload():
    """create_git_ignore_file_onload
    """
    from backupp.py_template import template_py
    assert template_py is not None
    file_name = str(Path("") / ".gitignore")
    if Path(file_name).exists():
        return
    WriteBytes(file_name, bytes(template_py, encoding="utf-8"))
    content = ReadBytes(file_name)
    assert content