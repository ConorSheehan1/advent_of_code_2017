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

# def dfs(grid, i, j, num_regions):
#     print(i, j)
#     # if the index is out of bound return None
#     if not (0 <= i < 128) or not (0 <= j < 128):
#         return 
#     if grid[i][j] == "1":
#         grid[i] = "{}{}{}".format(grid[i][:j], num_regions+2, grid[i][j+1:])
#     else:
#         return
#     # below
#     dfs(grid, i+1, j, num_regions)
#     # left
#     dfs(grid, i, j-1, num_regions)
#     # right
#     dfs(grid, i, j+1, num_regions)
#     return True

# def create_group(grid, i, j, num_regions):
#     for row in grid[i:]:
#         current = row[j]
#         if current == "1":
#             left = row[j-1]
#             right = row[j+1]
#             below = grid[i+1][j]



def part2(data):
    grid = part1(data, part2=True)
    regions = 0
    # there are zeros and ones already, so anything above one will be a region
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "1":
                # if a new group was created, increment regions
                if dfs(grid, i, j, regions):
                    regions += 1
    return regions
