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
    assert empty_stack.size == 0


def test_empty_stack_pointer():
    """Test to see if in an empty stack the top is empty."""
    empty_stack = Stack()
    assert empty_stack.top is None


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_stack_push_empty(init_value):
    """Test push on an empty stack."""
    test_stack = Stack()
    test_stack.push(init_value)
    assert test_stack.top.value == init_value


@pytest.mark.parametrize('init_stack, result', TABLE_LENGTHS)
def test_push_size(init_stack, result):
    """Test size is correct after a push."""
    test_stack = Stack(init_stack)
    test_stack.push('some_string')
    assert test_stack.size == len(init_stack) + 1


@pytest.mark.parametrize('init_value', TYPE_TABLE)
def test_pop(init_value):
    """Test pop returns correct value."""
    test_stack = Stack()
    test_stack.push(init_value)
    assert test_stack.pop() == init_value


def test_pop_empty():
    """Test that popping an empty stack returns None."""
    test_stack = Stack()
    assert test_stack.pop() is None


@pytest.mark.parametrize('init_stack, result', TABLE_LENGTHS)
def test_pop_length(init_stack, result):
    """Test size after a pop in a zero size stack."""
    test_stack = Stack(init_stack)
    test_stack.pop()
    assert test_stack.size == max(0, len(init_stack) - 1)


@pytest.mark.parametrize('init_stack, result', TABLE_LENGTHS)
def test_size(init_stack, result):
    """Test display function on longer strings."""
    test_stack = Stack(init_stack)
    assert test_stack.size == len(init_stack)


def test_size_xl():
    """Test init and size on an xl stack."""
    test_stack = Stack(LONG_STACK)
    assert test_stack.size == 30000
