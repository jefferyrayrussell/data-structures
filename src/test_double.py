# -*- coding: utf-8 -*-
"""Tests for double.py."""
from __future__ import unicode_literals

import pytest
from double import DNode, DList


TYPE_TABLE = [
    '1',
    1,
    '-' * 10000,
    'āĕĳœ',
    '',
    b'1234',
    '12345\t',
    [1, 2, 3],
    (1, 2, 3)
]

TABLE_LENGTHS = [
    (['a'], "(a)"),
    (['a', ' b'], "(b, a)"),
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
    (TYPE_TABLE, b'1234', True),
    (TYPE_TABLE, 'āĕĳœ', True),
    (TYPE_TABLE, '12345\t', True),
    (TYPE_TABLE, (1, 2, 3), True),
]

# DNode Tests


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_dnode_init_value(init_value):
    """Test that the values initialize correctly."""
    test_dnode = DNode(init_value)
    assert test_dnode.value == init_value


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_dnode_init_next_node(init_value):
    """Test that the next_node pointer initializes correctly."""
    test_dnode = DNode(init_value)
    assert test_dnode.next_node is None


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_dnode_init_prev_node(init_value):
    """Test that the prev_node pointer initializes correctly."""
    test_dnode = DNode(init_value)
    assert test_dnode.prev_node is None


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_dnode_next_node(init_value):
    """Test that the next node pointer returns the correct node."""
    test_dnode = DNode(init_value)
    second_dnode = DNode(init_value, test_dnode)
    assert second_dnode.next_node == test_dnode


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_dnode_pointer(init_value):
    """Test that the previous node pointer returns the correct node."""
    test_dnode = DNode(init_value)
    second_node = DNode(init_value, prev_node=test_dnode)
    assert second_node.prev_node == test_dnode

# DList Test


def test_empty_list_length():
    """Test to see if any empty string has length zero."""
    empty_list = DList()
    assert empty_list.length == 0


def test_empty_list_head():
    """Test to see if in an empty list the head is none."""
    empty_list = DList()
    assert empty_list.head is None


def test_empty_list_tail():
    """Test to see if in an empty list the tail is none."""
    empty_list = DList()
    assert empty_list.tail is None


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_list_push_empty(init_value):
    """Test push on an empty list."""
    test_list = DList()
    test_list.push(init_value)
    assert test_list.head.value == init_value


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_list_push_head_value(init_value):
    """Test push on a non-empty list. Make sure pushing to head."""
    test_list = DList()
    test_list.push('test_string')
    test_list.push(init_value)
    assert test_list.head.value == init_value


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_list_append_empty(init_value):
    """Test append on an empty list."""
    test_list = DList()
    test_list.append(init_value)
    assert test_list.tail.value == init_value


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_list_append_tail_value(init_value):
    """Test append on a non-empty list. Make sure appending to tail."""
    test_list = DList()
    test_list.append('test_string')
    test_list.append(init_value)
    assert test_list.tail.value == init_value


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_list_push_next(init_value):
    """Test push on a non-empty list. Make sure that next pointer is initializing correctly."""
    test_list = DList()
    test_list.push('test_string')
    test_list.push(init_value)
    assert test_list.head.next_node.value == 'test_string'


@pytest.mark.parametrize('init_list, result', TABLE_LENGTHS)
def test_push_length(init_list, result):
    """Test length is correct after a push."""
    test_list = DList(init_list)
    test_list.push('some_string')
    assert test_list.length == len(init_list) + 1


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_list_append_next(init_value):
    """Test append on a non-empty list. Make sure that next pointer is initializing correctly."""
    test_list = DList()
    test_list.append('test_string')
    test_list.append(init_value)
    assert test_list.tail.prev_node.value == 'test_string'


@pytest.mark.parametrize('init_list, result', TABLE_LENGTHS)
def test_append_length(init_list, result):
    """Test length is correct after an append."""
    test_list = DList(init_list)
    test_list.append('some_string')
    assert test_list.length == len(init_list) + 1


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_pop(init_value):
    """Test pop returns correct value."""
    test_list = DList()
    test_list.push(init_value)
    assert test_list.pop() == init_value


def test_pop_empty():
    """Test that popping an empty string returns None."""
    test_list = DList()
    assert test_list.pop() is None


@pytest.mark.parametrize('init_list, result', TABLE_LENGTHS)
def test_pop_length(init_list, result):
    """Test length is correct after a pop. If pop a zero length list, should still be 0."""
    test_list = DList(init_list)
    test_list.pop()
    assert test_list.length == max(0, len(init_list) - 1)


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_shift(init_value):
    """Test shift returns correct value."""
    test_list = DList()
    test_list.append(init_value)
    assert test_list.shift() == init_value


def test_shift_empty():
    """Test that shifting an empty string returns None."""
    test_list = DList()
    assert test_list.shift() is None


@pytest.mark.parametrize('init_list, result', TABLE_LENGTHS)
def test_shift_length(init_list, result):
    """Test length is correct after a shift. If shift a zero length list, should still be 0."""
    test_list = DList(init_list)
    test_list.shift()
    assert test_list.length == max(0, len(init_list) - 1)


def test_size_xl():
    """Test init and size on an xl list."""
    test_list = DList(LONG_LIST)
    assert test_list.size() == 30000


@pytest.mark.parametrize('init_list, search_val, val_is_expected', SEARCH_TABLE)
def test_search(init_list, search_val, val_is_expected):
    """Test display function on longer strings."""
    test_list = DList(init_list)
    if val_is_expected:
        assert test_list.search(search_val).value == search_val
    else:
        with pytest.raises(IndexError):
            test_list.search(search_val)


# New Tests

@pytest.mark.parametrize('init_list, result', TABLE_LENGTHS)
def test_remove_node_length(init_list, result):
    """Test length is correct after a remove."""
    test_list = DList(init_list)
    test_list.remove_node()
    assert test_list.length == max(0, len(init_list) - 1)
