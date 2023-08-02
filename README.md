# manger

![banner](https://user-images.githubusercontent.com/100007797/257945920-1a057ecc-1968-4fe2-a26a-1cffa87733df.png)

manger is a python cli tool to download manga. It just need a **url** of the index from the manga but you can also personalize other options like its title, path to be saved, if you want it to create a copy of each chapter in pdf.

You don't have to worry if the manga doesn't downloading in the frist session, just run the same command again and manger will start where it leaved.

**Note:** the tool work best with sites like this [site](https://ww6.read-onepiece.com/) maybe it can work other kinds of sites but not granted.
## Requirements

- Having installed **Python 3.9** or superior.
- pip

## Installation

**1.** Clone the repository and move into the repository.

```bash
git clone https://github.com/MarioChvx/manger.git
cd manger
```

**2.** Install the module.

```bash
# to install it in your main Python
python3 -m pip install --user .

# to install it in a virtual environment
pip install .
```

## Usage

```bash
manger --help
```

For more detailed usage descriptions

## Pending changes

- complete pending functions
  - manga download
    - add range of chapters option
- better handle error from requests
- async download
