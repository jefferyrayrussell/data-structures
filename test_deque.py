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

# test for empty deque

def test_empty_DeQue_size():
    """Test to see if any empty queue has length zero."""
    empty_DeQue = DeQue()
    assert empty_queue.size() == 0


# test for size of deque

# test for append increase in size

# test for append presence of new value

# test for appendleft increase in size

# test for appendleft presence of new value

# test for pop decrease in size

# test for pop to return the correct value

# test for popleft decrease in size

# test for popleft to return the correct value

# test for peek to return the correct value

# test for popleft to return the correct value
