#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.1dev'

with open('README.md') as f:
    readme = f.read()

with open('../LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = 'Sarek',
    version = version,
    description = 'Helper tools for use with the Sarek Nextflow pipeline.',
    long_description = readme,
    keywords = ['sarek', 'cancer', 'nextflow', 'bioinformatics', 'workflow', 'pipeline', 'biology', 'sequencing', 'NGS', 'next generation sequencing'],
    author = 'Maxime Garcia, Szilvester Juhos, Phil Ewels',
    author_email = 'maxime.garcia@scilifelab.se, phil.ewels@scilifelab.se',
    url = 'https://github.com/SciLifeLab/Sarek',
    license = license,
    scripts = ['scripts/sarek'],
    install_requires = required,
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False
)
