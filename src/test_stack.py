# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
from stack import Stack

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


LONG_STACK = ('a b c ' * 10000).split()

# Stack Test


def test_empty_stack_size():
    """Test to see if any empty stack has length zero."""
    empty_stack = Stack()
    assert empty_stack.size() == 0


def test_empty_stack_pointer():
    """Test to see if in an empty stack the top is empty."""
    empty_stack = Stack()
    assert empty_stack.top is None


def test_stack_push_empty():
    """Test push on an empty stack."""
    test_stack = Stack()
    test_stack.push('test_value')
    assert test_stack.top.value == 'test_value'


def test_push_size():
    """Test size is correct after a push."""
    test_stack = Stack(['a', 'b'])
    test_stack.push('some_string')
    assert test_stack.size() == 3


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_pop(init_value):
    """Test pop returns correct value."""
    test_stack = Stack()
    test_stack.push(init_value)
    assert test_stack.pop() == init_value


def test_pop_empty():
    """Test that popping an empty stack returns None."""
    test_list = Stack()
    with pytest.raises(IndexError):
        test_list.pop()



@pytest.mark.parametrize('init_stack, result', TABLE_LENGTHS)
def test_size(init_stack, result):
    """Test ."""
    test_stack = Stack(init_stack)
    assert test_stack.size() == len(init_stack)


def test_pop_length():
    """Test size after a pop in a zero size stack."""
    test_stack = Stack(['a', 'b'])
    test_stack.pop()
    assert test_stack.size() == 1


def test_size_xl():
    """Test init and size on an xl stack."""
    test_stack = Stack(LONG_STACK)
    assert test_stack.size() == 30000
