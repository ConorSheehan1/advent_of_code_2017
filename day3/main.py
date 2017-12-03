def clean_data(data):
    return data

def is_square(data):
    row_size = len(data[0])
    for row in data:
        if len(row) != row_size:
            return False
    return True

# question about cleaner way to format format string
def print_grid(grid):
    # biggest number is always bottom right
    space_size = len(str(grid[-1][-1])) + 2
    for row in grid:
        to_format = "{:" + str(space_size) + "}"
        output_string = ""
        for number in row:
            output_string += to_format.format(number)
        print(output_string)

def generate_grid(size):
    num, height = 1, 1
    grid = [[1]]
    # always make a square grid
    while num < size:
        num += 1
        # if grid is square, add next number to the right of the current bottom right number
        if is_square(grid):
            grid[-1].append(num)

            # then fill the new right hand column, don't take into account bottom and top row
            for i in range(2, height+1):
                num += 1
                grid[-i].append(num)

        top_row = []
        for i in range(height+1):
            num+=1
            top_row.append(num)

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

        grid.append(bottom_row)
        height += 1
    return grid

def grid_location(grid, num):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==num:
                return i, j

def distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

if __name__ == "__main__":
    user_input = int(input())
    answer = generate_grid(user_input)
    print_grid(answer)
    x1, y1 = grid_location(answer, user_input)
    x2, y2 = grid_location(answer, 1)

    # 1 is always at the center of the grid, which is the height of the grid divided by 2 (integer division truncated)
    # print(len(answer)//2)

    print(distance(x1,y1,x2,y2))
    # input = 368078 answer = 371
