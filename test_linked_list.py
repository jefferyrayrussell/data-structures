# -*- coding: utf-8 -*-

import pytest
from linked_list import Node


def test_node_init_value():
    test_node = Node(5)
    assert test_node.value == 5

def test_node_init_pointer():
    test_node = Node(5)
    assert test_node.pointer is None



