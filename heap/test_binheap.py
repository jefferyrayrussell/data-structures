# -*- coding: utf-8 -*-
"""Tests for binheap.py."""

from __future__ import unicode_literals

import pytest



def test_binnode_init_value(binnode_1):
    """Test that the values initialize correctly."""
    assert test_node.value == 1


def test_binnode_init_value(binnode_1):
    """Test that the values initialize correctly."""
    assert test_node.parent is None


def test_binnode_init_value(binnode_1):
    """Test that the values initialize correctly."""
    assert test_node.child_a is None


def test_binnode_init_value(binnode_1):
    assert test_node.child_b is None


def test_binnode_init_value(binnode_1):
    """Test that the values initialize correctly."""
    test_node_2 = BinNode(2, binnode_1)
    assert test_node.parent is binnode_1






