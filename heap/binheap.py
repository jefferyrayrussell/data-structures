# -*- coding: utf-8 -*-
"""Create a binary heap."""
from __future__ import unicode_literals

class BinNode(object):
    """Create a Node constructor to store data in a binary heap."""

    def __init__(self, value, parent=None, child_a=None, child_b=None):
        """Create an instance of a Node in a binary heap."""
        self.value = value
        self.parent = parent
        self.child_a = child_a
        self.child_b = child_b


class BinHeap(object):
    """Create a Binary Heap constructor."""

    def __init__(self, data_list=None):
        """Create an instance of a Binary Heap."""
        self.length = 0
        self.top = None
        self.bin_heap_list = []
        try:
            data_list.sort()
        except TypeError as message:
                raise TypeError('The input is of different types; cannot create a binary heap.' + message)
        except AttributeError as message:
                raise AttributeError('The input is not sortable; cannot create a binary heap.' + message)