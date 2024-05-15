

"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from pathlib import Path
from .files import Read, ReadBytes, WriteBytes
from .read_ignore_templates import git_ignore_template_for_R
from .utils import yaz_file
def get_global_ignore_file_name() -> Path:
    global_Template_folder = Path("")
    return Path() / global_Template_folder / ".gitignore"
def get_global_template():
    file_name = get_global_ignore_file_name()  # Path() / global_Template_folder / ".gitignore"
    assert file_name.is_file(), "get_global_template Dosyası bulunamadı"
    content = Read(file_name)
    print(content.splitlines()[0])
    return content
def create_git_ignore_file(folder):
    """create_git_ignore_file
    """
    template = get_global_template()
    # print(template)
    assert template is not None
    # yaz_file(template, Path() / folder / ".gitignore")
    WriteBytes(Path() / folder / ".gitignore", bytes(template, encoding="utf-8"))
    content = ReadBytes(Path() / folder / ".gitignore")
    assert content
def create_git_ignore_file_for_RProjects(folder, template=git_ignore_template_for_R):
    yaz_file(template, Path() / folder / ".gitignore")