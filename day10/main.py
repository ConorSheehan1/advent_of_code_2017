from collections import OrderedDict

def clean_data(data):
    return list(map(int, data[0].split(",")))

def reverse_selection(knot, i, length):
    selection = []
    indexes = []
    for index in range(i, i+length):
        currnet_index = index%len(knot)
        selection.append(knot[currnet_index])
        indexes.append(currnet_index)
    # print("selection", selection, "indexes", indexes)
    # reverse the selection
    selection = selection[::-1]
    # add back into list (mutate knot inplace)
    for replace_index in indexes:
        knot[replace_index] = selection.pop(0)

def to_hex(num):
    hex_rep = hex(num).split("x")[-1]
    if len(hex_rep) == 1:
        return "0"+hex_rep
    return hex_rep

def part1(data):
    size = 256
    knot = list(range(size))
    for length in data:
        # print(knot, i, skip)
        if length > size:
            continue
        reverse_selection(knot, i, length)
        i += length + skip
        skip += 1
    return knot[0]*knot[1]

def part2(data):

    size = 256
    # data=[1,2,3]
    if type(data) == str:
        string_data = data
    else:
        string_data = ",".join(map(str, data))
    bytes_data = [ord(char) for char in string_data]
    bytes_data.extend([17, 31, 73, 47, 23])
    # bytes_data = [3, 4, 1, 5, 17, 31, 73, 47, 23]
    i, skip = 0, 0
    knot = list(range(size))
    # basically calling part1 here, possibly refactor?
    for round in range(64):
        for length in bytes_data:
            if length > size:
                continue
            reverse_selection(knot, i, length)
            i += length + skip
            skip += 1
    sparse_hash = knot
    dense_hash = []
    chunk_size = 16
    # print(sparse_hash)
    for i in range(0, len(sparse_hash), chunk_size):
        # xor each 16 bit chunk and add to the dense hash
        dense_hash.append(eval("^".join(map(str, sparse_hash[i:i+chunk_size]))))
    return "".join([to_hex(num) for num in dense_hash])
