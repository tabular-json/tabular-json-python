from setuptools import find_packages, setup
from codecs import open
from os import path

# Get the long description from the README file
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read().replace("\r", "")

setup(
    name="tabularjson",
    version="1.0.2",
    packages=find_packages(include=["tabularjson"]),
    description="Tabular-JSON: A superset of JSON adding CSV-like tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://tabular-json.org/",
    author="Jos de Jong",
    author_email="wjosdejong@gmail.com",
    license="ISC",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=[],
)
