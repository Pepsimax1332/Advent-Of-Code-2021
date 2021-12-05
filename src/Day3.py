from pathlib import Path

FILEPATH = f"{Path()}/data/day3.txt"

test = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


test_data = list(map(lambda x: int(x, 2), test.splitlines()))

with open(FILEPATH, "r") as f:
    data = list(map(lambda x: int(x, 2), f.readlines()))


def task_one(data, bit_len=5):

    bit_count = [0 for _ in range(bit_len)]
    decode = lambda bits : sum(c << i for i, c in enumerate(bits))

    for bit_string in data:
        for bit_index in range(bit_len):
            bit_count[bit_index] += (bit_string & (1 << bit_index)) >> bit_index

    decoded = map(lambda x: x > len(data)/2, bit_count)

    gamma = decode(decoded)
    epsilon = ~gamma & decode([1 for i in range(bit_len)])

    return gamma * epsilon


def task_two(data, bit_len=5):

    o2 = filter_scrubbers(set(data), bit_len, lambda x, y: x <= y)
    co2 = filter_scrubbers(set(data), bit_len, lambda x, y: x > y)

    return o2 * co2


def filter_scrubbers(data, bit_len, func):

    for bit_index in range(bit_len-1, -1, -1):

        lead_1 = set(filter(lambda x: (x & (1 << bit_index)) == 1 << bit_index, data))
        lead_0 = data - lead_1

        if func(len(lead_0), len(lead_1)):
            data = lead_1

        else:
            data = lead_0

        if len(data) == 1:
            return data.pop()



if __name__ == "__main__":
    print(f"Solution to day 2 test task 1: {task_one(test_data.copy())}")
    print(f"Solution to day 2 real task 1: {task_one(data.copy(), 12)}")

    print(f"Solution to day 2 test task 2: {task_two(test_data.copy())}")
    print(f"Solution to day 2 real task 2: {task_two(data, 12)}")