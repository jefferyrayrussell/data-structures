# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from linked_list import LinkedList


class Stack(object):
    """Create a Stack class."""

    def __init__(self, value_list=None):
        """Create an instance of a stack."""
        if value_list:
            self._linked_list = LinkedList(value_list)
            self.is_empty = False
        else:
            self._linked_list = LinkedList()
            self.is_empty = True
        self.top = self._linked_list.header
        self.size = len(self._linked_list)

    def push(self, value):
        """Add a new layer to the head of the stack."""
        self._linked_list.push(value)
        self.top = self._linked_list.header
        self.size += 1
        self.is_empty = False

    def pop(self):
        """Remove the top of the stack and return it."""
        if not self.is_empty:
            value = self._linked_list.pop()
            self.top = self._linked_list.header
            self.size -= 1
            if self.size == 0:
                self.empty = True
            return value
