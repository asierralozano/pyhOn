#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    install_requires = f.read().splitlines()

with open("pyhon/__version__.py", "r", encoding="utf-8") as f:
    _, _, version = f.read().partition("=")
    version = version.strip().strip("'\"")

setup(
    name="pyhOn",
    version=version,
    author="Kuba Sawulski",
    description="Control hOn devices with python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "GitHub": "https://github.com/IoTLabs-pl/pyhOn",
    },
    license="MIT",
    platforms="any",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        "console_scripts": [
            "pyhOn = pyhon.__main__:start",
        ]
    },
)
