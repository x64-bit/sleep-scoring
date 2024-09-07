#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

__version__ = "0.0.4"
NAME = 'sleep_scoring'
AUTHOR = "Visbrain developers"
MAINTAINER = "Anjo Pagdanganan"
EMAIL = 'anjopag31@berkeley.edu'
KEYWORDS = "brain MNI GPU visualization data OpenGL vispy neuroscience " + \
           "sleep data-mining"
DESCRIPTION = "Standalone version of Sleep module from Visbrain suite."
DOWNLOAD_URL = "https://github.com/x64-bit/sleep-scoring"
# Data path :
HERE = os.path.abspath(os.path.dirname(__file__))
PACKAGE_DATA = {}


def read(fname):
    """Read README and LICENSE."""
    return open(os.path.join(HERE, fname), 'rb').read().decode('utf8')


setup(
    # DESCRIPTION
    name=NAME,
    version=__version__,
    description=DESCRIPTION,
    long_description=read('README.rst'),
    keywords=KEYWORDS,
    license=read('LICENSE'),
    author=AUTHOR,
    maintainer=MAINTAINER,
    author_email=EMAIL,
    download_url=DOWNLOAD_URL,
    # PACKAGE / DATA
    packages=find_packages(),
    package_dir={'visbrain': 'visbrain'},
    package_data=PACKAGE_DATA,
    include_package_data=True,
    platforms='any',
    setup_requires=['numpy'],
    install_requires=[
        "numpy>=1.13",
        "scipy",
        "vispy>=0.5.2",
        "matplotlib>=1.5.5",
        "pyqt5",
        "pillow",
        "PyOpenGL"
    ],
    extras_require={
        'full': ["mne", "tensorpac", "pandas", "xlrd", "scikit-image",
                 "nibabel"],
        'sleep': ["mne", "tensorpac"],
        'roi': ["pandas", "xlrd"],
        'topo': ["scikit-image"]
    },
    dependency_links=[],
    classifiers=["Development Status :: 3 - Alpha",
                 'Intended Audience :: Science/Research',
                 'Intended Audience :: Education',
                 'Intended Audience :: Developers',
                 'Topic :: Scientific/Engineering :: Visualization',
                #  "Programming Language :: Python :: 3.5",
                #  "Programming Language :: Python :: 3.6",
                #  "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.9",
                 "Programming Language :: Python :: 3.10",
                 "Programming Language :: Python :: 3.11",
                 "Programming Language :: Python :: 3.12",
                 "Operating System :: MacOS",
                #  "Operating System :: POSIX :: Linux",
                 "Operating System :: Microsoft :: Windows",
                 "Natural Language :: English"
                 ])
