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

        self.set_init_list(*value)

    def set_init_list(self, *values):
        for value in values:
            self.length += 1
