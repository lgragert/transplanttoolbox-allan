#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from transplanttoolbox_allan.conversion_functions import convert_allele_to_ag

__author__ = "Gragert Lab"
__copyright__ = "Gragert Lab"
__license__ = "gpl3"


def test_single_allele_to_ag():
	assert conversion_functions("B*07:02") == {'B*07:02': ['B7', 'Bw6']}
   




    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
