def clean_data(data):
    return data

class Map:
    def __init__(self, data):
        self.data = data
        self.direction = "down"
        self.letters = []

        # single directions
        self.sd = {"up":[0, -1], "down":[0, 1], "left":[-1, 0], "right":[1, 0]}
        # double directions
        self.dd = {k*2:list(map(lambda x: x*2, v)) for k,v in self.sd.items()}

        self.horizontal = ["left", "right"]
        self.vertical = ["up", "down"]

        # starting point is the only charater in the first line that isn't white space
        start_char = data[0].strip() 
        self.xy = [data[0].index(start_char), 0]

        # current character in map diagram
        self.current = self.data[self.xy[1]][self.xy[0]]
        self.map_paths = {"|":["up", "down"], "-":["left", "right"], "+":list(self.sd.keys())}

        # set up limits for the map
        self.xlimit = len(data[0])
        self.ylimit = len(data)

    def __repr__(self):
        return f"{self.direction} current {self.data[self.xy[1]][self.xy[0]]} xy: {self.xy} letters: {self.letters}"

    def apply_offset(self, offset=[0,0]):
        return list(map(lambda x: sum(x), zip(self.xy, offset)))

    def try_get(self, offset):
        # add the offset to the current position
        xy = self.apply_offset(offset)
        # return character at index self.xy and offset
        if (0 <= xy[0] < self.xlimit) and (0 <= xy[1] < self.ylimit):
            return self.data[xy[1]][xy[0]]
        # if the index is out of bounds, return Empty string
        return ""

    # using current location
    def can_go(self, direction):
        return (direction in self.map_paths[self.current]) or self.current.isalpha()

    # using possible new location
    def could_go(self, direction):
        next_char = self.try_get(self.sd[direction])
        if next_char.isalpha():
            return True
        for k, v in self.map_paths.items():
            if direction in v and k == next_char:
                print("could_go", direction, v, k, next_char)
                return True
        return False


    def get_surrounding_options(self):
        options = {}
        for d in [self.sd, self.dd]:
            for key, value in d.items():
                options[key] = self.try_get(offset=value)
        return options

    def try_other(self, directions):
        for direction in directions:
            if self.could_go(direction):
                return direction


    def try_other_direction(self):
        if self.direction in self.vertical:
            self.direction = self.try_other(self.horizontal)
        else:
            self.direction = self.try_get(self.vertical)
        self.xy = self.apply_offset(offset=self.sd[self.direction])

    def solve(self):
        while True:
            print(self)
            self.current = self.data[self.xy[1]][self.xy[0]]
            # if you hit a letter, keep going the same way
            if self.current.isalpha():
                self.letters.append(self.current)
                self.xy = self.apply_offset(offset=self.sd[self.direction])
            # if you're at a crossroads
            elif self.current == "+":
                options = self.get_surrounding_options()
                # try to keep going the same way
                if options[self.direction].strip() != "":
                    print("cross same", options[self.direction])
                    print(options)
                    self.xy = self.apply_offset(offset=self.sd[self.direction])
                # if you can't, try switching from vertical movement to horizontal
                # not setting up backtracking yet
                else:
                    print("cross different")
                    self.try_other_direction()
                    # if self.direction in vertical:
                    #     for direction in horizontal:
                    #         if self.could_go(direction):
                    #             self.direction = direction
                    # elif self.direction in horizontal:
                    #     for direction in vertical:
                    #         if self.could_go(direction):
                    #             self.direction = direction
                    # self.xy = self.apply_offset(offset=self.sd[self.direction])

                # print("cross", self.xy, self.direction)
            # if you can, keep going the same way
            elif self.could_go(self.direction):
                print("can go")
                self.xy = self.apply_offset(offset=self.sd[self.direction])
            else:
                # break

                self.try_other_direction()
                # print("cant", direction, self.can_go(self.direction), )
                # if self.direction in vertical:
                #     print("vert")
                #     for direction in horizontal:
                #         if self.could_go(direction):
                #             self.direction = direction
                #             break
                # elif self.direction in horizontal:
                #     print("horiz")
                #     for direction in vertical:
                #         if self.could_go(direction):
                #             print("could go", direction)
                #             self.direction = direction
                #             break
                #     else:
                #         print("fail")

                # self.xy = self.apply_offset(offset=self.sd[self.direction])



def part1(data):
    m = Map(data)
    # print(m)
    # print(m.get_surrounding_options())
    m.solve()




