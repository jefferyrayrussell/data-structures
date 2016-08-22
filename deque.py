# -*- coding: utf-8 -*-
"""Deque data structure."""
from __future__ import unicode_literals

# Use the doubly-linked list as the parent for the class."""
from double import DList


class DeQue(object):
    """Create a Deque class."""

    def __init__(self, value_list=None):
        """Create an instance of a Deque using DList."""
        self._dlist = DList(value_list)

    def append(self, value):
        """Add value to the end of the deque."""
        self._dlist.append(value)

    def appendleft(self, value):
        """Add value to the front of the deque."""
        self._dlist.push(value)

    def pop(self):
        """From the end of the deque, remove and return value."""
        return self._dlist.shift()

    def popleft(self):
        """From the front of the deque, remove and return value."""
        return self._dlist.pop()

    def peek(self):
        """Return the next value without popping it from tail."""
        try:
            return self._dlist.tail.value
        except AttributeError:
            return None

    def peekleft(self):
        """Return the next value without popping it from head."""
        try:
            return self._dlist.head.value
        except AttributeError:
            return None

    def size(self):
        """Return the size of the deque, 0 if empty."""
        return self._dlist.size()
