# -*- coding: utf-8 -*-
"""Create a binary heap."""
from __future__ import unicode_literals

class BinNode(object):
    """Create a Node constructor to store data in a binary heap."""

    def __init__(self, value, parent=None):
        """Create an instance of a Node in a binary heap."""
        self.value = value
        self.parent = parent
        self.child_a = None
        self.child_b = None

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value


class BinHeap(object):
    """Create a Binary Heap constructor."""

    def __init__(self, data_list=None):
        """Create an instance of a Binary Heap."""
        self.top = None
        self.bin_heap_list = []
        if data_list:
            try:
                data_list.sort()
            except TypeError as message:
                    raise TypeError('The input is of different types; cannot create a binary heap.' + message)
            except AttributeError as message:
                    raise AttributeError('The input is not sortable; cannot create a binary heap.' + message)

            data_list.reverse()
            for idx, item in enumerate(data_list):
                self.set_node_in_heap(item, idx)
            self._size = idx + 1
        else:
            self._size = 0

    def push(self, value):
        current_node = self.set_node_in_heap(value, self._size)
        try:
            while current_node > current_node.parent:
                current_node.value, current_node.parent.value = current_node.parent.value, current_node.value
                current_node = current_node.parent
        except AttributeError:
            pass
        self._size += 1

    def set_node_in_heap(self, value, idx):
        if idx == 0:
            new_node = BinNode(value)
            self.bin_heap_list.append(new_node)
            self.top = new_node
        else:
            parent_position = ((idx + 1) // 2) - 1
            is_child_a = bool(idx % 2)
            new_node = BinNode(value, self.bin_heap_list[parent_position])
            if (is_child_a):
                new_node.parent.child_a = new_node
            else:
                new_node.parent.child_b = new_node
            self.bin_heap_list.append(new_node)

        return new_node
