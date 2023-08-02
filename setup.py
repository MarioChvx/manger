from setuptools import setup

def gen_requirements():
    with open('./requirements.txt', 'r') as file:
        requirements = [line.strip() for line in file if line.strip()]
    return requirements

setup(
    name='manger',
    version='0.1.0',
    author='Mario Chavez',
    description='manger is a cli tool for manga downloading',
    py_modules=[
        'manger',
        'manger_logic',
        'directory_management',
        'dir_to_pdf',
        'web_scraping'
    ],
    install_requires=gen_requirements(),
    entry_points={
        'console_scripts': [
            'manger = manger:manger',
        ],
    },
)