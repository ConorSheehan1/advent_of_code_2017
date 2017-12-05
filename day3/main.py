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
        self.grid = [[5,4,2],[10,1,1],[11,23,25]]
        self.num = 25
        self.height = 3
        while self.num < min_num_in_grid:
            self.fill_right_column()
            self.fill_top_row()
            self.fill_left_column()
            self.fill_bottom_row()

    # def get_square(self,x,y):
    #     to_sum = []
    #     for i in range(x, x+2):
    #         for j in range(y, y+2):
    #             to_sum.append(self.grid[j][i])
    #     print(to_sum)
    #     return sum(to_sum)

    def get_width(self):
        return len(min(self.grid, key=len))

    def get_square(self, y, x):
        bottom = self.grid[y][x:]
        print(bottom)        
        top = self.grid[y+1][x:]
        print(top)
        return sum(bottom + top)

    def fill_right_column(self):
        for i in range(1, self.height+1):
            y = -i
            x = self.get_width()-2
            self.num=self.get_square(x,y)
            self.grid[-i].append(self.num)  



# class SpiralSumGrid(SpiralGrid):
#     def get_width(self):
#         return len(max(self.grid, key=len))

#     def normalize_index(self, yx):
#         '''
#         xy is list or tuple of coordinates [x,y]
#         '''
#         # x is already negative so add it to the width of the grid to get real offset
#         y,x = yx
#         # print(x,y)
#         if x < 0:
#             x +=  self.get_width()+1#len(self.grid[0])
#         if y < 0:
#             y += self.height
#         print(y, x, yx, self.height, len(max(self.grid, key=len))+1)
#         return x,y 

#     def get_unique_grid_indexes(self, indexes):
#         unique_indexes = set()
#         for coords in indexes:
#             unique_indexes.add(self.normalize_index(coords))
#         return unique_indexes

#     def get_right_square(self, y):
#         to_sum = []
#         indexes = []
#         width_of_square = self.get_width()
#         if width_of_square > 2:
#             width_of_square = 2
#         # get current row and one row above if it exists
#         for i in range(y,self.height)[:2]:
#             # get last two values for each row
#             for j in range(-width_of_square, 0):
#                 indexes.append([i,j])
#         unique_indexes = self.get_unique_grid_indexes(indexes)
#         return unique_indexes

#     def fill_right_column(self):
#         for i in range(1, self.height+1):
#             print(self.get_right_square(-i))
#             self.num+=1
#             self.grid[-i].append(self.num)


def clean_data(data):
    return int(data[0])

def distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def part1(data):
    grid = SpiralGrid(data)    
    x1, y1 = grid.get_location(data)
    x2, y2 = grid.get_location(1)
    return distance(x1,y1,x2,y2)


if __name__ == "__main__":
    user_input = int(input("number to search grid for: "))

    # grid = SpiralGrid(user_input)
    # print(grid)

    # x1, y1 = grid.get_location(user_input)
    # x2, y2 = grid.get_location(1)

    # # 1 is always at the center of the grid, which is the height of the grid divided by 2 (integer division truncated)
    # # print(grid.height//2, x2, y2)

    # print("distance from {} to 1: ".format(user_input), distance(x1,y1,x2,y2))
    # # input = 368078 answer = 371

    grid = SpiralSumGrid(user_input)
    print(grid)


# [(0,-2), (0-1)]
# [(1,-2), (1, -1)]