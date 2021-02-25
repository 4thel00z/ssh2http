# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except IOError:
    long_description = ""

try:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = fh.read().strip()
except IOError:
    requirements = """pwntools==4.3.1
sanic==20.12.2""".strip()

setup(
    name="ssh2http",
    version="0.1.0",
    description="Simple utility to tunnel ssh over http",
    license="GPL",
    url="https://github.com/4thel00z/ssh2http",
    author="4thel00z",
    author_email="4thel00z@gmail.com",
    packages=find_packages(),
    install_requires=requirements.split("\n"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
)