# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ================================================================================
#           sermetpekin@gmail.com
#           2022 Kasım
# ================================================================================
from setuptools import setup, find_packages
from pathlib import Path
import sys

""" Parameters for build and cmd file creator """
from setup_config_pub import package_name

root_version = "0.0.16"
project_urls = {
    "Homepage": f"https://github.com/SermetPekin/{package_name}-rep",
    "Documentation": f"https://github.com/SermetPekin/{package_name}-rep",
}
description_ = f"""
Back ups your folder to your preferred local or network destination reading or creating a gitignore file.
"""
# python3 setup.py bdist_wheel --universal

def read_me_file():
    with open("README.md", "r") as file_:
        long_des = file_.read()

    return long_des


setup(
    name=package_name,
    version=root_version,
    description=description_,
    long_description=read_me_file(),
    long_description_content_type="text/markdown",
    project_urls=project_urls,
    # url=f"https://github.com/SermetPekin/{package_name}-rep",
    author="Sermet Pekin",
    author_email="sermet.pekin@gmail.com",
    license="MIT",
    keywords=f"back up , backupp {package_name}-rep",
    setup_requires=[],
    tests_require=["pytest"],
    packages=find_packages(
        exclude=(
            "scratches",
            "tests",
            "logs",
            "docs",
            "env",
            "index.py",

        )
    ),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Topic :: Office/Business :: Financial",
        "Programming Language :: Python :: Implementation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=[
        "rich>=12.5.1",
        "pandas>=0.19.2",
        "openpyxl>=3.0.10",
        "numpy>=1.5.0",
        "gitignore_parser>=0.0.16",
    ],
    exclude_package_data={},
    python_requires=">=3",
    entry_points={"console_scripts": [f"{package_name}={package_name}:console_main",],},
    extras_require={"dev": ["verser"], "docs": [], "testing": [],},
)
# --------------------------------------------------------------------------------------
