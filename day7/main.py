from copy import deepcopy

# todo: create cleaning function that works for both parts
def clean_data1(data):
    nodes, children = [],[]
    for line in data:
        if " -> " in line:
            n, c = line.split(" -> ")
            children.append(c.split(", "))
        else:
            n = line
        nodes.append(n)
    return nodes, children

# class Node():
#     def __init__(self, name, weight, children=None):
#         self.name = name
#         self.weight = weight
#         self.children = children

# class Tree():
#     def __init__(self, root):
#         self.root = Node(*root)

#     def dfs(graph, start):
#         visited, stack = set(), [start]
#         while stack:
#             vertex = stack.pop()
#             if vertex not in visited:
#                 visited.add(vertex)
#                 stack.extend(graph[vertex] - visited)
#         return visited


#     def add_node(self, data):



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


def part2(data):
    # print(get_root(data))
    # root should always be single value, if not wrong number of args will throw exception
    original_weight = deepcopy(data)
    order = get_order(data, *get_root(data))
    for node in order:
        get_weight(data, node)

    # # print(data)
    # weights = [data[node]["weight"] for node in order]
    # # print(weights)
    # # create sliding window three spaces wide
    # # the first weight that is different from the weight before and after it is the problem
    # for first, second, third in zip(weights, weights[1:], weights[2:]):
    #     # print(first, second, third)
    #     # pass
    #     if first != second and second != third:
    #         # return first
    #         print(first, second, third)

    # get the first node whos children don't all have the same weight
    for node in order:
        children =  data[node]["children"]
        if children:
            first_weight = data[children[0]]["weight"]
            for child in children:
                if data[child]["weight"] != first_weight:
                    child_dict = {c:data[c]["weight"] for c in children}
                    print(child_dict)
                    # get the child with the most weight
                    max_child = max(child_dict, key=child_dict.get)
                    min_child = min(child_dict, key=child_dict.get)
                    # return the origin weight of the heaviest child 
                    # minus the difference between its overall weight and siblings overal weight
                    return original_weight[max_child]["weight"] - (data[max_child]["weight"] - data[min_child]["weight"])

    # print(data["ugml"]["weight"] == 251)
    # print(data["padx"]["weight"] == 243)
    # print(data["fwft"]["weight"] == 243)



# 2800 too high
# 2607 too high