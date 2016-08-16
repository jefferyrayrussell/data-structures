# -*- coding: utf-8 -*-


class Node(object):
    """ """
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer


class LinkedList(object):
    """ """
    def __init__(self, value_list=None):
        self.length = 0
        self.header = None
        if hasattr(value_list, '__iter__'):
            for value in value_list:
                self.push(value)
        elif value_list:
            self.push(value_list)


    def __len__(self):
        return self.length

    def push(self, value):
        temp_node = self.header
        new_node = Node(value, temp_node)
        self.header = new_node
        self.length += 1

    def size(self):
        return len(self)

    def pop(self):
        pop_node = self.header
        self.header = pop_node.pointer
        self.length -= 1
        return pop_node.value

    def display(self):
        current_node = self.header
        return_str = u'('
        while current_node.pointer:
            return_str += u'{0}{1}'.format(current_node.value, ', ')
            current_node = current_node.pointer
        else:
            return_str += u'{0}{1}'.format(current_node.value, ')')
        return return_str

    def search(self, val):
        current_node = self.header
        while current_node.pointer:
            if current_node.value == val:
                return current_node
            current_node = current_node.pointer
        else:
            if current_node.value == val:
                return current_node


    def remove(self, remove_node):
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
