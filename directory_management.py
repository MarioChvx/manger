import os
from pathlib import Path

def check_path(path_str):
    """ Check if the path exist and is a valid directory and return a Path object """
    wd = Path(path_str).resolve()
    if not wd.exists():
        raise Exception(f'Sorry, "{path_str}" do not exist')
    if not wd.is_dir():
        raise Exception(f'Sorry, "{path_str}" is not a directory')
    return wd

def move_to(path:Path):
    os.chdir(path)

def create_father(name:str, wd:Path):
    """ Create a new file in the path with the name and return a path to it """
    father_path = wd / name
    if not father_path.exists():
        os.mkdir(father_path)
    return father_path

def create_chapter(number:int, padding:int, fd:Path):
    """ Create a new file in the path with the number and return a path to it """
    chapter_path = fd / f'chapter_{number:0{padding}}'
    if not chapter_path.exists():
        os.mkdir(chapter_path)
    return chapter_path
