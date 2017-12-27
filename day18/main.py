import string
import multiprocessing

def clean_data(data):
    return list(map(lambda x: x.split(" "), data))

# if it's an integer, return the integer, otherwise get the latest value put in the deque
def get_data(registers, index):
    if index[-1].isnumeric():
        return int(index)
    return registers[index][-1]


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


class worker:
    def __init__(self, data, inq, outq, id):
        self.id = id        
        self.inq = inq
        self.outq = outq
        self.send_count = 0
        self.ci = 0
        self.stopped = False
        self.instructions = data
        self.registers = {v[1]:[id] for v in data if v[1] in string.ascii_lowercase}

    def __repr__(self):
        return f"process: {self.id}, stopped: {self.stopped}\nregisters: \
        {self.registers}\ncurrent_instruction: {self.instructions[self.ci]}"
    
    def process(self):
        while not self.stopped:
            print(self)
            instruction = self.instructions[self.ci]
            if instruction[0] == "set":
                set_value = get_data(self.registers, instruction[2])
                self.registers[instruction[1]].append(set_value)
            elif instruction[0] == "add":
                # in order to keep previous value, add old value to add value, then append left
                add_value = get_data(self.registers, instruction[2])
                add_value += self.registers[instruction[1]][-1]
                self.registers[instruction[1]].append(add_value)
            elif instruction[0] == "mul":
                mul_value = get_data(self.registers, instruction[2])
                mul_value *= self.registers[instruction[1]][-1]
                self.registers[instruction[1]].append(mul_value)
            elif instruction[0] == "mod":
                mod_value = get_data(self.registers, instruction[2])
                mod_value = self.registers[instruction[1]][-1] % mod_value
                self.registers[instruction[1]].append(mod_value)


            elif instruction[0] == "snd":
                self.outq.put(get_data(self.registers, instruction[1]))
                self.send_count += 1
            elif instruction[0] == "rcv":
                # add latest value in queue to register, if nothing is in queue wait
                self.stopped = True
                self.registers[instruction[1]] = self.inq.get(block=True)
                self.stopped = False
            elif instruction[0] == "jgz":
                if get_data(self.registers, instruction[1]) > 0:
                    self.ci += get_data(self.registers, instruction[2])
                    # skip the normal step of increasing current position by 1
                    continue
            self.ci += 1
        self.stopped = True

    # def self.is_waiting(self):
    #     return self.current_instruction == "rcv" and self.inq.empty()

    # def is_stopped(self):
    #     return self.instruction_idx > len(self.instruction) or self.is_waiting()

def part2(data):
    q0, q1 = multiprocessing.Queue(), multiprocessing.Queue()
    # worker one gets data from queue one and puts data in queue zero and vice versa
    w0 = worker(data, q0, q1, 0)
    w1 = worker(data, q1, q0, 1)

    p0 = multiprocessing.Process(target=w0.process)
    p1 = multiprocessing.Process(target=w1.process)
    # p.start()
    # if both queues are empty or both programs are finished, stop
    # while not(w1.stopped and w2.stopped):
    # p0.start()
    p1.start()
    # p0.join()
    p1.join()

