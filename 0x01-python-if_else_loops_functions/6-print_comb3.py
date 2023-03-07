#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if (digit1 == 8) & (digit2 == 9):
            print(f"{digit1}{digit2}")
        else:
            print(f"{digit1}{digit2}, ")
