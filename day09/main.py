def clean_data(data):
    # used for test data
    for line in data:
        if line[0] != "#":
            return line

# garbage start with < and ends with >
# anything after ! in garbage is ignored

# remove anything between < and > preceded by a !
def remove_escaped_data(data):
    garbage = False
    i = 0
    while i < len(data):
        char = data[i]

        # remove ! and char after it if currently in garbage
        if char == "!" and garbage:
            data = data[:i] + data[i+2:]
            i += 2
            continue
        if char == "<" and not garbage:
            garbage = True
        if char == ">":
            garbage = False
        i += 1
    return data

# remove anything between < and >
def remove_garbage(data):
    garbage = False
    i = 0
    while i < len(data):
        char = data[i]
        if char == "<" and not garbage:
            garbage = True
            to_remove = 0
            while garbage:
                if data[i+to_remove] == ">":
                    garbage=False
                    # keep the surround < and >, remove rest
                    data = data[:i+1] + data[i+to_remove:]
                    break
                else:
                    to_remove += 1
        i += 1
    return data

def count_groups(data):
    pass

def part1(data):
    return remove_garbage(remove_escaped_data(data))
    