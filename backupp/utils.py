

import string
import random
from pathlib import Path

true = True
false = False
from datetime import date, datetime
from backupp.github_actions import GithubActions

def pop_folder(folder: Path):
    if GithubActions().is_testing:
        return
    from pathlib import Path
    import subprocess, os
    try:
        subprocess.Popen(f"explorer {os.path.realpath(folder)}")
    except:
        pass

def get_date_as_str(clean=True):
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H_%M")
    if clean:
        """Dosya isimleri için"""
        template = f"{day}{month}{year}_{time}"
    else:
        time = now.strftime("%H:%M")
        template = f"{day}.{month}.{year}  {time}"

    return template

def yaz(copiedFiles, fileName):
    # self.copiedFiles
    text = "\n".join(copiedFiles)
    with open(fileName, "w") as file_:
        file_.write(text)

def yaz_file(content, file_name: Path):

    if isinstance(content, bytes):
        raise NotImplementedError
        # content =  str(content, 'UTF-8')
    assert content, "CONTENT is NONE "
    with open(file_name, "w") as file_:
        file_.write(content)

def dosya_yaz(fileName, content):
    with open(fileName, "w") as file_:
        file_.write(content)

def TarihTemizle(st):
    seps = [":", "-", ".", " "]
    nseps = ["_", "_", "_", "__"]
    for index, item in enumerate(seps):
        st = st.replace(item, nseps[index])
    return st


def check_if_one(names, name):
    yanit = False
    for name_ in names:
        if name_ in name:
            yanit = True
    return yanit

def get_random_hash(num):
    letters = string.ascii_letters
    randomF = "".join(random.choice(letters) for i in range(num))
    return randomF

