# -*- coding: utf-8 -*-

"""Tests for  queue.py."""

from __future__ import unicode_literals

from queue import Queue

import pytest
#from linked_list import Node, LinkedList

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
    (TYPE_TABLE, b'1234', True),
    (TYPE_TABLE, 'āĕĳœ', True),
    (TYPE_TABLE, '12345\t', True),
    (TYPE_TABLE, (1, 2, 3), True),
]

#  Tests for Empty Queue

def test_empty_queue_size():
    """Test to see if any empty queue has length zero."""
    empty_queue = Queue()
    assert empty_queue.size == 0


def test_empty_queue_pointer():
    """Test to see if in an empty queue the top is empty."""
    empty_queue = Queue()
    assert empty_queue.top is None

# Tests for XL Queue

def test_size_xl():
    """Test init and size on an xl queue."""
    test_queue = Queue(LONG_queue)
    assert test_queue.size == 30000

# Tests for Enqueue

@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_queue_enqueue_empty(init_value):
    """Test enqueue on an empty queue."""
    test_queue = Queue()
    test_queue.enqueue(init_value)
    assert test_queue.top.value == init_value


@pytest.mark.parametrize('init_queue, result', TABLE_LENGTHS)
def test_enqueue_size(init_queue, result):
    """Test size is correct after a enqueue."""
    test_queue=Queue(init_value)
    test_queue.enqueue('some_string')
    assert test_queue.size == len(init_queue) + 1

# Tests for Dequeue

@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_dequeu.init_value):
    """Test dequeue returns correct value."""
    test_list = DList()
    test_list.append(init_value)
    assert test_list.dequeu) == init_value


def test_shift_empty():
    """Test that dequeueing an empty string returns None."""
    test_list = DList()
    assert test_list.dequeu) is None


@pytest.mark.parametrize('init_list, result', TABLE_LENGTHS)
def test_shift_length(init_list, result):
    """Test length is correct after a dequeue. If dequeue a zero length list, should still be 0."""
    test_list = DList(init_list)
    test_list.dequeu()
    assert test_list.length == max(0, len(init_list) - 1)

# Tests for Peek

????

