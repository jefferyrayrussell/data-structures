# -*- coding: utf-8 -*-
"""Create a doubbly linked list."""
from __future__ import unicode_literals


class DNode(object):
    """Create a node to store data."""

    def __init__(self, value, next_node=None, prev_node=None):
        """Create an instance of a Node."""
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class DList(object):
    """Create a doubly-linked list class to store strings of data."""

    def __init__(self, value_list=None):
        """Create an instance of a doubly-linked list."""
        self.length = 0
        self.head = None
        self.tail = None
        if hasattr(value_list, '__iter__'):
            for value in value_list:
                self.push(value)
        elif value_list:
            self.push(value_list)

    def __len__(self):
        """Return the length of the linked list for the built in len."""
        return self.length

    def push(self, value):
        """Add a new node to the head of the linked list."""
        new_node = DNode(value, self.head)
        if self.head:
            self.head.prev_node = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def append(self, value):
        """Add a new node to the tail of the linked list."""
        new_node = DNode(value, prev_node=self.head)
        if self.tail:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def size(self):
        """Return the length of the linked list."""
        return len(self)

    def pop(self):
        """Remove the first value off the head of the list and return it."""
        if self.length:
            pop_node = self.head
            self.length -= 1
            self.head.prev_node = None
            self.head = pop_node.next_node
            return pop_node.value

    def shift(self):
        """Remove the first value off the head of the list and return it."""
        if self.length:
            shift_node = self.tail
            self.length -= 1
            self.tail.next_node = None
            self.tail = shift_node.prev_node
            return shift_node.value

    def display(self):
        """Return a unicode string representing the list."""
        if self.length:
            current_node = self.head
            return_str = '('
            while current_node != self.tail:
                return_str += '{0}{1}'.format(current_node.value, ', ')
                current_node = current_node.next_node
            else:
                return_str += u'{0}{1}'.format(current_node.value, ')')
            return return_str

    def search(self, val):
        """Return the node containing a 'val' in the list."""
        if self.length:
            current_node = self.head
            while current_node.next_node:
                if current_node.value == val:
                    return current_node
                current_node = current_node.next_node
            else:
                if current_node.value == val:
                    return current_node
        raise IndexError('Value not in list.')

    def remove_node(self, remove_node):
        """Remove the given node from the list."""
        if self.head == remove_node:
            self.pop()
            return
        if self.tail == remove_node:
            self.shift()
            return
        remove_node.prev_node.next_node = remove_node.next_node
        remove_node.next_node.prev_node = remove_node.prev_node
        self.length -= 1

    def remove(self, value):
        self.remove_node(self.search(value))
