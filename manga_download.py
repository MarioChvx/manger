import click
import directory_management as dm
import web_scraping as ws
import re
import math


@click.command()
@click.option('--name',  prompt='Provide the title of the manga',           help='The title of the manga, is going to be used to name files')
@click.option('--url',   prompt='Provide the URL form the start chapter',   help='The URL where the download is going to start the number of the chapter should be surrounded by []')
@click.option('--num',   default=1,     help='The number of chapters that is going to be downloaded')
@click.option('--path',  default='.',   help='The path to save the downloads if not provided current path will be used')
def by_chapter_link(name, url, num, path):
    """Creates a new directory in the specified path with the name and sub-directories where the download images will be stored."""
    wd = dm.check_path(path)
    father_path = dm.create_father(name, wd)

    chapters_urls = ws.gen_chapters_urls(url, int(num))
    max_num = chapters_urls[-1][0]
    padding = math.floor(math.log(max_num, 10))

    for chapter_url in chapters_urls:
        chapter_name = f'chapter_{chapter_url[0]:0{padding}}'
        download_chapter(chapter_url[1], chapter_name, father_path)

@click.command()
@click.option('--name',  prompt='Provide the title of the manga',           help='The title of the manga, is going to be used to name files')
@click.option('--list',  default='.',   help='The path of the source file.')
@click.option('--path',  default='.',   help='The path to save the downloads if not provided current path will be used')
def by_chapter_list(name, list, path):
    """Receive an html or txt file and extract a list of links and write it to a text file. It's propose is create a queue for download."""
    for chapter_url in ws.get_chapters_urls(dm.read_file(list)):
        download_chapter(chapter_url, )

    pass


def download_chapter(chapter_url: str, father_path: str, padding: int):
    chapter_nums = re.findall('[\d]+', re.findall('chapter.*\d',chapter_url))
    chapter_name = f'chapter_{chapter_nums[0]:0{padding}}' + '.'.join(chapter_nums[1:])
    chapter_path = dm.create_chapter(chapter_name, father_path)
    dm.move_to(chapter_path)
    click.echo(f'Downloading {chapter_name}')
    chapter_soup = ws.soup_page(chapter_url)
    chapter_images = ws.get_img_urls(chapter_soup)
    ws.download_images(chapter_images)
    dm.move_to(father_path)


if __name__ == '__main__':
    pass
