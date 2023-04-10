# A cli tool for manga downloading

A python cli for manga downloading. With a given **url** of a list of chapters the tool will create a directory with the given **title** provided in the **path** selected and each chapter will be saved as a subdirectory with the images named by his order.

If the command is run again with the same parameters, it will only download the missing chapters.

**Note:** the tool work best with sites like this [site](https://ww6.read-onepiece.com/) maybe it can work other kinds of sites but not granted.

## Pending changes

- complete pending functions
  - manga download
    - add range of chapters option
  - chapter download
  - convert to pdf
- async download

## Requirements

- Having installed **Python 3.9** or superior.

## Installation

1. Clone the repository.

```bash
git clone https://github.com/MarioChvx/manger.git
```

2.Move into the repository.

```bash
cd manger
```

(if you are going to use it just one time may be you should consider installing it on a venv)

3.Install the module.

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
manger --help
```

For more detailed usage descriptions
