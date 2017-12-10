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

def get_weight(node_dict):
    # make copy of dict so that order in which weights are calculated for nodes doesn't matter
    new_weights = deepcopy(node_dict)
    # for each node, the weight is itself plus the weight of all its children
    for node in node_dict.keys():
        weight = node_dict[node]["weight"]
        stack = node_dict[node]["children"]
        # print("weight", weight)
        while stack:
            # print("stack", stack)
            next_node = stack.pop()
            # print("next weight", node_dict[next_node]["weight"])
            weight += node_dict[next_node]["weight"]
            children = node_dict[next_node]["children"]
            if children:
                for child in children:
                    stack.append(child)
        new_weights[node]["weight"] = weight
    return new_weights


def part2(data):
    data = get_weight(data)
    # print(data["ugml"]["weight"] == 251)
    # print(data["padx"]["weight"] == 243)
    # print(data["fwft"]["weight"] == 243)


    for node in data.keys():
        children = data[node]["children"] 
        # print(children)
        if children:
            weights = [data[child]["weight"] for child in children]
            if len(set(weights)) > 1:
                print("weights", weights, children)
                # return most common weight from uneven group of weights
                # return max(weights, key=weights.count)

# 2800 too high