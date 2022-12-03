import csv
import heapq

def part_1():
    curr_sum = 0
    max_sum = 0

    with open('./data.csv') as file:
        reader = csv.reader(file)
        for line in reader:
            if line:
                curr_sum += int(line[0])
            else:
                max_sum = max(max_sum, curr_sum)
                curr_sum = 0

    return max(max_sum, curr_sum)


def part_2():

    heap = []

    with open('./data.csv') as file:
        reader = csv.reader(file)

        curr_sum = 0
        for line in reader:
            if line:
                curr_sum += int(line[0])
            else:
                heapq.heappush(heap, curr_sum)
                curr_sum = 0

    return sum(heapq.nlargest(3, heap))

if __name__ == '__main__':
    print(f'Answer to part 1: {part_1()}')
    print(f'Answer to part 2: {part_2()}')
