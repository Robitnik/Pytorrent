import os.path
import pathlib
import re

from setuptools import setup

PROJECT_NAME = 'pytorrent'
VERSION = '0.0.1-beta'
DESCRIPTION = 'Torrent Client for Python3.12+'
AUTHOR = 'Robitnik'
AUTHOR_EMAIL = ''
URL = 'https://github.com/yourusername/pytorrent'

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license='BSD License',
    packages=[PROJECT_NAME],
    entry_points={
        'console_scripts': ['pytorrent=pytorrent.cli:run_cli']
    },
    install_requires=[
        'libtorrent>=2.0.11',  # Оновлена версія libtorrent
        'asyncclick>=8.1.7.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.11, <3.13',
)
