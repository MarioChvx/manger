import click
import directory_management as dm
import web_scraping as ws
import math

@click.command()
@click.option('--manga-name', prompt='Provide the manga name', help='The title of the manga, is going to be used to name files')
@click.option('--start-url', prompt='Provide the URL form the start chapter', help='The URL where the download is going to start')
@click.option('--chapters', default=1, help='The number of chapters is going to be downloaded')
@click.option('--path', default='.', help='The path to save the downloads if not provided current path will be used')
def manga_download(manga_name, start_url, chapters, path):
    """
    Place holder
    """
    wd = dm.check_path(path)
    father = dm.create_father(manga_name, wd)
    print(f'{father = }')

    chapters_urls = ws.get_chapters_urls(start_url, int(chapters))
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
