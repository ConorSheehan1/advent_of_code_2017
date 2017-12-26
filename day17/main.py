def clean_data(data):
    return int(data[0])

def part1(data, part2=False, limit=2018):
    step_size = data
    # step_size = 3
    circular_buffer = [0]
    current_position = 0
    # 1 up to 2017
    for i in range(1, limit):
        current_position += step_size
        current_position = current_position % len(circular_buffer)
        current_position += 1
        circular_buffer.insert(current_position, i)
        # current position DOES NOT become the inserted value
        # current_position = i
    if part2:
        return circular_buffer
    return circular_buffer[current_position+1%len(circular_buffer)]


def part2(data):
    step_size = data
    current = 0
    after_zero = 0
    for i in range(1, 50000000):
        # i is the same as length because array increases one element is inserted each iteration
        current += step_size
        current = current% i
        current += 1
        if (current == 1):
            after_zero = i
    return after_zero

# 1898340 too low
# 1898341 is right -_-
# 43292861 too high
