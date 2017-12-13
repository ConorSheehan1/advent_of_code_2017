def clean_data(data):
    d = {}
    for line in data:
        k,v = line.split(": ")
        d[int(k)] = {"pos":0,"range":int(v), "up":True}
    return d

def increment_scanners(data):
    for v in data.values():
        position = v["pos"]
        if position == v["range"]-1:
            v["up"] = False
        if position == 0:
            v["up"] = True
        if v["up"]:
            v["pos"] += 1
        else:
            v["pos"] -= 1


def part1(data):
    caught = []
    last_position = max(data.keys())
    for i in range(last_position+1):
        if i in data.keys():
            position = data[i]["pos"]
            if position == 0:
                caught.append(i*data[i]["range"])
        increment_scanners(data)
    return sum(caught)

def part2(data):
    pass

