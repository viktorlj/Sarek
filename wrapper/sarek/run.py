#!/usr/bin/env python
""" Tools to launch the Sarek pipeline.

Builds Nextflow command according to user input
and chains multiple nextflow commands together
"""

import logging
import subprocess
import sys

class Sarek(object):
    """ Object to hold Sarek pipeline info """

    def __init__(self, tsv_path):
        self.config = {
            tsv: tsv_path
            mappedfiles: None
        }

    def map(self):
        print(self.config.tsv)
        self.config.tsv = 'something new'
        success = subprocess.check(['nextflow', 'run', 'SciLifeLab/Sarek/main.nf', '--tools'])
        if success:
            self.config.mappedfiles = 'some path'

    def annotate(self):
        print(self.config.tsv)
        if self.config.mappedfiles is None:
            logging.critical("Annotation needs mapped files")
            sys.exit(1)
