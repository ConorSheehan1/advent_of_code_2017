def clean_data(data):
    # used for test data
    for line in data:
        if line[0] != "#":
            return line

def remove_escaped_data(data):
    copy = ""
    skip = 0
    for char in data:
        if char == "!" and skip == 0:
            skip = 2
        if skip > 0:
            skip -= 1
            continue
        if char != "!" and skip == 0:
            copy += char
    return copy

# remove anything between < and >
def remove_garbage(data, keep_tag=False):
    garbage = False
    copy = ""
    for char in data:
        if char == "<":
            garbage = True
        # use continue top skip the step adding the current character to copy
        # since the current char is the closing tag for garbage
        if char == ">":
            garbage = False
            continue
        if not garbage:
            copy += char
    return copy

def count_groups(data):
    score = 0
    level = 0
    for char in data:
        if char == "{":
            level += 1
            score += level
        if char == "}":
            level -= 1
    return score


def part1(data):
    data = remove_escaped_data(data)
    data = remove_garbage(data)
    return count_groups(data)

def part2(data):
    formatted = remove_escaped_data(data)
    no_garbage = remove_garbage(formatted)
    number_of_garbage_tags = formatted.count(">") * 2
    return len(formatted) - len(no_garbage) - number_of_garbage_tags
    # all non-escaped data within garbage tags is the same as the difference between 
    # all non-escaped data and all non-garbage data 
    # (minus the garbage tags themselves since they don't count as data within garbage tags) 

    # 18429 too high
    # 10167 too high


if __name__ == "__main__":
    for k,v in {
        "{}":1 ,"{{{}}}":6, "{{},{}}":5, "{{{},{},{{}}}}":16, "{<a>,<a>,<a>,<a>}":1,
        "{{<ab>},{<ab>},{<ab>},{<ab>}}":9, '{{<!!>},{<!!>},{<!!>},{<!!>}}':9,
        "{{<a!>},{<a!>},{<a!>},{<ab>}}":3
    }.items():
        answer = part1(k)
        print(answer== v, answer, v, "\n\n")
    
