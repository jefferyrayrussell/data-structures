# -*- coding: utf-8 -*-

"""Test deque.py."""

from __future__ import unicode_literals

from deque import DeQue

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


def test_empty_deque_size():
    """Test to see if any empty queue has length zero."""
    empty_deque = DeQue()
    assert empty_deque.size() == 0


def test_size_xl():
    """Test init and size on an xl deque."""
    test_deque = DeQue(LONG_LIST)
    assert test_deque.size() == 30000


def test_peek():
    """Test the peek functionality."""
    test_list = DeQue(['a', 'b', 'c'])
    assert test_list.peek() == 'c'


def test_peekleft():
    """Test the peekleft functionality."""
    test_list = DeQue(['a', 'b', 'c'])
    assert test_list.peek() == 'a'


# test for append increase in size

# test for append presence of new value

# test for appendleft increase in size

# test for appendleft presence of new value

# test for pop decrease in size

# test for pop to return the correct value

# test for popleft decrease in size

# test for popleft to return the correct value


# test for popleft to return the correct value
