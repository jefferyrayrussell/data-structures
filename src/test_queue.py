# -*- coding: utf-8 -*-

# Tests for queue.py.

from __future__ import unicode_literals

from queue import Queue

import pytest

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
    assert empty_queue.size() == 0


# Tests for XL Queue

def test_size_xl():
    """Test init and size on an xl queue."""
    test_queue = Queue(LONG_LIST)
    assert test_queue.size() == 30000

# Tests for Enqueue

def test_queue_enqueue_empty():
    """Test enqueue on an empty queue."""
    test_queue = Queue()
    test_queue.enqueue('test')
    assert test_queue.peek() == 'test'


@pytest.mark.parametrize('init_queue, result', TABLE_LENGTHS)
def test_enqueue_size(init_queue, result):
    """Test size is correct after a enqueue."""
    test_queue = Queue(init_queue)
    test_queue.enqueue('some_string')
    assert test_queue.size() == len(init_queue) + 1

# Tests for Dequeue

def test_dequeue():
    """Test dequeue returns correct value."""
    test_list = Queue(['a', 'b', 'c'])
    assert test_list.dequeue() == 'a'


def test_dequeue_empty():
    """Test that dequeueing an empty string returns None."""
    test_list = Queue()
    assert test_list.dequeue() is None


@pytest.mark.parametrize('init_list, result', TABLE_LENGTHS)
def test_dequeue_length(init_list, result):
    """Test length is correct after a dequeue. If dequeue a zero length list, should still be 0."""
    test_list = Queue(init_list)
    test_list.dequeue()
    assert test_list.size() == max(0, len(init_list) - 1)

# Tests for Peek
