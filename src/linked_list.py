# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value, pointer=None):
        """Create an instance of a Node."""
        self.value = value
        self.pointer = pointer


class LinkedList(object):
    def __init__(self, value_list=None):
        """Create an instance of a singly-linked list."""
        self.length = 0
        self.header = None
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
        temp_node = self.header
        new_node = Node(value, temp_node)
        self.header = new_node
        self.length += 1

    def size(self):
        """Return the length of the linked list."""
        return len(self)

    def pop(self):
        """Remove the first value off the head of the list and return it."""
        if self.length:
            pop_node = self.header
            self.header = pop_node.pointer
            self.length -= 1
            return pop_node.value

    def display(self):
        """Return a unicode string representing the list."""
        if self.length:
            current_node = self.header
            return_str = u'('
            while current_node.pointer:
                my_value = current_node.value
                # try:
                #     my_value = current_node.value.decode('utf-8')
                # except AttributeError:
                #     pass
                return_str += u'{0}{1}'.format(my_value, ', ')
                current_node = current_node.pointer
            else:
                my_value = current_node.value
                # try:
                #     my_value = current_node.value.decode('utf-8')
                # except AttributeError:
                #     pass
                return_str += u'{0}{1}'.format(my_value, ')')
            return return_str

    def search(self, val):
        """Return the node containing a 'val' in the list."""
        if self.length:
            current_node = self.header
            while current_node.pointer:
                if current_node.value == val:
                    return current_node
                current_node = current_node.pointer
            else:
                if current_node.value == val:
                    return current_node

    def remove(self, remove_node):
        """Remove the given node from the list."""
        if self.header == remove_node:
            self.header = remove_node.pointer
            self.length -= 1
            return
        current_node = self.header
        while current_node.pointer:
            if current_node.pointer == remove_node:
                current_node.pointer = current_node.pointer.pointer
                self.length -= 1
                return
            current_node = current_node.pointer
