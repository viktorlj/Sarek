#!/usr/bin/env python
""" Main Sarek module file.

Shouldn't do much, as everything is under subcommands.
"""

import pkg_resources

__version__ = pkg_resources.get_distribution("sarek").version
