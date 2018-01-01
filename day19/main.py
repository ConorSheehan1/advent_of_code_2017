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
                return True
        return False


    def get_surrounding_options(self):
        options = {}
        for d in [self.sd, self.dd]:
            for key, value in d.items():
                options[key] = self.try_get(offset=value)
        return options

    def solve(self):
        horizontal = ["left", "right"]
        vertical = ["up", "down"]
        while True:
            print(self)
            current = self.data[self.xy[1]][self.xy[0]]
            # if you hit a letter, keep going the same way
            if current.isalpha():
                self.letters.append(current)
                self.xy = self.apply_offset(offset=self.sd[self.direction])
            # if you're at a crossroads, try to keep going the same way
            elif current == "+":
                options = self.get_surrounding_options()
                if options[self.direction] != "":
                    self.xy = self.apply_offset(offset=self.sd[self.direction])
                # if you can't, try switching from vertical movement to horizontal
                # not setting up backtracking yet
                else:
                    if self.direction in vertical:
                        if self.try_get(self.sd["left"]) == "-":
                            self.direction = "left"
                        elif self.try_get(self.sd["right"]) == "-":
                            self.direction = "right"
                    elif self.direction in horizontal:
                        print("horizontal")
                        if self.try_get(self.sd["up"]) == "|":
                            self.direction = "up"
                        elif self.try_get(self.sd["down"]) == "|":
                            self.direction = "down"
                    self.xy = self.apply_offset(offset=self.sd[self.direction])

                print("cross", self.xy, self.direction)
            # if you can, keep going the same way
            elif self.can_go(self.direction):
                self.xy = self.apply_offset(self.sd[self.direction])
            else:
                break



def part1(data):
    m = Map(data)
    # print(m)
    # print(m.get_surrounding_options())
    m.solve()




