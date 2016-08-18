# data-structures

Classic Data Structure Assignments

__Linked List__

__authors:__ Zach Rickert and Jeffery Russell

__date:__ 8/17/2016

These modules are recreations of classic data structures.


###LinkedList###

A Singly-Linked List in Python.

__Attributes__:
Length - Returns the length of the list.

__Methods__:

* push - Puts a new value at the head of the list.
* size - Returns the length of the list.
* pop - Pops off the first value of the list and returns the value.
* search('val') - Returns the first node that contains the 'val' in the list.
* remove ('node') - Removes a given node from the list.
* display - Return a unicode string representative of the list.


###Stack###

A Stack List in Python.

__Attributes__:

* size - Returns the size of the stack.
* is_empty - Returns True is it is an empty stack, False otherwise.
* top - returns the top node of the stack.


__Methods__:

* push - Puts a new value at the head of the list.
* pop - Pops off the first value of the list and returns the value.


###Doubly-Linked List###

A Doubly-Linked List in Python.

A doubly linked list would be useful for traversing back and forth through
the pages of blog posts or the images of a slider.  A singly linked list 
would be useful for a web crawler as it caches links and connects to the 
next link from that link.

__Methods__:

* push(val) - Insert the value 'val' at the tail of the list.
* append(val) - Append the value 'val' at the tail of the list.
* pop() - Pop the first value off the list and replace it.
* shift() - Remove the the last value from the tail of the list and return it.
* remove(val) - Remove the first instance of 'val' found in the list, starting 
from the head.  If 'val' is not present, it will raise an approtpriate Python exception.


###Queue###

A Queue in Python.

__Methods__:

* enqueue(value) - Adds value to the queue.
* dequeue() - removes the correct item from the queue and returns its value;
    should raise an error if the queue is empty.
* peek() - returns the next value in the queue without dequeueing it; returns
    none if the queue is empty. 
* size - Returns the size of the queue; returns 0 if empty.
