from setuptools import setup, find_packages
import os.path
import sys, os
import json

# HERE = pathlib.Path(__file__).parent


# README = (HERE / "README.md").read_text()


setup(
    name="apptweak",
    version="1.0.2",
    description="access the apptweak-io API in an easier way",
    url="https://github.com/apptweak/apptweak-api-python-library",
    author="apptweak",
    author_email="romain@apptweak.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "",
        ]
    },
    zip_safe=False)
