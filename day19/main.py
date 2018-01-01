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
        self.map_paths = {
                            "|":self.vertical + [v*2 for v in self.vertical],
                             "-":self.horizontal + [v*2 for v in self.horizontal], 
                             "+":list(self.sd.keys())
                        }

        # set up limits for the map
        self.xlimit = len(data[0])
        self.ylimit = len(data)

        self.steps = 0

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

    # using possible new location
    def could_go(self, direction):
        directions = dict(self.sd, **self.dd)
        print(directions[direction], direction)
        next_char = self.try_get(directions[direction])
        if next_char.isalpha():
            return True
        for k, v in self.map_paths.items():
            if direction in v and k == next_char:
                print("returning true")
                return True
        print("returning false")
        return False


    def get_options(self, d):
        # pass self.sd to get close options, self.dd to get far options
        options = {}
        for key, value in d.items():
            options[key] = self.try_get(offset=value)
        return options

    def try_other(self, directions):
        for direction in directions:
            if self.could_go(direction):
                return direction

    def could_jump(self, direction):
        if self.try_get(self.sd[direction]).strip() != "":
            return self.could_go(direction*2)

    def remove_backtrack(self, dict):
        opposites = {'up':'down','down':'up','left':'right', 'right':'left'}
        return {k:v for k,v in dict.items() if k != opposites[self.direction]}


    def try_other_direction(self):
        # if you can't, try switching from vertical movement to horizontal
        # not setting up backtracking yet
        if self.direction in self.vertical:
            print("horiz")
            new_direction = self.try_other(self.horizontal)
        else:
            print("vert")
            new_direction = self.try_other(self.vertical)

        # try to jump in the same direction
        if (new_direction is None) and self.could_jump(self.direction):
            new_direction = self.direction
            # move twice to skip over the corssing line
            self.xy = self.apply_offset(offset=self.sd[self.direction])
            self.steps += 1


        self.direction = new_direction
        print("switching to", self.direction)
        self.xy = self.apply_offset(offset=self.sd[self.direction])
        self.steps += 1

    def solve(self):
        while True:
            print(self)
            self.current = self.data[self.xy[1]][self.xy[0]]
            if self.current.isalpha():
                # print(f"appending {self.current}")
                self.letters.append(self.current)

            # exit if the only way to go is back
            options = self.get_options(self.sd)
            options_without_backtrack = self.remove_backtrack(options)
            if all([v.strip()=="" for v in options_without_backtrack.values()]):
                # print("exiting")
                break

            # if you can, keep going the same way
            if self.could_go(self.direction):
                # print("continuing")
                self.xy = self.apply_offset(offset=self.sd[self.direction])
                self.steps += 1
            else:
                # print("changing")
                self.try_other_direction()



def part1(data):
    m = Map(data)
    m.solve()
    return "".join(m.letters)


def part2(data):
    m = Map(data)
    m.solve()
    return m.steps+1




