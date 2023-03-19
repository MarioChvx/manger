import click
import directory_management as dm
import web_scraping as ws
import re
import math
from dirtopdf.dirtopdf import dirtopdf

@click.command
@click.option(
    '--title',
    prompt = 'Provide the title of the manga',
    help = 'The title of the manga, is going to be used to name files, if is not provided the app will ask for it.')
@click.option('--url',
    prompt = 'Provide the home direction form the manga site',
    help = 'The URL where the list of available chapters is displayed, if is not provided the app will ask for it.')
@click.option('--path',
    default='.',
    help='The path to save the downloads, if is not provided current path will be used')
def manger(title: str, url: str, path: str):
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
            # dirtopdf(father_path.joinpath(chapter_name), father_path.joinpath('chapters_pdf'))
        else:
            pass


if __name__ == '__main__':
    manger()