def clean_data(data):
    return list(map(int, data[0].split()))


def get_max(data):
    # ties are broken by order, so first largest is largest
    current_max = [0,0]
    for i, val in enumerate(data):
        if val > current_max[1]:
            current_max = [i, val]
    return current_max


def redistribute_data(data):
    index, data_to_redistribute = get_max(data)
    data[index] = 0
    for i in range(1, data_to_redistribute+1):
        # go to the next memory bank after max and redistribute the data
        # wrap around to the start of the list
        data[(index+i)%len(data)]+=1
    return data


# how many redistributions until state is seen again
def part1(data):
    # list of lists, need to use comprehension since [data] would be a reference of data
    # so when data is modified so is [data], messing up while condition
    states = [[v for v in data]]
    count = 1
    data = redistribute_data(data)
    while data not in states:
        states.append([v for v in data])
        data = redistribute_data(data)
        count += 1
    return count

# run until state is seen again
# then how long does it take until state is seen again
def part2(data):
    for i in range(part1(data)):
        data = redistribute_data(data)
    return part1(data)

