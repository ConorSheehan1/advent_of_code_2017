from copy import deepcopy

def clean_data(data):
    nc_delim = " -> "
    nodes = {}
    for line in data:
        if nc_delim in line:
            n, c = line.split(nc_delim)
            children = c.split(", ")
        else:
            children = []
            n = line
        node, weight = n.split()
        node_data = {}
        node_data["weight"] = int(weight.replace("(", "").replace(")", ""))
        node_data["children"] = children
        nodes[node] = node_data
    return nodes

def get_root(data):
    children = []
    for node in data.keys():
        [children.append(child) for child in data[node]["children"]]
    return [node for node in data.keys() if node not in children]

def get_order(data, root):
    # breadth first traverse the dictionary of nodes and return traversal order (for bottom of graph up)
    path = [root]
    queue = [root]
    while queue:
        current = queue.pop()
        children = data[current]["children"]
        if children:
            [queue.insert(0, child) for child in children]
            [path.insert(0, child) for child in children]
    return path

def get_weight(data, node):
    data[node]["weight"] += sum(data[child]["weight"] for child in data[node]["children"])


def part1(data):
    return get_root(data)


def part2(data):
    # root should always be single value, if not wrong number of args will throw exception
    original_weight = deepcopy(data)
    order = get_order(data, *get_root(data))
    # the new weight of each node is the sum of all its childrens weights and its own weight
    for node in order:
        get_weight(data, node)

    # # for test input, returned value should be 60
    # print(data["ugml"]["weight"] == 251)
    # print(data["padx"]["weight"] == 243)
    # print(data["fwft"]["weight"] == 243)

    # get the first node whos children don't all have the same weight
    for node in order:
        children =  data[node]["children"]
        if children:
            first_weight = data[children[0]]["weight"]
            for child in children:
                if data[child]["weight"] != first_weight:
                    child_dict = {c:data[c]["weight"] for c in children}
                    # get the child with the most weight
                    max_child = max(child_dict, key=child_dict.get)
                    min_child = min(child_dict, key=child_dict.get)
                    # return the origin weight of the heaviest child 
                    # minus the difference between its overall weight and siblings overal weight
                    return original_weight[max_child]["weight"] - (data[max_child]["weight"] - data[min_child]["weight"])

# 2800 too high
# 2607 too high