"""
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from tiddlywebwiki import __version__ as VERSION

setup(name = 'tiddlywebwiki',
        version = VERSION,
        description = 'A plugin for TiddlyWeb that provides a multiuser TiddlyWiki environment.',
        author = 'Chris Dent',
        author_email = 'cdent@peermore.com',
        packages = ['tiddlywebwiki'],
        platforms = 'Posix; MacOS X; Windows',
        install_requires = ['tiddlyweb', 'BeautifulSoup'], # + wikklytextrender
        include_package_data = True,
        )




