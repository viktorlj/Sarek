#!/usr/bin/env python
""" Tools to check the Sarek pipeline.

Checks that everything is installed
"""

import logging
import sys

def check(quiet=True):
    print("hello world")
    if not quiet:
        print("THIS IS LOUD")
    if not check_nextflow() or not check_singularity():
        sys.exit(1)


def check_nextflow():
    logging.critical("Nextflow not installed")
    return True

def check_singularity():
    logging.critical("Singularity not installed")
    return True
