# -*- coding: utf-8 -*-

import pytest
from linked_list import Node, LinkedList

TYPE_TABLE = ['1', 
    1, 
    '-'*10000
    ,'āĕĳœ',
    '', 
    b'1234', 
    '12345\t',
    [1, 2, 3],
    (1, 2, 3)
    ]

# Node Tests

@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_node_init_value(init_value):
    """Test that the values initialize correctly."""
    test_node = Node(init_value)
    assert test_node.value == init_value


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_node_init_pointer(init_value):
    """Test that the pointer initializes correctly."""
    test_node = Node(init_value)
    assert test_node.pointer is None


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_node_pointer(init_value):
    """Test that the node pointer returns the correct node."""
    test_node = Node(init_value)
    second_node = Node(init_value, test_node)
    assert second_node.pointer == test_node

# List Test


def test_empty_list_length():
    """Test to see if any empty string has length zero."""
    empty_list = LinkedList()
    assert empty_list.length == 0


def test_empty_list_pointer():
    """Test to see if any empty string has length zero."""
    empty_list = LinkedList()
    assert empty_list.header is None


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_list_push_empty(init_value):
    """Test push on an empty list."""
    test_list = LinkedList()
    test_list.push(init_value)
    assert test_list.header.value == init_value


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_list_push_head_value(init_value):
    """Test push on a non-empty list. Make sure pushing to head."""
    test_list = LinkedList()
    test_list.push('test_string')
    test_list.push(init_value)
    assert test_list.header.value == init_value


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_list_push_pointer(init_value):
    """Test push on a non-empty list. Make sure that pointer is initializing correctly."""
    test_list = LinkedList()
    test_list.push('test_string')
    test_list.push(init_value)
    assert test_list.header.pointer.value == 'test_string'


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_pop(init_value):
    """Test pop returns correct value."""
    test_list = LinkedList()
    test_list.push(init_value)
    assert test_list.pop() == init_value



