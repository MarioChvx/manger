import re
import math
import click
from typing import List, Dict

import directory_management as dm
import web_scraping as ws
from dir_to_pdf import convert_pdf

def download_manga(url: str, title: str, path: str, pdf: bool, range):
    soup_home = ws.get_soup_page(url)
    title = title if title is not None else soup_home.title.string
    chapters_urls = ws.get_chapters_urls(soup_home)
    wd = dm.check_path(path)
    father_path = dm.create_father(title, wd)

    padding = math.floor(math.log(len(chapters_urls), 10))
    # for url in list(reversed(chapters_urls)):
    for url in chapters_urls:
        download_chapter(url, father_path, pdf= pdf, padding= padding)

def download_chapter(url: str, path: str, title: str = '', pdf: bool = False, padding: int = 0):
    chapter_name = guess_title(url, title, padding)
    if not dm.exist_path(dm.chapter_path(path, chapter_name)):
        downloading_path = dm.create_downloading(path)
        dm.move_to(downloading_path)
        click.echo(f'Downloading {chapter_name}...')
        ws.download_chapter(url)
        dm.move_to(path)
        chapter_path = dm.rename_chapter(path, chapter_name)
        print(path)
        from pathlib import Path
        if pdf:
            convert_pdf(chapter_path, path)

def guess_title(url: str, title:str, padding: int = 0):
    if title is None:
        return url.split('/')[-1]
    elif title == '':
        chapter_nums = re.findall('[\d]+', re.findall('chapter.*\d',url)[0])
        res = f'chapter_{int(chapter_nums[0]):0{padding}}'
        if len(chapter_nums) > 1:
            res += '.'.join(chapter_nums[1:])
        return res
    else: 
        return title

def convert_to_pdf(path, multiple: bool, destiny: str):
    wd = dm.chapter_path(path)
    if not multiple:
        convert_pdf(wd, destiny)
        return
    save_path = dm.chapter_path(destiny)
    for directory in wd.iterdir():
        if not directory.is_dir():
            pass
        convert_pdf(directory, destiny)