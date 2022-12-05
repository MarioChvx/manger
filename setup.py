from setuptools import setup

setup(
    name='manga_download',
    version='0.1.0',
    py_modules=['manga_download'],
    install_requires=[
        'Click',
        'BS4',
        'Requests'
    ],
    entry_points={
        'console_scripts': [
            'manga_download = manga_download:manga_download',
        ],
    },
)