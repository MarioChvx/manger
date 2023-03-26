
import click
import manger_logic as ml

@click.group(invoke_without_command= True)
@click.pass_context
def manger(ctx):
    """
    manger contains different useful commands to download manga and save it as pdf.
    To know more about each command run "manger COMMAND --help".
    CAUTION! is probable that manger will not work correctly or not work at all 
    with every single site, it could download images that doesn't belong to the
    manga or some times will not be able to access certain pages.
    """
    if ctx.invoked_subcommand is None:
        click.echo('No command selected. Pease run "manger --help" to know more about manger')
    # else:
        # click.echo(f"I am about to invoke {ctx.invoked_subcommand}")

@manger.command()
@click.argument('url')
@click.option(
    '-t',
    '--title',
    help = 'The title of the manga, is going to be used to name files, if is not provided the app will infer it from the homepage.'
)
@click.option(
    '-p',
    '--path',
    default='.',
    help='The path to save the downloads, if is not provided current path will be used'
)
@click.option(
    '--pdf',
    is_flag= True,
    help= 'If it is enabled a copy of each chapter in pdf format will be saved'
)
def manga(url: str, title: str, path: str, pdf: bool):
    """
    Will download all chapters from a specific type of page.
    It receives an url of the page, the following are examples
    of pages which manger works: \n
      - https://w16.read-onepiece.com/ \n
      - https://manga-baki.com/ \n
      - https://dorohedoro.online/ \n
      - https://record-ofragnarok.com/ \n
    """

    ml.download_manga(url, title, path, pdf)

@manger.command()
@click.argument('url')
@click.option(
    '-t',
    '--title',
    help= 'The title of the manga, is going to be used to name files, if is not provided the app will infer it from the homepage.'
)
@click.option(
    '-p',
    '--path',
    default='.',
    help='The path to save the downloads, if is not provided current path will be used'
)
@click.option(
    '--pdf',
    is_flag= True,
    help= 'If it is enabled a copy of each chapter in pdf format will be saved'
)
def chapter(url: str, title: str, path: str, pdf: bool):
    """
    Will download a single chapter from the url passed as argument.
    """
    pass

@manger.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option(
    '--multiple/--single',
    default= True,
    help= 'Default is "--multiple" that will convert all the subdirectories to pdf, "--single" will only convert the directory specified'
)
@click.option(
    '-d',
    '--destiny',
    default='.',
    help='The path to save the file with the pdf documents, by default saves in the current directory'
)
def pdf(filename, multiple: bool, destiny: str):
    """
    Use it to convert files with images inside to pdf documents.
    """
    pass

if __name__ == '__main__':
    manger()
