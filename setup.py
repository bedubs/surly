# coding=utf-8
from setuptools import setup, find_packages
from codecs import open
import os


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()


setup(
    name="surly",
    version="0.2.0",
    packages=find_packages(),

    zip_safe=True,

    author="William Williamson",
    author_email="william.williamson-2@selu.edu",
    description="Single user relational database", install_requires=['pandas']
)
