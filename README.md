[![Python package](https://github.com/SermetPekin/backup2/actions/workflows/python-package.yml/badge.svg)](https://github.com/SermetPekin/backup2/actions/workflows/python-package.yml)


### backupp

Back ups your folder to your preferred local or network destination reading or creating a gitignore file.

### installation 
-U for the latest 
    
    pip install backupp -U         # or 
    # pip3 install backupp -U  

#### Usage from console (Win) / terminal on (linux / Mac)

    $ backupp /some_folder/that_folder  my_backup_folder

    $ backupp /some_folder/that_folder  path/to_my_backup_folder

    # backup current folder
    $ backupp .  path/to_my_backup_folder 

    # backup parent folder
    $ backupp ..  path/to_my_backup_folder 

#### gitignore file 
backupp package looks for a .gitignore file. If it does not exist it creates one for your folder. You may modify it to create rules which files/ folders to ignore just like git does. 

#### setup global backup folder 

    backupp --setup my_favorite_backup_folder

    backupp some_folder 

#### check backup setup  

displays your current setup and preferences


    backupp --check 


#### backup with commit   

similar to $ git add . ; git commit -m'Thisisacommitmessage' ; git push

    # creates a Thisisacommitmessage folder and backups 
    # your folders and files inside this new folder 
    # this is helpful when you would like to create breakpoints 
    backupp path/somepath/somefolder_commit_Thisisacommitmessage



