#!/usr/bin/env python3

"""
Advent of Code 2k25 - Day 02
Day 02: Gift Shop

Usage:
    ./solve.py input.txt
"""

import sys

sumInvalidID = 0

def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return file.read().splitlines()

def check_range(line: str) -> int:
    '''Checks for any invalid ids in the given range and adds them to the sum.'''
    global sumInvalidID

    parts = line.split('-')
    for i in range(int(parts[0]), int(parts[1]) + 1):
        strID = str(i)
        if len(strID) % 2 != 0:
            continue

        firstpart, secondpart = strID[:len(strID)//2], strID[len(strID)//2:]
        if firstpart == secondpart:
            sumInvalidID += i
            print(f"Found invalid ID: {i} ({firstpart}|{secondpart})")

    return 0

def check_range_2(line: str) -> int:
    '''Checks for any ids with repeating patterns in the given range and adds them to the sum.'''
    global sumInvalidID

    parts = line.split('-')
    for i in range(int(parts[0]), int(parts[1]) + 1):
        strID = str(i)
        length = len(strID)

        for pattern_length in range(1, length // 2 + 1):
            substring = strID[0:pattern_length]
            if length % pattern_length != 0: # cant be a pattern if it doesnt divide evenly
                continue
            repetitions = length // pattern_length
            if substring * repetitions == strID:
                sumInvalidID += i
                print(f"Found invalid ID with pattern: {i} (pattern: {substring})")
                break
    return 0

def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: ./solve.py [PART] input.txt")
        return 1

    input_file = argv[2]
    lines = read_input(input_file)

    if argv[1] == "1":
        for line in lines:
            check_range(line)
    elif argv[1] == "2":
        for line in lines:
            check_range_2(line)
    else:
        print("Invalid part specified. Use '1' or '2'.")
        return 84

    print(f"Total sum of invalid IDs: {sumInvalidID}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))