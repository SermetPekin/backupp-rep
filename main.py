from backupp import BackupClass
from pathlib import Path
from backupp.Directory import DirectoryClass




def backup_now(source = '.' , destination = Path('..') / 'SomeFolderForBackup' ):
    project = DirectoryClass(Path(source) ,  Path(destination))
    backup = BackupClass(project)
    backup.do_backup()


if "__main__" == __name__:
    backup_now()



"""
    when installed from PYPI with command below 
    pip install backupp 

    it can be used as a console application. 

    
    # command source destination
    $ backupp . ../SomeFolderForBackup 
    
    # or 
    
    # command --setup destination 
    $ backupp --setup ../SomeFolderForBackup
    
    # command source 
    $ backupp . 


"""