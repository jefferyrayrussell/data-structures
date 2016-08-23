# -*- coding: utf-8 -*-
"""Tests for binheap.py."""

from __future__ import unicode_literals

import pytest


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






