"""
Module that is responsible for setting up the environment
"""
import os

import setuptools

# get the current path
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

# parse the readme into a variable
with open("README.md", "r", encoding="utf8") as rmd:
    long_desc = rmd.read()

# fetch the requirements required
with open(os.path.join(CURRENT_PATH, "requirements.txt"), "r", encoding="utf8") as req_file:
    requirements = req_file.read().split("\n")

# now create the setup tools script
setuptools.setup(
    name="covid19-sounds-npjdm",
    version="0.0.1",
    author="Andreas A. Grammenos",
    author_email="ag926@cl.cam.ac.uk",
    description="COVID-19 Sounds npj Digital Medicine Supplementary Material",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/cam-mobsys/covid19-sounds-npjDM",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="==3.6",
    install_requires=requirements,
    platforms="any",
)
