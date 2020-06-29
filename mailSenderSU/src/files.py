"""
The ``files`` module manages files.
The ``File`` class can edit a file.

.. moduleauthor:: Quentin Deschamps <quentindeschamps18@gmail.com>

"""
import os


class File:
    """Manage a file."""
    def create(self):
        """Create an empty file."""
        with open(self.filename, 'w'):
            pass

    def __init__(self, filename):
        """Init a file."""
        self._filename = filename
        if not os.path.exists(filename):
            self.create()

    @property
    def filename(self):
        """Get filename."""
        return self._filename

    def read(self):
        """Read a file."""
        f = open(self.filename, 'r')
        ret = f.read()
        f.close()
        return ret

    def get_list(self):
        """Return the list from a file."""
        f = open(self.filename, 'r')
        lines = f.readlines()
        f.close()
        return [i.strip() for i in lines]

    def add(self, data):
        """Add data to a file."""
        f = open(self.filename, 'a')
        f.write(f'{data}\n')
        f.close()

    def clear(self):
        """Delete all data from a file."""
        f = open(self.filename, 'r+')
        f.truncate(0)
        f.close()
