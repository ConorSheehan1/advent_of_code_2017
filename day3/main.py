'''
for day 3 the input is the same for both parts
to test this script run it directly
'''


class SpiralGrid:
    def __init__(self, min_num_in_grid):
        '''
        generate a spiral grid of numbers as a 2d list
        which contains min_num_in_grid
        '''
        self.num = 1
        self.height = 1
        self.grid = [[1]]
        while self.num < min_num_in_grid:
            self.fill_right_column()
            self.fill_top_row()
            self.fill_left_column()
            self.fill_bottom_row()

    def __repr__(self):
        space_size = len(str(self.grid[-1][-1])) + 2
        output_string = ""
        for row in self.grid:
            to_format = "{:" + str(space_size) + "}"
            for number in row:
                output_string += to_format.format(number)
            output_string += "\n"
        return output_string

    def fill_right_column(self):
        for i in range(1, self.height+1):
            self.num+=1
            self.grid[-i].append(self.num)

    def fill_left_column(self):
        for i in range(self.height):
            self.num += 1
            self.grid[i].insert(0, self.num)

    def fill_top_row(self):
        top_row = []
        for i in range(self.height+1):
            self.num+=1
            top_row.append(self.num)
        self.grid.insert(0, top_row[::-1])
        self.height += 1

    def fill_bottom_row(self):
        bottom_row = []
        for i in range(self.height+1):
            self.num+=1
            bottom_row.append(self.num)
        self.grid.append(bottom_row)
        self.height += 1

    def get_location(self, number):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j]==number:
                    return i, j


class SpiralSumGrid(SpiralGrid):
    def __init__(self, min_num_in_grid):
        super().__init__(min_num_in_grid)
        self.trav_order = self.get_traversal_order()
        self.min_num_in_grid = min_num_in_grid

    def get_traversal_order(self):
        # get the index of each number in the grid
        indexes = [self.get_location(num) for num in range(1, self.grid[-1][-1]+1)]
        # remove any index that returns none because it's not in the grid
        return [tup for tup in indexes if tup]


    def spiral_sum(self):
        # formatted_indexes = self.get_traversal_order()

        # set the grid to all 0s
        self.grid = [[0]*self.height for _ in range(self.height)]

        # put one at the center
        mid_index = self.height//2 
        self.grid[mid_index][mid_index] = 1

        for index in self.trav_order:
            y,x = index
            replacement_num = self.get_sum(index)
            if self.get_sum(index) > self.min_num_in_grid:
                return replacement_num

            print(replacement_num, self.min_num_in_grid)
            self.grid[y][x] = replacement_num

    def get_sum(self, index):
        # get all indexes adjacent to one passed and add their values together
        total = 0
        indexes_to_check = []
        for y in range(index[0]-1, index[0]+2):
            for x in range(index[1]-1, index[1]+2):
                if y >= 0 and x >= 0:
                    indexes_to_check.append([y,x])
        for l in indexes_to_check:
            try:
                total += self.grid[l[0]][l[1]]
            except IndexError:
                pass
                # if index isn't in grid, skip it
        return total

    # def get_location_gt(self, number):
    #     for index in self.trav_order:
    #         if self.grid[index[0]][index[1]] > number:
    #             return index



def clean_data(data):
    return int(data[0])

def distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def part1(data):
    grid = SpiralGrid(data)    
    x1, y1 = grid.get_location(data)
    x2, y2 = grid.get_location(1)
    return distance(x1,y1,x2,y2)


def part2(data):
    print(data)
    grid = SpiralSumGrid(data)
    print(grid)
    return grid.spiral_sum()



if __name__ == "__main__":
    user_input = int(input("number to search grid for: "))
    grid = SpiralSumGrid(user_input)
    print(grid, grid.spiral_sum())
    # print(grid)

    # print(grid.get_location_gt(user_input))