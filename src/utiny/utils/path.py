# -*- coding: utf-8 -*-
"""
All path used by utiny
"""

from __future__ import division, print_function, absolute_import

import os
from pathlib import Path
from icecream import ic


HOME = Path('~/').expanduser()
DIR = HOME / '.utiny/'

if not DIR.exists():
    os.mkdir(DIR)
