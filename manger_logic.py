import re
import math
import directory_management as dm
import web_scraping as ws
import dir_to_pdf #as pdf

def download_manga(url: str, title: str, path: str):
    soup_home = ws.get_soup_page(url)
    chapters_urls = ws.get_chapters_urls(soup_home)
    chapters_index = [(int(re.findall('[\d]+', re.findall('chapter.*\d',url)[0])[0]), url) for url in chapters_urls]
    chapters_index.sort()
    wd = dm.check_path(path)
    father_path = dm.create_father(title, wd)
    padding = math.floor(math.log(len(chapters_urls), 10))
    for chapter in chapters_index:
        i, chapter_url = chapter[0], chapter[1]
        chapter_nums = re.findall('[\d]+', re.findall('chapter.*\d',chapter_url)[0])

        if len(chapter_nums) > 1:
            chapter_name = f'chapter_{int(chapter_nums[0]):0{padding}}' + '.' + '.'.join(chapter_nums[1:])
        else:
            chapter_name = f'chapter_{int(chapter_nums[0]):0{padding}}'

        if not dm.exist_path(dm.chapter_path(father_path, chapter_name)):
            downloading_path = dm.create_downloading(father_path)
            dm.move_to(downloading_path)
            click.echo(f'Downloading {chapter_name}...')
            ws.download_chapter(chapter_url)
            dm.move_to(father_path)
            dm.rename_chapter(father_path, chapter_name)
        else:
            pass