#!/usr/bin/env python3

"""
Advent of Code 2k25 - Day 03
Day 3: Lobby

Find the max voltage you can get from emergency batteries
for the elevator lobby.

Usage:
    ./solve.py input.txt
"""

import sys

total_voltage = 0

def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return file.read().splitlines()


def get_voltage(line: str) -> int:
    """Returns the voltage max produces by two batteries in a bank (line)"""
    first = 0
    second = 0
    index = 0

    for _ in range(len(line) -1):
        if int(line[_]) > first:
            first = int(line[_])
            index = _

    # print(f"Highest battery in bank {first}V [{index}]")

    for _ in range(index + 1, len(line)):
        if int(line[_]) > second:
            second = int(line[_])

    # print(f"Highest volatge in bank {first}{second}V [{index}]")

    voltage = (first * 10) + second
    print(f"Bank {line} produces {voltage}V")
    return voltage

def find_battery(line: str, start_index: int, battery_idx: int) -> int:
    """Finds the highest battery in a bank starting at start_index."""
    highest = -1
    index = start_index

    limit = len(line) - (11 - battery_idx)

    for i in range(start_index, limit):
        if int(line[i]) > highest:
            highest = int(line[i])
            index = i

    # print(f"Finding battery {battery_idx + 1} in bank {line[start_index:]} [{index}]")

    return index


def get_voltage_2(line: str) -> int:
    """return the voltage of one bank using 12 batteries"""
    batteries = [0] * 12
    voltage = ""
    current_pos = 0

    print(f'Processing bank: {line}')

    for i in range(12):
        found_index = find_battery(line, current_pos, i)
        batteries[i] = int(line[found_index])
        current_pos = found_index + 1

    voltage = str(''.join(str(batteries[i]) for i in range(12)))

    print(f"Bank {batteries} [{voltage}V]")

    return int(voltage)


def main(argv: list[str]) -> int:
    global total_voltage

    if len(argv) != 3:
        print("Usage: ./solve.py [PART] input.txt")
        return 84

    lines = read_input(argv[2])

    if int(argv[1]) == 1:
        for line in lines:
            total_voltage += get_voltage(line)
    elif int(argv[1]) == 2:
        for line in lines:
            total_voltage += get_voltage_2(line)
    else:
        print("Invalid part specified. Use '1' or '2'.")
        return 84

    print(f"Total voltage from batteries: {total_voltage}V")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))