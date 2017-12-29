import string

def clean_data(data):
    return list(map(lambda x: x.split(" "), data))

# if it's an integer, return the integer, otherwise get the latest value put in the deque
def get_data(registers, index):
    if index[-1].isnumeric():
        return int(index)
    return registers[index]#[-1]


def part1(data):
    # every register has current and previous value so values can be recovered
    registers = {v[1]:[0] for v in data if v[1] in string.ascii_lowercase}
    played = []

    ci = 0
    while True:
        instruction = data[ci]
        if instruction[0] == "snd":
            played.append(get_data(registers, instruction[1]))
        elif instruction[0] == "set":
            set_value = get_data(registers, instruction[2])
            registers[instruction[1]].append(set_value)
        elif instruction[0] == "add":
            # in order to keep previous value, add old value to add value, then append left
            add_value = get_data(registers, instruction[2])
            add_value += registers[instruction[1]][-1]
            registers[instruction[1]].append(add_value)
        elif instruction[0] == "mul":
            mul_value = get_data(registers, instruction[2])
            mul_value *= registers[instruction[1]][-1]
            registers[instruction[1]].append(mul_value)
        elif instruction[0] == "mod":
            mod_value = get_data(registers, instruction[2])
            mod_value = registers[instruction[1]][-1] % mod_value
            registers[instruction[1]].append(mod_value)
        elif instruction[0] == "rcv":
            # if the current value is not 0, remove the latest appended value (reseting current value to previous value)
            if registers[instruction[1]][-1] != 0:
                registers[instruction[1]].pop()
                return played.pop()
        elif instruction[0] == "jgz":
            if get_data(registers, instruction[1]) > 0:
                ci += get_data(registers, instruction[2])
                # skip the normal step of increasing current position by 1
                continue
        ci += 1


class Worker():
    def __init__(self, id, inq, outq, instructions):
        self.id = id
        self.inq = inq
        self.outq = outq
        self.instructions = instructions
        self.ci = 0
        self.stopped = False
        self.send_count = 0
        self.registers = {v[1]:id for v in instructions if v[1] in string.ascii_lowercase}

    def __repr__(self):
        # return f"id: {self.id} ci: {self.ci} current instruction: {self.instructions[self.ci]}, inq {self.inq}, outq {self.outq}"
        return f"{self.id} {self.ci} {self.registers}"


    def process(self): 
        if self.ci >= len(self.instructions) -1:
            print(f"stopped {self.id} out of bounds")
            self.stopped = True
            return 

        instruction = self.instructions[self.ci]
        if instruction[0] == "set":
            set_value = get_data(self.registers, instruction[2])
            self.registers[instruction[1]] = set_value
        elif instruction[0] == "add":
            # in order to keep previous value, add old value to add value, then append left
            add_value = get_data(self.registers, instruction[2])
            add_value += self.registers[instruction[1]]
            self.registers[instruction[1]] = add_value
        elif instruction[0] == "mul":
            mul_value = get_data(self.registers, instruction[2])
            mul_value *= self.registers[instruction[1]]
            self.registers[instruction[1]] = mul_value
        elif instruction[0] == "mod":
            mod_value = get_data(self.registers, instruction[2])
            mod_value = self.registers[instruction[1]] % mod_value
            self.registers[instruction[1]] = mod_value

        elif instruction[0] == "snd":
            self.outq.append(get_data(self.registers, instruction[1]))
            self.send_count += 1
        elif instruction[0] == "rcv":
            if self.inq:
                self.registers[instruction[1]] = self.inq.pop(0)
                self.stopped = False
            else:
                self.stopped = True
                print(f"stopped {self.id} no data in inq")
                # don't increase ci, need to try this instruction again
                return
        elif instruction[0] == "jgz":
            if get_data(self.registers, instruction[1]) > 0:
                self.ci += get_data(self.registers, instruction[2])
                # skip the normal step of increasing current position by 1
                return
        self.ci += 1

def part2(data):
    q0, q1 = [], []
    w0 = Worker(0, q0, q1, data[:])
    w1 = Worker(1, q1, q0, data[:])

    while not (w0.stopped and w1.stopped):
        w0.process()
        w1.process()

    return w1.send_count

# # 127 too low
