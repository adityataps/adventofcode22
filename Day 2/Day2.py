import csv


ROCK = 1
PAPER = 2
SCISSORS = 3

me_dict = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS
}

you_dict = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS
}

you_me_dict = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}


def part_1():
    curr_score = 0
    with open('data.csv') as file:
        reader = csv.reader(file)
        for line in reader:
            line = line[0]
            you, me = line[0], line[2]
            curr_score += me_dict[me]
            if you_dict[you] == me_dict[me]:    # draw
                curr_score += 3
            elif you_me_dict[you] == me:        # player beats opponent; no addition for loss
                curr_score += 6

    return curr_score


outcome_dict_pt_2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

outcome_you_dict = {
    'X': {'A': SCISSORS, 'B': ROCK, 'C': PAPER},
    'Y': {'A': ROCK, 'B': PAPER, 'C': SCISSORS},
    'Z': {'A': PAPER, 'B': SCISSORS, 'C': ROCK}
}


def part_2():
    curr_score = 0
    with open('data.csv') as file:
        reader = csv.reader(file)
        for line in reader:
            line = line[0]
            you, me = line[0], line[2]
            curr_score += outcome_dict_pt_2[me] + outcome_you_dict[me][you]

    return curr_score


if __name__ == '__main__':
    print(f'The answer to part 1 is: {part_1()}')   # 15422
    print(f'The answer to part 2 is: {part_2()}')   # 15442
