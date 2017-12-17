def clean_data(data):
    to_return = {}
    for line in data:
        # advanced unpacking doesn't work with pypy
        # _, generator, *_, number = line.split(" ")
        arr = line.split(" ")
        to_return[arr[1]] = int(arr[-1])
    return to_return

def part1(data):
    score = 0
    prev = data
    factors = {"A":16807, "B":48271}
    for i in range(40000000):
        for generator in prev.keys():
            tmp = prev[generator]
            prev[generator] = (tmp * factors[generator]) % 2147483647
        if bin(prev["A"])[-16:] == bin(prev["B"])[-16:]:
            score += 1
    return score

def part2(data):
    a_out, b_out = [], []
    score = 0
    prev = data
    factors = {"A":16807, "B":48271}
    for i in range(40000000):
        for generator in prev.keys():
            tmp = prev[generator]
            new_number = (tmp * factors[generator]) % 2147483647
            prev[generator] = new_number
            if new_number % 4 == 0 and generator == "A":
                a_out.append(new_number)
            elif new_number % 8 == 0 and generator == "B":
                b_out.append(new_number)
    for a, b in zip(a_out, b_out):
        if bin(a)[-16:] == bin(b)[-16:]:
            score += 1
    return score


