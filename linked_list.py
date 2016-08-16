# -*- coding: utf-8 -*-


class Node(object):
    """ """
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer


class LinkedList(object):
    """ """
    def __init__(self):
        self.length = 0
        self.header = None

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
        return pop_node.value

    def display(self):
        current_node = self.header
        return_str = '('
        while current_node.pointer:
            return_str += '{0}{1}'.format(current_node.value, ', ')
            current_node = current_node.pointer
        else:
            return_str += '{0}{1}'.format(current_node.value, ')')
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

    #     self.set_init_list(*value)

    # def set_init_list(self, *values):
    #     for value in values:
    #         self.length += 1
