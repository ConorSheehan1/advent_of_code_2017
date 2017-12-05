import sys
sys.path.append("..")
from aoc_util import AocUtil


def clean_data(data):
    # each line in the file contains a list with one number, so return a flat list with all numbers
    return [int(line) for line in data]

def print_data(i, data):
    string = "["
    for index, value in enumerate(data):
        if index == i:
            string += "({}),\t".format(value)
        else:
            string += "{},\t".format(value)
    string += "]"
    print(string)


def part1(data):
    return clean_data(data)

    # i, count = 0, 0
    # print_data(count, data)
    # while i < len(data):
    #     data[i]+=1
    #     print(i, data[i], i+data[i])
    #     i = data[i] if data[i] >= 0 else i + data[i]
    #     count += 1
    #     print_data(i, data)
    # return count

if __name__ == "__main__":
    AocUtil.handle_args()

