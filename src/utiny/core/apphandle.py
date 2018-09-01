# -*- coding: utf-8 -*-
"""
Handle app core
"""

from __future__ import division, print_function, absolute_import


import os
from tinydb import TinyDB
# from tinydb.storages import MemoryStorage

from utiny.core import Handler
from utiny.utils import path


class App(Handler):
    """
    App handler
    """

    def __init__(self):
        self.database = path.DIR
        self.table = list(self.database.iterdir())

    def list(self):
        """
        list all table
        """

        for table in self.table:
            # ../database/the_table.foo.json -> the_table.foo
            print(str(table.resolve()).split(table.suffix)[0].split('/')[-1])

    def new(self, table_name=None):
        """
        Create new table
        """

        if not table_name:
            table_name = input(' table name: ')

        self.table.append(TinyDB(
            self.database / f'{table_name}.json',
            sort_keys=True,
            indent=4,
            separators=(',', ': '),
            default_table='_entry'))

        print(f'{table_name} created')

    def remove(self, table_name):
        """
        remove selected table
        """

        to_remove = self.database / f'{table_name}.json'
        if to_remove.exists():
            os.remove(to_remove)
            print(f'{table_name} removed')
        else:
            print(f'{table_name} does not exist')
