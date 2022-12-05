from copy import deepcopy
from csv import reader


stacks = {
    1: ['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'],
    2: ['N', 'B', 'L'],
    3: ['J', 'C', 'H', 'T', 'L', 'V'],
    4: ['S', 'P', 'J', 'W'],
    5: ['Z', 'S', 'C', 'F', 'T', 'L', 'R'],
    6: ['W', 'D', 'G', 'B', 'H', 'N', 'Z'],
    7: ['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'],
    8: ['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'],
    9: ['R', 'P', 'M', 'L', 'H']
}


def part_1():
    stacks_copy = deepcopy(stacks)
    with open('data.csv') as file:
        lines = reader(file)
        for line in lines:
            line = line[0].split(' ')
            quantity, start, end = int(line[1]), int(line[3]), int(line[5])
            stacks_copy[end].extend(stacks_copy[start][-1 * quantity:][::-1])
            stacks_copy[start] = stacks_copy[start][:-1 * quantity]

    return ''.join([stacks_copy[i][-1] for i in range(1, 10)])


def part_2():
    stacks_copy = deepcopy(stacks)
    with open('data.csv') as file:
        lines = reader(file)
        for line in lines:
            line = line[0].split(' ')
            quantity, start, end = int(line[1]), int(line[3]), int(line[5])
            stacks_copy[end].extend(stacks_copy[start][-1 * quantity:])
            stacks_copy[start] = stacks_copy[start][:-1 * quantity]

    return ''.join([stacks_copy[i][-1] for i in range(1, 10)])


if __name__ == '__main__':
    print(f'The answer to part 1 is: {part_1()}')   # TGWSMRBPN
    print(f'The answer to part 2 is: {part_2()}')   # TZLTLWRNF