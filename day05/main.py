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
    i, count = 0, 0
    while i < len(data):
        jump = data[i]
        data[i]+=1
        i += jump
        count += 1
        # print_data(i, data)
    return count

def part2(data):
    i, count = 0, 0
    # print_data(count, data)
    while i < len(data):
        jump = data[i]
        if jump >= 3:
            data[i]-=1
        else:
            data[i]+=1
        i += jump
        count += 1
        # print_data(i, data)
    return count   