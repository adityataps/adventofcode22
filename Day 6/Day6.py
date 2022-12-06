from csv import reader


def part_1():
    with open('data.csv') as file:
        lines = reader(file)
        start = 0
        end = 4
        for line in lines:
            line = line[0]
            while end < len(line):
                subset = set(line[start:end])
                if len(subset) == 4:
                    return end
                else:
                    start += 1
                    end += 1

        return end



def part_2():
    with open('data.csv') as file:
        lines = reader(file)
        start = 0
        end = 14
        for line in lines:
            line = line[0]
            while end < len(line):
                subset = set(line[start:end])
                if len(subset) == 14:
                    return end
                else:
                    start += 1
                    end += 1

        return end


if __name__ == '__main__':
    print(f'The answer to part 1 is: {part_1()}')   # 1757
    print(f'The answer to part 2 is: {part_2()}')   # 2950