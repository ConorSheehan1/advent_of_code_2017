def clean_data(data):
    return data

def get_next_index(current_index, change, xlimit, ylimit):
    new_index = [a+b for a,b in zip(current_index, change)]
    if (0 <= new_index[0] < ylimit) and (0 <= new_index[1] < xlimit):
        return new_index

def part1(data):
    start_char = data[0].strip()
    # x, y coords
    xy = [0, data[0].index(start_char)]
    direction = "down"
    directions = {"up":[-1, 0], "down":[1, 0], "left":[0, -1], "right":[0, 1]}
    letters = []
    ylimit = len(data)
    xlimit = len(data[0])
    while True:
        current = data[xy[0]][xy[1]]
        if current.isalpha():
            letters.append(current
        if get_next_index(current, directions[direction], xlimit, ylimit) is not None:
            current = get_next_index(current, directions[direction], xlimit, ylimit)
        # change direction


