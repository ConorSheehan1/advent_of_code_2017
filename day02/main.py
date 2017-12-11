import itertools

def clean_data(data):
    formatted = []
    for line in data:
        # split on white space (space for test.txt, tabs for input.txt)
        formatted.append(list(map(int, line.split())))
    return formatted


def part1(data):
    def get_checksum(line):
        return max(line) - min(line)
    return sum(map(get_checksum, data))


def part2(data):
    def get_checksum(line):
        # get every combination of two numbers in the list
        for tup in itertools.combinations(line, r=2):
            # order matters because integer should be returned (8/4=2 is correct, can't do 4/8 = 1/2)
            big, small = max(tup), min(tup) 
            if  big % small == 0:
                return big / small
    return sum(map(get_checksum, data))
