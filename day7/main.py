def clean_data(data):
    nodes, children = [],[]
    for line in data:
        if " -> " in line:
            n, c = line.split(" -> ")
            children.append(c.split(", "))
        else:
            n = line
        nodes.append(n)
    return nodes, children

def part1(data):
    nodes, children = data
    # remove all weights from nodes
    nodes = list(map(lambda x:x.split("(")[0].strip(), nodes))
    # print("nodes", nodes)
    # print("children", children)
    for node in nodes:
        # if the node is not any other nodes child, it's the root
        if all(node not in arr for arr in children):
            # return node
            return node

def part2(data):
    pass