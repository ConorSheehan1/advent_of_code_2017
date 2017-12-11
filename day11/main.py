def clean_data(data):
    return data[0].split(",")

def remove_opposites(data):
    oposite = {'n':'s', 's':'n', 'se':'nw', 'nw':'se', 'ne':'sw', 'sw':'ne'}
    for move in data:
        if oposite[move] in data:
            data.remove(move)
            data.remove(oposite[move])
    return data

def compress_similar(data):
    similar = {'se':['ne','s'], 's':['se','sw'], 'sw':['s','nw'], 'nw':['sw','n'], 'n':['nw','ne'], 'ne':['n','se']}
    for move in data:
        for key, value in similar.items():
            if all(v in data for v in value):
                [data.remove(v) for v in value]
                data.append(key)
    return data


def part1(data):
    data = remove_opposites(data)
    data = compress_similar(data)
    # print(data)
    return len(data)

def part2(data):
    max_distance = 0
    limit = len(data)
    for i in range(limit):
        print(i, limit)
        new_distance = part1(data[:i+1])
        if new_distance > max_distance:
            max_distance = new_distance
            # print(max_distance)
    return max_distance