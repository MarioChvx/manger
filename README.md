# A cli tool for manga downloading

A python cli for manga downloading. With a given **url** of a list of chapters the tool will create a directory with the given **title** provided in the **path** selected and each chapter will be saved as a subdirectory with the images named by his order.

If the command is run again with the same parameters, it will only download the missing chapters.

**Note:** the tool work best with sites like this [site](https://ww6.read-onepiece.com/) maybe it can work other kinds of sites but not granted.

## Pending changes

- complete pendign functions
  - add range of chpaters to `manga` command
- assync download

## Requirements

- Having installed **Python 3.9** or superior.
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

For users of unix based operative systems

```bash
python3 -m pip install --user --editable .
```

For Windows users

```bash
py -m pip install --user --editable .
```

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

