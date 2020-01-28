#!/usr/bin/env python3import sys
import sys

print("starting!")


class UserMainCode(object):
    @classmethod
    def calculate_loss_rate(cls, input1, input2):
        """
        input1 : int
        input2 : int
        Expected return type : int
        """
        input1 = inputone
        input2 = inputtwo
        UserMainCode = cls(input1, input2)
        return UserMainCode

    @staticmethod
    def arithimetic(a, b):
        percent = a / 100
        years = 1 / b
        carryover = pow(percent, years)
        return abs(round((carryover - 1) * 100))


if __name__ == "__main__":
    if len(sys.argv[1:]) < 2:
        inputone = int(input())
        inputtwo = int(input())
    else:
        inputone = int(sys.argv[1])
        inputtwo = int(sys.argv[2])
