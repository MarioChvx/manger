import click
import directory_management as dm
import web_scraping as ws
import math

@click.command()
@click.option('--name',  prompt='Provide the title of the manga',           help='The title of the manga, is going to be used to name files')
@click.option('--url',   prompt='Provide the URL form the start chapter',   help='The URL where the download is going to start the number of the chapter should be surrounded by []')
@click.option('--num',   default=1,     help='The number of chapters that is going to be downloaded')
@click.option('--path',  default='.',   help='The path to save the downloads if not provided current path will be used')
def manga_download(name, url, num, path):
    """
    Creates a new directory in the specified path with the name and sub-directories where the download images will be stored.
    """
    wd = dm.check_path(path)
    father = dm.create_father(name, wd)

    chapters_urls = ws.get_chapters_urls(url, int(num))
    max_num = chapters_urls[-1][0]
    pad = math.floor(math.log(max_num, 10))

    for chapter_url in chapters_urls:
        chapter_path = dm.create_chapter(chapter_url[0], pad, father)
        dm.move_to(chapter_path)

        click.echo(f'Downloading {chapter_url[0]}...')
        chapter_soup = ws.soup_page(chapter_url[1])
        chapter_images = ws.get_img_urls(chapter_soup)
        ws.download_images(chapter_images)

        dm.move_to(father)

if __name__ == '__main__':
    manga_download()
