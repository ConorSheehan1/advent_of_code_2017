def part1(data):
    to_sum = [0]
    for i in range(len(data)):
        if data[i] == data[(i+1)%len(data)]:
            to_sum.append(data[i])
    return sum(map(lambda x: int(x), to_sum))


def part2(data):
    to_sum = [0]
    for i in range(len(data)):
        # check for integer division?
        # print(i, (i+(len(data)//2))%len(data))
        if data[i] == data[(i+(len(data)//2))%len(data)]:
            to_sum.append(data[i])
    return sum(map(lambda x: int(x), to_sum))