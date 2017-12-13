def clean_data(data):
    return list(map(int, data[0].split(",")))

def part1(data):
    i = 0
    skip_size = 0
    knot = list(range(256))
    for length in data:
        # plus 1?
        knot_section = knot[i%len(knot):(i+length)%len(knot)]
        # reverse section
        knot[i%len(knot):(i+length)%len(knot)] = knot_section[::-1]
        i += length + skip_size
        skip_size += 1
    print(knot)
    return knot[0] * knot[1]
    # 7140 too low
