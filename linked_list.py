# -*- coding: utf-8 -*-


class Node(object):
    """ """
    def __init__(self, value):
        self.value = value
        self.pointer = None


class LinkedList(object):
    """ """
    def __init__(self, value):
        self.length = 0
        self.header = Node(None)

    def push(self, value):
        temp_node = self.header
        new_node = Node(value)
        self.header = new_node
        temp_node.pointer = new_node


    #     self.set_init_list(*value)

    # def set_init_list(self, *values):
    #     for value in values:
    #         self.length += 1
