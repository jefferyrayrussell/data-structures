import pytest
from binheap import BinNode, BinHeap

@pytest.fixture()
def binnode_empty():
    """Create an empty binnode."""
    test_binnode = BinNode()
    return test_binnode

@pytest.fixture()
def binnode_1():
    """Create an binnode with value 1."""
    test_binnode = BinNode(1)
    return test_binnode


@pytest.fixture()
def binheap_empty():
    """Create an empty."""
    test_heap = BinHeap()
    return test_heap