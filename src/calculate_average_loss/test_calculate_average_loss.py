#!/usr/bin/env python3
"""
test_calculate_average_loss.py
"""

from src.calculate_average_loss.calculate_average_loss import UserMainCode

user = UserMainCode()


def test_calculate_loss_rate():
    input1 = 72
    input2 = 13
    assert type(input1) == int
    assert type(input2) == int
    assert user.calculate_loss_rate(input1, input2) == int(round(input1 / input2))
