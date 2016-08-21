# -*- coding: utf-8 -*-
"""Queue data structure."""
from __future__ import unicode_literals

# Use the doubly-linked list as the parent just as we used the singly-linked list as the parent for the stack.
from double import DList


class Queue(object):
    """Create a Queue class."""

    def __init__(self, value_list=None):
        """Create an instance of a queue using DList."""
        self._dlist = DList(value_list)

    def enqueue(self, value):
        """Add value to the top of  the queue."""
        return self._dlist.push(value)

    def dequeue(self):
        """From the bottom of the queue, remove and return value."""
        return self._dlist.shift()

    def peek(self):
        """Return the next value in the queue without dequeueing it.  If the queue is empty, returns none."""
        try:
            return self._dlist.tail.value
        except AttributeError:
            return None

    def size(self):
        """Return the size of the queue, 0  if  empty."""
        return self._dlist.__len__()
