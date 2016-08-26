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
        """Magic method for greater than."""
        return self.value > other.value

    def __lt__(self, other):
        """Magic method for less than."""
        return self.value < other.value


class BinHeap(object):
    """Create a Binary Heap constructor."""

    def __init__(self, data_list=None):
        """Create an instance of a Binary Heap in max mode."""
        self.top = None
        self.bin_heap_list = []
        if data_list:
            try:
                data_list.sort()
            except TypeError as message:
                    raise TypeError('The input is of different types; cannot create a binary heap.' + message)
            except AttributeError as message:
                    raise AttributeError('The input is not sortable; cannot create a binary heap.' + str(message))

            data_list.reverse()
            for idx, item in enumerate(data_list):
                self.set_node_in_heap(item, idx)
            self._size = idx + 1
        else:
            self._size = 0

    def push(self, value):
        """Push a value onto the heap."""
        current_node = self.set_node_in_heap(value, self._size)
        try:
            while current_node > current_node.parent:
                current_node.value, current_node.parent.value = current_node.parent.value, current_node.value
                current_node = current_node.parent
        except AttributeError:
            pass
        self._size += 1

    def set_node_in_heap(self, value, idx):
        """Set node in the heap."""
        if idx == 0:
            new_node = BinNode(value)
            self.bin_heap_list.append(new_node)
            self.top = new_node
        else:
            parent_position = ((idx + 1) // 2) - 1
            is_child_a = idx % 2
            new_node = BinNode(value, self.bin_heap_list[parent_position])
            if (is_child_a):
                new_node.parent.child_a = new_node
            else:
                new_node.parent.child_b = new_node
            self.bin_heap_list.append(new_node)

        return new_node

    def pop(self):
        """Pop a node off of the heap."""
        try:
            last_node = self.bin_heap_list[-1]
        except IndexError:
            raise IndexError('You cannot pop an empty heap.')
        if self._size == 1:
            self.top = None
            return self.bin_heap_list.pop().value

        last_node.value, self.top.value = self.top.value, last_node.value
        is_child_b = self._size % 2
        if (is_child_b):
            self.bin_heap_list[-1].parent.child_b = None
        else:
            self.bin_heap_list[-1].parent.child_a = None
        self._size -= 1
        return_value = self.bin_heap_list.pop().value
        current_node = self.top
        while True:
            try:
                child_a = current_node.child_a.value
            except AttributeError:
                break
            try:
                child_b = current_node.child_b.value
            except AttributeError:
                child_b = child_a

            if child_a >= child_b:
                if current_node.child_a > current_node:
                    current_node.value, current_node.child_a.value = current_node.child_a.value, current_node.value
                    current_node = current_node.child_a
                else:
                    break
            else:
                if current_node.child_b > current_node:
                    current_node.value, current_node.child_b.value = current_node.child_b.value, current_node.value
                    current_node = current_node.child_b
                else:
                    break

        return return_value
