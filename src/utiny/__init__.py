# -*- coding: utf-8 -*-
"""
User_friendly database for everyone
"""

from pkg_resources import get_distribution, DistributionNotFound

try:
    DIST_NAME = __name__
    __version__ = get_distribution(DIST_NAME).version
except DistributionNotFound:
    __version__ = 'unknown'
