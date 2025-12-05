#!/usr/bin/env python3

"""
Advent of Code 2k25 - Day 04
Day 4: Printing Departement

Search the number or accessible roll of papers using forklifts
in the printing departement.

Usage:
    ./solve.py [PART] input.txt
"""

import sys

grid = []
total_papers = 0

def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return file.read().splitlines()

def get_map(lines: list[str]) -> list[list[int]]:
    """Converts input lines into a 2D map of integers."""
    grid = []
    for line in lines:
        new_line = []
        for char in line:
            if (char == '.'):
                new_line.append(0)
            else:
                new_line.append(1)
        grid.append(new_line)
    return grid


def check_voisins(grid: list[list[int]], x: int, y: int) -> bool:
    """Checks for at least 4 accessible (empty) neighbors around the cell (x, y)."""
    rows = len(grid)
    cols = len(grid[0])
    accessible_count = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # Out of bounds counts as NON-accessible (blocked)
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
            continue  # Don't count out-of-bounds as accessible
        if grid[nx][ny] == 1 or grid[nx][ny] == 2:  # counting paper rolls
            accessible_count += 1
    
    return accessible_count < 4


def find_paper_rolls(grid: list[list[int]]) -> list[list[int]]:
    """Finds all accessible paper rolls in the grid."""
    new_grid = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1 and check_voisins(grid, i, j):
                new_grid[i][j] = 2
    return new_grid

def has_accessible_papers(grid: list[list[int]]) -> bool:
    """Checks if there are any accessible paper rolls in the grid."""
    for row in grid:
        for cell in row:
            if cell == 2:
                return True
    return False


def remove_accessible_papers(grid: list[list[int]]) -> list[list[int]]:
    """Removes accessible paper rolls (marked as 2) from the grid."""
    new_grid = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                new_grid[i][j] = 0
    return new_grid


def main(argv: list[str]) -> int:
    total_papers = 0

    if len(argv) != 3:
        print("Usage: ./solve.py [PART] input.txt")
        return 84

    lines = read_input(argv[2])
    grid = get_map(lines)

    if argv[1] == "1":
        grid = find_paper_rolls(grid)
        for row in grid:
            for cell in row:
                if cell == 2:
                    total_papers += 1
    elif argv[1] == "2":
        while True:
            grid = find_paper_rolls(grid)
            if not has_accessible_papers(grid):
                break

            for row in grid:
                for cell in row:
                    if cell == 2:
                        total_papers += 1
            grid = remove_accessible_papers(grid)
    else:
        print("Usage: ./solve.py [PART] input.txt")
        return 84

    for row in grid:
        print("".join("." if c == 0 else "@" if c == 1 else "x" for c in row))

    print(f"Total accessible paper rolls: {total_papers}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))