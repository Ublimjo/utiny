# -*- coding: utf-8 -*-
"""
Module entry point of console script
"""

from __future__ import division, print_function, absolute_import

from utiny.command.appinteract import AppInteraction


def main():
    """
    Function entry point of console script
    """

    greet()
    session = AppInteraction()
    session.run()


def greet():
    """
    First greetings
    """

    print('utiny - user-friendly database')
    print('------------------------------')
