# -*- coding: utf-8 -*-
"""
Start command interaction
"""

from __future__ import division, print_function, absolute_import


class Interactive(object):
    """
    Parent Interactive base command
    """

    def __init__(self):
        self.leftp = []

    def prompter(self):
        """
        high-level of input()
        """

        rawleft = ''.join((_ + ' > ') for _ in self.leftp)
        result = input(' ' + rawleft)
        return result.split(' ')

    def cmd(self, cmd):
        """
        list of cmd
        please follow this rule:
            return {
                'add': lambda: x + y,
                'sub': lambda: x - y,
                'mul': lambda: x * y,
                'div': lambda: x / y,
            }.get(operator, lambda: None)()
        """
        raise NotImplementedError('Please implemente list of command')

    def run(self):
        """
        run command loop
        """

        while True:
            self.cmd(*self.prompter())
