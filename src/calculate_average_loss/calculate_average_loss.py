#!/usr/bin/env python3
"""
calculate_average_loss.py
"""


class UserMainCode(object):
    """Un-editable challenge portion"""

    @classmethod
    def calculate_loss_rate(cls, input1, input2):
        """
        input1: int
        input2: int
        Checks for type and value and int value.
        """
        if type(input1) != int or type(input2) != int:
            raise TypeError("Input must be of type int")
        elif input1 < 0 or input2 < 0:
            raise ValueError("Input must be a positive int.")
        else:
            return int(round(input1 / input2))
