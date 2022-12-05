from setuptools import setup

setup(
    name='manger',
    version='0.1.0',
    py_modules=['manger'],
    install_requires=[
        'Click',
        'BS4',
        'Requests'
    ],
    entry_points={
        'console_scripts': [
            'manger = manger:manger',
        ],
    },
)