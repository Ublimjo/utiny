# -*- coding: utf-8 -*-
"""
Main core module
"""

from __future__ import division, print_function, absolute_import


class Handler(object):
    """
    Parent handler
    """

    def invalid(self):
        """
        Executed when invalid command
        """

        print('invalid command')
