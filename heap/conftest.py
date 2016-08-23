import pytest
from binheep import BinNode, BinHeap

@pytest.fixture()
def binnode_empty():
    """Create an empty binnode"""
    test_binnode() = BinNode()

def binnode_1():
    """Create an binnode with value 1"""
    test_binnode() = BinNode(1)