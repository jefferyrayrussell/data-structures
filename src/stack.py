# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from linked_list import LinkedList


class Stack(object):
    """Create a Stack class."""

    def __init__(self, value_list=None):
        """Create an instance of a stack."""
        self._linked_list = LinkedList(value_list)
        self.top = self._linked_list.header

    def push(self, value):
        """Add a new layer to the head of the stack."""
        self._linked_list.push(value)
        self.top = self._linked_list.header

    def pop(self):
        """Remove the top of the stack and return it."""
        return self._linked_list.pop()
        self.top = self._linked_list.header

    def size(self):
        """Return the size of the stack."""
        return self._linked_list.size()
