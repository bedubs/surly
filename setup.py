# coding=utf-8
from setuptools import setup, find_packages
from codecs import open
import os


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()


setup(
    name="surly",
    version="1.0.0",
    py_modules=['command'],
    install_requires=[
        'Click',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'surly-cli=surly.commands:cli',
            'READ=surly.commands:read',
            'RELATION=surly.commands:relation',
            'INSERT=surly.commands:insert',
            'SELECT=surly.commands:select',
            'PROJECT=surly.commands:project',
            'JOIN=surly.commands:join',
            'PRINT=surly.commands:print',
            'DELETE=surly.commands:delete',
            'DESTROY=surly.commands:destroy',
            'QUIT=surly.commands:quit',
        ],
    },

    #
    # 'surly-cli=surly.commands:cli',
    # 'relation=surly.commands:relation_command',
    # 'insert=surly.commands:insert_command',
    # 'select=surly.commands:select_command',
    # 'project=surly.commands:project_command',
    # 'join=surly.commands:join_command',
    # 'print=surly.commands:print_command',
    # 'delete=surly.commands:delete_command',
    # 'destroy=surly.commands:destroy_command',
    # 'quit=surly.commands:quit_command',



    packages=find_packages(),

    zip_safe=True,

    author="William Williamson",
    author_email="william.williamson-2@selu.edu",
    description="Single user relational database"
)
