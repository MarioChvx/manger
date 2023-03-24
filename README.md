# A cli tool for manga downloading

A python cli for manga downloading. With a given **url** of a list of chapters the tool will create a directory with the given **title** provided in the **path** selected and each chapter will be saved as a subdirectory with the images named by his order.

If the command is run again with the same parameters, it will only download the missing chapters.

**Note:** the tool work best with sites like this [site](https://ww6.read-onepiece.com/) maybe it can work other kinds of sites but not granted.

## Pending changes

- remove unused code
- change usage to `manger www.mangaexample.com` and options
- pdf option
- assync download

## Usage

```bash
manger [OPTIONS]
```

### Options

- `--title` *(TEXT)*

The title of the manga, is going to be used to name files, if is not provided the app will ask for it.

- `--url` *(TEXT)*

The URL where the list of available chapters is displayed, ifis not provided the app will ask for it.

- `--path` *(TEXT)*

The path to save the downloads if is not provided current path will be used

- `--help`

Show a help message and exit.

### Example

An example of his usage with all the parameters filled.

```bash
(venv) [username @ desktop ~]$ manger --title One_Piece --url https://ww6.read-onepiece.com/ --path ~/Pictures/Mangas
https://ww6.read-onepiece.com/ successfully accessed!
Created /mnt/PICS/Pictures/Mangas/One_Piece
https://ww6.read-onepiece.com/manga/one-piece-chapter-1/ successfully accessed!
Downloading...
https://ww6.read-onepiece.com/manga/one-piece-chapter-2/ successfully accessed!
Downloading...
https://ww6.read-onepiece.com/manga/one-piece-chapter-3/ successfully accessed!
Downloading...
https://ww6.read-onepiece.com/manga/one-piece-chapter-4/ successfully accessed!
Downloading...
^C
Aborted!
```

An example of his usage with some of the parameters not filled.

```bash
(venv) [username @ desktop ~]$ manger --path ~/Pictures/Mangas
Provide the title of the manga: One_Piece
Provide the home direction form the manga site: https://ww6.read-onepiece.com                           
https://ww6.read-onepiece.com successfully accessed!
https://ww6.read-onepiece.com/manga/one-piece-chapter-4/ successfully accessed!
Downloading...
https://ww6.read-onepiece.com/manga/one-piece-chapter-5/ successfully accessed!
Downloading...
^C
Aborted!
```

As you can see the tool asks for the missing parameter and if you give the same parameters the tool will start where it left the last time.

## Installation

1. Clone the repository.

```bash
git clone https://github.com/MarioChvx/manger.git
```

2. Move into the repository.

```bash
cd manger
```

(if you are going to use it just one time may be you should consider installing it on a venv)

3. Install the module.

```bash
pip install --editable .
```
