# data-structures

Classic Data Structure Assignments

__authors:__ Zach Rickert and Jeffery Russell

__date:__ 8/17/2016

These modules are recreations of classic data structures.


###LinkedList###

A Singly-Linked List in Python.

A Linked List consists of Nodes, each of which contains some data and a
pointer to the next node.  It is self referential (naturally recusive).
Linked Lists are great for holding data, though you do not always know
its size in advance.  They store items linearly and allow quick inserts
and easy removal operations. They can be used for a web crawler cacheing
links and the next link from that link.

__Methods__:

* push(val): inserts a new value at the head of the list.
* size(): returns the length of the list.
* pop(): pops off the first value of the list and returns it.
* search(val): returns the first node that contains the 'val' in the list.
    If not present, returns None.
* remove(node): removes the given node from the list, wherever it might
    be.  The node must be an item in the list.
* display(): returns a unicode string representative of the list as if it
    were a Python tuple literal.


###Stack###

A Stack in Python.

A Stack is a data structure where elements are inserted into and removed
from the head of a container.  It's characteristics are: sequential,
limited access, last-in first-out access, and linear.  A stack is useful 
for a Towers of Hanoi puzzle, rearranging railroad cars, and sorting
anything.

__Methods__:
* push(val): adds a new value to the top of the stack.
* pop(): pops off the top value of the stack and returns the value. If the
    stack is empty, a pop should raise an appropriate exception.


###Doubly-Linked List###

A Doubly-Linked List consists of Nodes, each of which contains some data
and pointers to the next and previous nodes.  It is self-referential, ie.
naturally recursive. A Doubly-Linked List would be useful for traversing back and forth through
the pages of blog posts or the images of a slider.  

__Methods__:
* push(val) - Insert the value 'val' at the tail of the list.
* append(val) - Append the value 'val' at the tail of the list.
* pop() - Pop the first value off the list and replace it.
* shift() - Remove the the last value from the tail of the list and 
    return it.
* remove(val) - Remove the first instance of 'val' found in the list, 
    starting from the head.  If 'val' is not present, it will raise an 
    approtpriate Python exception.


###Queue###

A Queue in Python.

A Queue is a data structure that inserts elements at the tail (enqueue) and 
accesses/removes (dequeue) elements at the head. A queue could be useful
for building a task manager, modeling traffic patterns, and printing
documents in the proper order.

__Methods__:
* enqueue(value): adds value to the queue at the back.
* dequeue(): removes the correct item from the front of the queue and 
    returns its value;should raise an error if the queue is empty.
* peek(): returns the next value in the queue without dequeueing it; returns
    none if the queue is empty. 
* size(): returns the size of the queue; returns 0 if empty.


###DeQue###

A DeQue in Python.

A DeQue is a data structure like the Queue but works at both ends.  Data
can be inserted at the head or tail, and retrieved from the head or tail.
A DeQue could be useful for: running the minimum and maximum run times for
code being tested; modeling how passengers board and deboard a plane with
two entrances/exits.  

__Methods__:
* append(val): adds value to the end of the deque.
* appendleft(val): adds a value to the front of the deque.
* pop(): removes a value from the end of the deque and returns it; raises
    an exception if the deque is empty.
* popleft(): removes a value from the front of the deque and returns it;
    raises an exception if the deque is empty.
* peek(): returns the next value that would be returned by popleft, but
    leaves leaves the value in the deque; returns None if the queue is empty. 
* peekleft(): returns the next value that would be returned by popleft but
    leaves the value in the deque; returns None if the deque is empty.
* size():  returns the count of items in the deque; returns 0 if empty.
