# -*- coding: utf-8 -*-

import pytest
from linked_list import Node

TYPE_TABLE = [(0, 0), ('a', 'a'), ([1, 2], [1, 2]), ((1, 2), (1, 2))]

# Node Tests


@pytest.mark.parametrize('init_value, result', TYPE_TABLE)
def test_node_init_value(init_value, result):
    """Test that the values initialize correctly."""
    test_node = Node(init_value)
    assert test_node.value == result


@pytest.mark.parametrize('init_value, result', TYPE_TABLE)
def test_node_init_pointer(init_value, result):
    """Test that the pointer initializes correctly."""
    test_node = Node(init_value)
    assert test_node.pointer is None


@pytest.mark.parametrize('init_value, result', TYPE_TABLE)
def test_node_pointer(init_value, result):
    """Test that the node pointer returns the correct node."""
    test_node = Node(init_value)
    second_node = Node(init_value, test_node)
    assert second_node.pointer == test_node
