# -*- coding: utf-8 -*-
"""
Handle app core
"""

from __future__ import division, print_function, absolute_import


from tinydb import TinyDB
from tinydb.storages import MemoryStorage

from utiny.core import Handler


class App(Handler):
    """
    App handler
    """

    def __init__(self):
        self.db = TinyDB(
            'db.json',
            sort_keys=True,
            indent=4,
            separators=(',', ': '),
            default_table='default')

    def list(self):
        """
        list all table
        """

        for table in self.db.tables():
            print(table)

    def new(self, table_name):
        """
        Create new table
        """

        table = self.db.table(table_name)
        print(f'{table_name} created')

    def remove(self, table_name):
        """
        remove selected table
        """

        self.db.purge_table(table_name)
        print(f'{table_name} removed')
