import sys
sys.path.append("..")

# from day10.main import part1 as knot_hash
from day10 import main

def clean_data(data):
    return data[0]


# count all the ones in the hashes
def part1(data, part2=False):
    # return bin(int("a0c2017", 16))[2:]
    grid = []
    total = 0
    for i in range(128):
        current = "{}-{}".format(data, i)
        current_hex = main.part2(current)
        # exclud leading 0b
        current_binary = bin(int(current_hex,16))[2:]
        current_binary = "0" * (128 - len(current_binary)) + current_binary
    
        if part2:
            grid.append(current_binary)
        else:
            total += current_binary.count("1")

    if part2:
        return grid
    return total

#8180 too low
#8188 too low

def get_region(grid, stack, seen):
    new_region = 0
    while stack:
        i, j = stack.pop()
        try:
            if grid[i][j] == "1" and (i, j) not in seen:
                new_region = 1
                seen.add((i,j))
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < 128 and 0 <= y < 128 and grid[x][y] == "1" and (x,y) not in seen:
                        stack.append((x,y))
        except Exception as e:
            print("err", i, j)
            raise e
    return new_region

def part2(data):
    grid = part1(data, part2=True)
    seen = set()
    regions = 0
    grid = list(map(list, grid))
    for i in range(128):
        for j in range(128):
            regions += get_region(grid, [(i, j)], seen)
    return regions
