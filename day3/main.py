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

class Square:
    def __init__(self, bottom, top, left, right):
        self.bottom = bottom
        self.top = top
        self.left = left
        self.right = right

    def get_coordinates(self):
        answer = []
        for y in range(self.top, self.bottom+1):
            for x in range(self.left, self.right+1):
                answer.append([y,x])
        return answer

    def move_down(self):
        self.bottom += 1
        self.top += 1

    def move_up(self):
        self.bottom-=1
        self.top -=1

    def move_left(self):
        self.left-=1
        self.right-=1

    def move_right(self):
        self.left+=1
        self.right+=1


class SpiralSumGrid(SpiralGrid):
    def spiral_sum(self):
        # get the index of each number in the grid
        indexes = [self.get_location(num) for num in range(1, self.grid[-1][-1]+1)]
        # remove any index that returns none because it's not in the grid
        formatted_indexes = [tup for tup in indexes if tup]
        # set the grid to all 0s
        self.grid = [[0]*self.height for _ in range(self.height)]

        # put one at the center
        mid_index = self.height//2 
        self.grid[mid_index][mid_index] = 1

        # print(formatted_indexes)

        # define location of square
        self.square = Square(mid_index, mid_index-1, mid_index, mid_index+1)
        print(self.square.get_coordinates())

        for index in formatted_indexes:
            print(self)
            y,x = index
            self.grid[y][x] = self.get_sum(index)
            # self.move_square(index)
            # self.grid[y][x] = self.get_square_sum()
            # if self.get_square_sum() >= 11:
            #     print("error", self.square.get_coordinates(), index)

    def get_sum(self, index):
        total = 0
        indexes_to_check = []
        for y in range(index[0]-1, index[0]+2):
            for x in range(index[1]-1, index[1]+2):
                if y >= 0 and x >= 0:
                    indexes_to_check.append([y,x])
        print(index, indexes_to_check)
        for l in indexes_to_check:
            try:
                total += self.grid[l[0]][l[1]]
            except IndexError:
                pass
                # if index isn't in grid, skip it
        return total

    def move_square(self, index):
        y,x = index
        if x > self.square.right:
            self.square.move_right()
        if x < self.square.left:
            self.square.move_left()
        if y > self.square.bottom:
            self.square.move_down()
        if y < self.square.top:
            self.square.move_up()


    def get_square_sum(self):
        answer = 0
        for index in self.square.get_coordinates():
            answer += self.grid[index[0]][index[1]]
        if answer == 22:
            print("ugh", self.square.get_coordinates())
            for index in self.square.get_coordinates():
                print(self.grid[index[0]][index[1]])
        return answer


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
    grid = SpiralSumGrid(user_input)
    # print(grid)
    grid.spiral_sum()
    print(grid)