# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from linked_list import LinkedList


class Queue(object):
    """Create a Queue class."""

    def __init__(self, value_list=None):
        """Create an instance of a queue."""
        if value_list:
            self._linked_list = LinkedList(value_list)
            self.is_empty = False
        else:
            self._linked_list = LinkedList()
            self.is_empty = True
        self.top = self._linked_list.header
        self.size = len(self._linked_list)

    def enqueue(self, value):
        """Add value to the queue."""
        self._linked_list.push(value)
        self.top = self._linked_list.header
        self.size += 1
        self.is_empty = False

    def denqueue(self, value): 
        """Removes the correct item from the queue, and
        returns its value.  Raises an error if the queue is empty."""
        self._linked_list.push(value) self.top = self._linked_list.header
        self.size += 1 self.is_empty = False

    # def pop(self):
    #     """Remove the top of the stack and return it."""
    #     if not self.is_empty:
    #         value = self._linked_list.pop()
    #         self.top = self._linked_list.header
    #         self.size -= 1
    #         if self.size == 0:
    #             self.empty = True
    #         return value

    def peek(self, value): 
        """Returns the next value in the queue without
        dequeueing it.  If the queue is empty, returns none."""
        self._linked_list.push(value) self.top = self._linked_list.header
        self.size += 1 self.is_empty = False

    def size(self, value): 
        """Returns the size of the queue, 0  if  empty."""
        self._linked_list.push(value) self.top = self._linked_list.header
        self.size += 1 self.is_empty = False
