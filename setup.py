#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='wavefunction',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',  # List any dependencies your package needs
        'matplotlib',
    ],
    author='Caroline and Jasmine',
    author_email='yhaun223@syr.edu',
    description='Wavefunction of Tritium that satisfies a 2nd order ODE of Schrodinger Eq',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cacapuano/phy_project2/project2',  # Your package's repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
