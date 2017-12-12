def clean_data(data):
    d = {}
    for line in data:
        k,v = line.split(" <-> ")
        d[int(k)] = list(map(int, v.split(", ")))
    return d

def part1(data, id=0, return_group=False):
    # print(f"data:\n{data}\n")
    group = {id}
    sizes = [1]
    # keep going until size stops growing
    while True:
        for key, value in data.items():
            if key in group or any(v in group for v in value):
                group.add(key)
                [group.add(v) for v in value]
        sizes.append(len(group))
        if sizes[-1] == sizes[-2]:
            # return group, otherwise return size of group
            if return_group:
                return group
            return sizes[-1]

def part2(data):
    groups = []
    for key, value in data.items():
        # if the id isn't in any group, see if it's a new group
        if not any(key in group for group in groups):
            new_group = part1(data, id=key, return_group=True)
            if new_group not in groups:
                groups.append(new_group)
    # print(groups)
    return len(groups)
