# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from linked_list import LinkedList

# Use the doubly-linked list as the parent just as we used the singly-linked list as the parent for the stack.
from  double import DList


class Queue(object):
    """Create a Queue class."""

    def __init__(self, value_list=None):
        """Create an instance of a queue using DList."""
       self._dlist = DList(value_list)
            
    def enqueue(self, value):
        """Add value to the top of  the queue."""
        return self._dlist.push(value)

    def denqueue(self, value): 
        """From the bottom of the queue, remove and return value."""
         self._dlist.shift(value)
        return  self

    
    # ?????
    def peek(self, value): 
        """Returns the next value in the queue without
        dequeueing it.  If the queue is empty, returns none."""
        
        if self.dlist.size = 0:
            return None
        else:
            return self._dlist.next_node.value


    def size(self, value): 
        """Returns the size of the queue, 0  if  empty."""
        return self._dlist.__len__()