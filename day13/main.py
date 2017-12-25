def clean_data(data):
    d = {}
    for line in data:
        k,v = line.split(": ")
        d[int(k)] = {"pos":0,"range":int(v), "up":True}
    return d

# def clean_data(data):
#     d = {}
#     for line in data:
#         k,v = line.split(": ")
#         d[int(k)] = int(v)
#     return d

# def print_data(data):
#     # lines is equivilant to highest range
#     top_line = "\t".join(list(map(str, range(max(data.keys())+1))))
#     for i in range(max(data.values(), key=lambda x: x['range'])["range"]):
#         pass
#     print(top_line)


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

def reset_scanners(data, offset):
    for k in data.keys():
        data[k]["pos"] = 0
    for i in range(offset):
        increment_scanners(data)
    # print(data)

def set_scanners(data, time):
    for i in data.keys():
        height = data[i]["range"]
        offset = time % ((height - 1) * 2)

        if offset > height - 1:
            data[i]["pos"] =  2 * (height - 1) - offset
        else:
            data[i]["pos"] = offset

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
    start = 0
    last_position = max(data.keys())
    while True:
        # print(start)
        set_scanners(data, start)
        for i in range(last_position+1):
            set_scanners(data, start+i)
            if i in data.keys():
                if data[i]["pos"] == 0:
                    # print("caught", start)
                    break
            # print("not caught", i)
        else:
            return start 
        start +=1 

# 10366 too low
# 26900 too low
# 3876272 answer
