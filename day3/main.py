def clean_data(data):
    return data

def is_square(data):
    row_size = len(data[0])
    for row in data:
        if len(row) != row_size:
            return False
    return True

# question about cleaner way to format format string
def print_grid(grid, num, height):
    print("num={}, height={}".format(num, height))
    # biggest number is always bottom right
    space_size = len(str(grid[-1][-1])) + 2
    for row in grid:
        to_format = "{:" + str(space_size) + "}"
        output_string = ""
        for number in row:
            output_string += to_format.format(number)
        print(output_string, row)

def generate_grid(size):
    num, height = 1, 1
    grid = [[1]]
    # always make a square grid
    while num < size:
        print_grid(grid, num, height)

        num += 1
        # if grid is square, add next number to the right of the current bottom right number
        if is_square(grid):
            grid[-1].append(num)

            # then fill the new right hand column, don't take into account bottom and top row
            for i in range(2, height+1):
                num += 1
                print("!!", -i, num)
                grid[-i].append(num)

        top_row = []
        for i in range(height+1):
            num+=1
            top_row.append(num)
        print("top row", top_row)

        # add the top row (in reverse)
        grid.insert(0, top_row[::-1])
        height += 1

        # fill the left column
        for i in range(height):
            num += 1
            grid[i].insert(0, num)

        # add the bottom row
        bottom_row = []
        for i in range(height+1):
            num+=1
            bottom_row.append(num)
        print("bottom row", bottom_row)

        grid.append(bottom_row)
        height += 1
        print_grid(grid, num, height)
    return grid

if __name__ == "__main__":
    generate_grid(int(input()))
