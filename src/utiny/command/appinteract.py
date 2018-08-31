# -*- coding: utf-8 -*-
"""
First app entry interaction
"""

from __future__ import division, print_function, absolute_import

from utiny.command import Interactive
from utiny.core.apphandle import App


class AppInteraction(Interactive):
    """
    Interaction of utiny app
    """

    def __init__(self):
        super().__init__()
        self.leftp.append('utiny')
        self.handled = App()


    def cmd(self, cmd, *args):
        """
        List of cmd
        """

        return {
            'list': self.handled.list,
            'new': self.handled.new,
            'remove': self.handled.remove,
        }.get(cmd, self.handled.invalid)(*args)
