import os
import click
import shutil
from pathlib import Path

def exist_path(path: Path):
    return path.exists()

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

def create_downloading(path: Path):
    down_path = path / 'downloading'
    if down_path.exists():
        shutil.rmtree(down_path)
    os.mkdir(down_path)
    return down_path

def rename_chapter(father_path: Path, chapter_name: str):
    os.rename(father_path / 'downloading', father_path / chapter_name)
    return father_path / chapter_name

def create_father(name: str, wd: Path):
    """ Create a new file in the path with the name and return a path to it """
    father_path = wd.joinpath(name)
    if not father_path.exists():
        os.mkdir(father_path)
        click.echo(f'Created {father_path}')
    return father_path

def chapter_path(father_path: Path, chapter_name: str):
    """ Create a new file in the path with the number and return a path to it """
    return father_path / chapter_name

def read_file(path:Path):
    content: str = str()
    with open(path, 'r') as f:
        for line in f:
            content += line
    return content

def has_subdirectories(path: Path):
    if not path.is_dir():
        raise Exception('Isn\'t a directory')
    for son in path.iterdir():
        if son.is_dir():
            return True
        pass