from setuptools import find_packages ,setup
from typing import List





setup(
    name = 'sensor',
    version="0.0.1",
    author="prince",
    author_email="saad.fastnu@gmail.com",
    packages=find_packages(),
    install_requires = ["pymongo"]

)