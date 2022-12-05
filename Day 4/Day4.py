import csv


def part_1():
    count = 0
    with open('data.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            elf_1, elf_2 = line
            start_1, end_1 = elf_1.split('-')
            start_2, end_2 = elf_2.split('-')
            start_1, end_1, start_2, end_2 = [int(i) for i in [start_1, end_1, start_2, end_2]]

            if (start_1 <= start_2 and end_1 >= end_2) \
                    or (start_2 <= start_1 and end_2 >= end_1):
                count += 1

    return count


def part_2():
    count = 0
    with open('data.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            elf_1, elf_2 = line
            start_1, end_1 = elf_1.split('-')
            start_2, end_2 = elf_2.split('-')
            start_1, end_1, start_2, end_2 = [int(i) for i in [start_1, end_1, start_2, end_2]]

            if start_2 > start_1:
                if start_2 <= end_1:
                    count += 1
            elif start_1 > start_2:
                if start_1 <= end_2:
                    count += 1
            else:
                count += 1

        return count


if __name__ == '__main__':
    print(f'The answer to part 1 is: {part_1()}')   # 453
    print(f'The answer to part 2 is: {part_2()}')   # 919
