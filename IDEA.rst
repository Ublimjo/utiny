Utiny structure
===============

Database is a folder
Table    is a database | metadata in '_index.db' database
Entry    is a table | entry in _entry


The Column
==========

_entry table has normal column from Entry the table but column field is in
``field.py`` with same level as Table the database

``field.py``
------------

.. code-block:: python

  class {table_name}(Field):
      @static
      def type(self):
          return str

      @static
      def default(self):
          return 'you@email.com'
