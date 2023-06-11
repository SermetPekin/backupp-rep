"""
--------------------------------------
   Developer : Sermet Pekin
    @ project Backup
    @ 2022 January
--------------------------------------
"""
from .utils import *
from .Backup_src import *
from backupp.github_actions import get_input


def testCon():
    backup = BackupClass()
    return backup.request_.test_connection()


def disp(item):
    return "." * 15 + item + "." * 15


def print_done(backup: BackupClass):
    """Show info when copy is done for a project"""
    temp = "=" * 50
    l = len(backup.copiedFiles)
    template = f"""
    {temp}
    {disp("source")}
    {backup.proje.sourceDir}
    {disp("files were copied")}
    {l} files were copied to directory
    {disp("Destination")}
    {backup.proje.destDir}
    {temp}
    """
    print(template)


def loopProjects(array, onay_iste=False):
    # onay_iste = False
    for proje in array:
        backup = BackupClass(proje=proje)
        backup.yedekle(onay=onay_iste)
        # print(backup.copiedFiles)
        print_done(backup)


def detay_goster(items):
    for item in items:
        print(" . {}, ".format(item.name))
    ans = get_input("continue to backup? ?(y/n)", default="y")
    if ans == "n" or ans == "N":
        return false
    return true


def yedekle_this(projects):
    onay_iste = False
    if not detay_goster(projects):
        return
    loopProjects(projects, onay_iste)


def yedekle_this_onayisteme(projects):
    onay_iste = False
    loopProjects(projects, onay_iste)
