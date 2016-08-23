# -*- coding: utf-8 -*-
"""Create a binary heap."""
from __future__ import unicode_literals

class BinNode(object):
    """Create a Node constructor to store data in a binary heap."""

    def __init__(self, value, parent_node=None, child_a_node=None, child_b_node=None):
        """Create an instance of a Node in a binary heap."""
        self.value = value
        self.parent_node = parent_node
        self.child_a_node = child_a_node
        self.child_b_node = child_b_node

class BinHeap(object):
    """Create a Binary Heap constructor."""

    def __init__(self, data_list=None)
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