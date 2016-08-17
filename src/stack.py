# -*- coding: utf-8 -*-

from linked_list import LinkedList


class Stack(object):
    def __init__(self, value_list=None):
        if value_list:
            self._linked_list = LinkedList(value_list)
        else:
            self._linked_list = LinkedList()
        self.top = self._linked_list.header
        self.size = len(self._linked_list)

    def is_empty(self):
        return not bool(self.size)

    def push(self, value):
        self._linked_list.push(value)
        self.top = self._linked_list.header
        self.size += 1

    def pop(self):
        if not self.is_empty():
            value = self._linked_list.pop()
            self.top = self._linked_list.header
            self.size -= 1
            return value
