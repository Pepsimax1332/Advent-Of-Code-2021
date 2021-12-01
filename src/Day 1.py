#Day 1
from pathlib import Path
from typing import Iterable

FILEPATH = f"{Path()}\data\Day1.txt"

test = """199
200
208
210
200
207
240
269
260
263"""

test_data = list(map(int, test.splitlines()))
with open(FILEPATH, "r") as f:
    data = list(map(int, f.readlines()))


def task(list: Iterable[int], win_size: int=1) -> int:
    l = (map(sum, zip(*[list[i+j:] for i in range(win_size)])) for j in range(2))
    return sum([prev < cur for prev, cur in zip(*l)])


print(f"Solution to day 1 test task 1: {task(test_data)}")
print(f"Solution to day 1 real task 1: {task(data, 1)}")

print(f"Solution to day 1 test task 2: {task(test_data, 3)}")
print(f"Solution to day 1 real task 2: {task(data, 3)}")