#!/usr/bin/env python3

"""
Advent of Code 2k25 - Day 01
Day 1: Secret Entrance
]
Find how to open the safe door

This challenge has two parts.
[PART] indicates which part the code is for.

Usage:
    ./solve.py [PART] input.txt
"""

import sys

nb_zeros = 0
actual_dial = 50
MAX_DIAL = 99

def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return file.read().splitlines()


def do_sequence(sequence: str) -> None:
    '''Handles the sequence and counts only when the dial lands on zero.'''
    global actual_dial
    global nb_zeros

    if (sequence[0] == 'R'):
        distance = int(sequence[1:])
        new_dial = (actual_dial + distance) % (MAX_DIAL + 1)
    elif (sequence[0] == 'L'):
        distance = int(sequence[1:])
        new_dial = (actual_dial - distance) % (MAX_DIAL + 1)
    if new_dial == 0:
        global nb_zeros
        nb_zeros += 1
        print(f"Hit zero {nb_zeros} times")

    actual_dial = new_dial


def do_sequence_2(sequence: str) -> None:
    '''Handles the sequence and counts every time the dial passes through zero.'''
    global actual_dial
    global nb_zeros

    distance = int(sequence[1:])
    if (sequence[0] == 'R'):
        while (MAX_DIAL + 1 - actual_dial) <= distance:
            distance -= MAX_DIAL + 1 - actual_dial
            actual_dial = 0
            nb_zeros += 1
            print(f"Hit zero {nb_zeros} times")
        actual_dial = (actual_dial + distance) % (MAX_DIAL + 1)

    elif (sequence[0] == 'L'):
        dist_to_zero = actual_dial if actual_dial > 0 else (MAX_DIAL + 1)
        while dist_to_zero <= distance:
            distance -= dist_to_zero
            actual_dial = 0
            nb_zeros += 1
            print(f"Hit zero {nb_zeros} times")
            dist_to_zero = MAX_DIAL + 1
        actual_dial = (actual_dial - distance) % (MAX_DIAL + 1)


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: ./slove.py <PART> <input_file>")
        return 84

    lines = read_input(argv[2])
    print(f"Read {len(lines)} lines")

    if int(argv[1]) == 1:
        for line in lines:
            do_sequence(line)
        print(f"Total zeros hit: {nb_zeros}")
        return 0

    elif int(argv[1]) == 2:
        for line in lines:
            do_sequence_2(line)
        print(f"Total zeros hit in part 2: {nb_zeros}")
        return 0

    print("Invalid PART specified. Use 1 or 2.")
    return 84


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))