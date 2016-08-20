# -*- coding: utf-8 -*-
"""Class implimentation of a singly linked list."""
from __future__ import unicode_literals

import pytest
from linked_list import Node, LinkedList

TYPE_TABLE = [
    ['1'],
    [1],
    ['-'] * 10000,
    ['āĕĳœ'],
    [],
    [b'1234'],
    ['12345\t'],
    [1, 2, 3],
    (1, 2, 3)
]

TABLE_LENGTHS = [
    (['a'], "(a)"),
    (['a', 'b'], "(b, a)"),
    (['a', 'b', 'c'], "(c, b, a)"),
    (('a b c ' * 5).split(), "(c, b, a, c, b, a, c, b, a, c, b, a, c, b, a)"),
    ([], None)
]


LONG_LIST = ('a b c ' * 10000).split()

SEARCH_TABLE = [
    (['a'], 'a', True),
    (['1'], '1', True),
    ([], '1', False),
    ([1, 2, 3], 1, True),
    ([1, 2, 3], '1', False),
    ([1, 2, 3], 4, False),
    ([[1, 2], 3], 1, False),
    ([[1, 2], 3], [1, 2], True),
    ([1, 2, 3], None, False),
    ([1, 2, 3, 2], 2, True),
    ([1] + LONG_LIST, 1, True),
    (LONG_LIST + [1], 1, True),
    (TYPE_TABLE, [b'1234'], True),
    (TYPE_TABLE, ['āĕĳœ'], True),
    (TYPE_TABLE, ['12345\t'], True),
    (TYPE_TABLE, (1, 2, 3), True),
]

# Node Tests


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_node_init_value(init_value):
    """Test that the values initialize correctly."""
    test_node = Node(init_value)
    assert test_node.value == init_value


def test_node_init_pointer():
    """Test that the pointer initializes correctly."""
    test_node = Node('test')
    assert test_node.pointer is None


def test_node_pointer():
    """Test that the node pointer returns the correct node."""
    test_node = Node('init_node')
    second_node = Node('second_node', test_node)
    assert second_node.pointer == test_node

# List Test


def test_empty_list_length():
    """Test to see if any empty string has length zero."""
    empty_list = LinkedList()
    assert empty_list.length == 0


@pytest.mark.parametrize('init_list, result', TABLE_LENGTHS)
def test_length(init_list, result):
    """Test the size function on strings of different lengths."""
    test_list = LinkedList(init_list)
    assert test_list.length == len(init_list)


@pytest.mark.parametrize('init_list, result', TABLE_LENGTHS)
def test_size(init_list, result):
    """Test the size function on strings of different lengths."""
    test_list = LinkedList(init_list)
    assert test_list.size() == len(init_list)


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


def test_list_push_head_value():
    """Test push on a non-empty list. Make sure pushing to head."""
    test_list = LinkedList()
    test_list.push('initial_node')
    test_list.push('second_node')
    assert test_list.header.value == 'second_node'


def test_list_push_pointer():
    """Test push on a non-empty list. Make sure that pointer is initializing correctly."""
    test_list = LinkedList()
    test_list.push('initial_node')
    test_list.push('second_node')
    assert test_list.header.pointer.value == 'initial_node'


def test_push_length():
    """Test length is correct after a push."""
    test_list = LinkedList(['a', 'b'])
    test_list.push('c')
    assert test_list.size() == 3


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_pop(init_value):
    """Test pop returns correct value."""
    test_list = LinkedList()
    test_list.push(init_value)
    assert test_list.pop() == init_value


def test_pop_empty():
    """Test that popping an empty string returns None."""
    test_list = LinkedList()
    with pytest.raises(IndexError):
        test_list.pop()


def test_pop_length():
    """Test length is correct after a pop."""
    test_list = LinkedList(['a', 'b'])
    test_list.pop()
    assert test_list.size() == 1


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_display(init_value):
    """Test display function."""
    test_list = LinkedList()
    test_list.push(init_value)
    assert test_list.display() == '({0})'.format(init_value)


@pytest.mark.parametrize('init_list, result', TABLE_LENGTHS)
def test_display_long(init_list, result):
    """Test display function on longer strings."""
    test_list = LinkedList(init_list)
    assert test_list.display() == result


def test_size_xl():
    """Test init and size on an xl list."""
    test_list = LinkedList(LONG_LIST)
    assert test_list.size() == 30000


@pytest.mark.parametrize('init_list, search_val, result', SEARCH_TABLE)
def test_search(init_list, search_val, result):
    """Test display function on longer strings."""
    test_list = LinkedList(init_list)
    assert bool(test_list.search(search_val)) is result
