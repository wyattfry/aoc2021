"""Python setup.py for aoc2021 package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("aoc2021", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="aoc2021",
    version=read("aoc2021", "VERSION"),
    description="Awesome aoc2021 created by wyattfry",
    url="https://github.com/wyattfry/aoc2021/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="wyattfry",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["aoc2021 = aoc2021.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
