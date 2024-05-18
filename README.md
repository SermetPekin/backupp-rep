# backupp

[![Python package](https://github.com/SermetPekin/backupp-rep/actions/workflows/python-package.yml/badge.svg)](https://github.com/SermetPekin/backupp-rep/actions/workflows/python-package.yml)

**backupp** is a Python package that automates the backup of folders to a specified local or network destination. It intelligently utilizes or generates a `.gitignore` file to manage which files or folders should be ignored during the backup process.

## Installation

Install the latest version of backupp using pip:

```bash
pip install backupp -U  # Alternatively, you can use pip3
```

## Usage

### Console (Windows) / Terminal (Linux/Mac)

To backup specific folders to a designated backup folder, use:

```bash
backupp /path/to/source_folder /path/to/backup_folder
```

Examples:

- Backup a specific folder:
  ```bash
  backupp /some_folder/that_folder my_backup_folder
  ```

- Backup the current folder:
  ```bash
  backupp . path/to_my_backup_folder
  ```

- Backup the parent folder:
  ```bash
  backupp .. path/to_my_backup_folder
  ```

## Handling .gitignore

The **backupp** package searches for an existing `.gitignore` file in the source directory. If it doesn't find one, it will create a default `.gitignore` file. You can modify this file to customize which files or folders should be excluded from backups, similar to how Git uses `.gitignore`.

## Setup Global Backup Folder

To set a default backup folder, which can be used for subsequent backup operations without specifying a path each time:

```bash
backupp --setup /path/to/my_favorite_backup_folder
```
## Backup to favorite folder


```bash
backupp path/source/somefolder   
```

## Backup current folder to favorite backup folder 

```bash
backupp . 
```


## Check Backup Setup

To display your current backup configuration and preferences:

```bash
backupp --check
```

