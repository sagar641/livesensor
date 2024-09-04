from setuptools import find_packages,setup
from typing import List

setup (
    name='Sensor',
    version="0.0.1",
    author="Sagar",
    author_email="sbjadhav641@gmail.com",
    packages=find_packages(),
    install_requres=["pymongo"]
)