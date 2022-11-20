import click
import re


@click.command()
@click.option('--manga-name', prompt='Provide the manga name', help='The title of the manga, is going to be used to name files')
@click.option('--start-url', prompt='Provide the URL form the start chapter', help='The URL where the download is going to start')
@click.option('--chapters', default=1, prompt='Provide number of chapters', help='The number of chapters is going to be downloaded')
def manga_download(start_url, chapters, manga_name):
    """
    Place holder
    """
    click.echo('Hello')
    start_num = re.search('(?<=\[)(.*?)(?=\])', start_url)

if __name__ == '__main__':
    manga_download()
