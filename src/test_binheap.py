# -*- coding: utf-8 -*-
"""Tests for binheap.py."""

from __future__ import unicode_literals

import pytest

TABLE_TO_INITALIZE_HEAP = [
    ([1]),
    ([1, 2]),
    ([1, 2, 3]),
    ([1, 2, 3, 4]),
    ([-100, -50, 0, 50, 100]),    
    ([])
]


def test_binnode_check_init_value(binnode_1):
    """Test that the values initialize correctly."""
    assert binnode_1.value == 1


def test_binnode_check_parent(binnode_1):
    """Test that the values initialize correctly."""
    assert binnode_1.parent is None


def test_binnode_check_child_a(binnode_1):
    """Test that the values initialize correctly."""
    assert binnode_1.child_a is None


def test_binnode_check_b(binnode_1):
    assert binnode_1.child_b is None


def test_binnode_passed_in_parent(binnode_1):
    """Test that the values initialize correctly."""
    from binheap import BinNode
    test_node_2 = BinNode(2, binnode_1)
    assert test_node_2.parent is binnode_1


def test_empty_heap_head(binheap_empty):
    assert binheap_empty.top is None


def test_empty_heap_list(binheap_empty):
    assert binheap_empty.bin_heap_list == []


def test_heapness():
    from binheap import BinHeap
    our_heap = BinHeap([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for item in our_heap.bin_heap_list[1:]:
        assert item.value <= item.parent.value


@pytest.mark.skipif("sys.version_info[0] < 3")
def test_bin_heap_different_types():
    from binheap import BinHeap
    with pytest.raises(TypeError):
        our_heap = BinHeap([1, 2, 'a', 3, 6])


def test_bin_heap_int():
    from binheap import BinHeap
    with pytest.raises(AttributeError):
        our_heap = BinHeap(6)


def test_bin_heap_str():
    from binheap import BinHeap
    with pytest.raises(AttributeError):
        our_heap = BinHeap('cat')


def test_push_length():
    from binheap import BinHeap
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    our_heap = BinHeap(data_list)
    our_heap.push(10)
    assert len(our_heap.bin_heap_list) == len(data_list) + 1  


def test_push_heapiness():
    from binheap import BinHeap
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    our_heap = BinHeap(data_list)
    our_heap.push(10)
    for item in our_heap.bin_heap_list[1:]:
        assert item.value <= item.parent.value


def test_push_top_value():
    from binheap import BinHeap
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    our_heap = BinHeap(data_list)
    our_heap.push(10)
    assert our_heap.top.value == 10


def test_pop_return_value():
    from binheap import BinHeap
    data_list = [4, 6, 2, 1, 5, 8, 9, 0, 6]
    our_heap = BinHeap(data_list)
    assert our_heap.pop() == max(data_list)


def test_pop_return_length():
    from binheap import BinHeap
    data_list = [4, 6, 2, 1, 5, 8, 9, 0, 6]
    our_heap = BinHeap(data_list)
    our_heap.pop()
    assert len(our_heap.bin_heap_list) == len(data_list) - 1


def test_pop_heapiness():
    from binheap import BinHeap
    data_list = [4, 6, 2, 1, 5, 8, 9, 0, 6]
    our_heap = BinHeap(data_list)
    our_heap.pop()
    for item in our_heap.bin_heap_list[1:]:
        assert item.value <= item.parent.value


def test_pop_not_in_list():
    from binheap import BinHeap
    data_list = [4, 6, 2, 1, 5, 8, 9, 0, 6]
    our_heap = BinHeap(data_list)
    our_heap.pop()
    assert max(data_list) not in our_heap.bin_heap_list


def test_pop_zero_length_heap():
    from binheap import BinHeap
    our_heap = BinHeap()
    with pytest.raises(IndexError):
        our_heap.pop()


def test_pop_one_item_head():
    from binheap import BinHeap
    our_heap = BinHeap([10])
    our_heap.pop()
    assert our_heap.top == None


def test_pop_childb_bigger():
    from binheap import BinHeap
    our_heap = BinHeap([10])
    our_heap.push(5)
    our_heap.push(6)
    our_heap.push(1)
    our_heap.push(2)
    our_heap.push(1)
    our_heap.push(2)
    our_heap.pop()
    assert our_heap.top.value == 6

