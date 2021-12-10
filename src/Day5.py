from pathlib import Path

FILEPATH = f"{Path()}/data/day5.txt"


test = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


test_data = [sorted([tuple(map(int, points.split(","))) for points in line.split(" -> ")]) for line in test.split("\n")]

with open(FILEPATH, "r") as f:
    data = [sorted([tuple(map(int, points.split(","))) for points in line.split(" -> ")]) for line in f.read().split("\n")]


def task_one(data):

    vertical = list(filter(lambda x: x[0][0] == x[1][0], data))
    horizontal = list(filter(lambda x: x[0][1] == x[1][1], data))

    max_x, max_y = max_coords(data)

    map = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

    for line in vertical:
        for y in range(line[0][1], line[1][1]+1):
            map[y][line[0][0]] += 1


    for line in horizontal:
        for x in range(line[0][0], line[1][0] + 1):
            map[line[0][1]][x] += 1


    return len(list(filter(lambda x: x > 1, sum(map, []))))


def task_two(data):

    vertical = list(filter(lambda x: x[0][0] == x[1][0], data))
    horizontal = list(filter(lambda x: x[0][1] == x[1][1], data))
    diagonal = list(filter(lambda x: x not in vertical and x not in horizontal, data))

    max_x, max_y = max_coords(data)

    map = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

    for line in vertical:
        for y in range(line[0][1], line[1][1]+1):
            map[y][line[0][0]] += 1


    for line in horizontal:
        for x in range(line[0][0], line[1][0] + 1):
            map[line[0][1]][x] += 1


    for line in diagonal:
        x1, y1 = line[0][0], line[0][1]
        x2, y2 = line[1][0], line[1][1]

        if x1 > x2 and y1 < y2:
            for x, y in zip(range(x1, x2-1, -1), range(y1, y2+1)):
                map[y][x] += 1

        elif x1 < x2 and y1 > y2:
            for x, y in zip(range(x1, x2+1), range(y1, y2-1, -1)):
                map[y][x] += 1

        elif x1 < x2 and y1 < y2:
            for x, y in zip(range(x1, x2+1), range(y1, y2+1)):
                map[y][x] += 1

        elif x1 > x2 and y1 > y2:
            for x, y in zip(range(x1, x2-1, -1), range(y1, y2-1, -1)):
                map[y][x] += 1
    
    return len(list(filter(lambda x: x > 1, sum(map, []))))

def max_coords(data):

    max_x, max_y = 0, 0

    for x, y in sum(data, []):
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    return max_x, max_y


if __name__ == "__main__":
    print(f"Solution to day 4 test task 1: {task_one(test_data)}")
    print(f"Solution to day 4 real task 1: {task_one(data)}")
    print(f"Solution to day 4 test task 2: {task_two(test_data)}")
    print(f"Solution to day 4 real task 2: {task_two(data)}")

