from collections import Counter
from csv import reader


priority = {i: (i - 96) for i in range(97, (97+26))}
priority.update({i: (i - 38) for i in range(65, 65+26)})


def part_1():
    sum = 0
    with open('data.csv') as file:
        lines = reader(file)
        for line in lines:
            line = line[0]
            sack_1 = set(line[:len(line) // 2])
            sack_2 = set(line[len(line) // 2:])
            sum += priority.get(ord(list(sack_1.intersection(sack_2))[0]))

    return sum


def part_2():
    sum = 0
    with open('data.csv') as file:
        lines = list(reader(file))
        num_chunks = len(lines) // 3
        for i in range(num_chunks):
            sack_1 = set(lines[3 * i][0])
            sack_2 = set(lines[3 * i + 1][0])
            sack_3 = set(lines[3 * i + 2][0])
            sum += priority.get(ord(list(set.intersection(sack_1, sack_2, sack_3))[0]))

    return sum


if __name__ == '__main__':
    print(f'The answer to part 1 is: {part_1()}')   # 8349
    print(f'The answer to part 2 is: {part_2()}')   # 2681
