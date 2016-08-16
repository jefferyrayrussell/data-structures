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


    #     self.set_init_list(*value)

    # def set_init_list(self, *values):
    #     for value in values:
    #         self.length += 1
