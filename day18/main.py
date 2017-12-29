import string
import multiprocessing
import time

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



    
def process(id, inq, outq, manager, instructions):  
    # multiprocessing manager dict doesn't support nested dict assignment
    # https://bugs.python.org/issue6766
    # # manager[id]["stopped"] = False 
    ci = 0
    manager[f"stopped{id}"] = False
    manager[f"send_count{id}"] = 0
    registers = {v[1]:[id] for v in instructions if v[1] in string.ascii_lowercase}
    time.sleep(1)
    while not manager[f"stopped{id}"]:
        print(id, instructions[ci])
        instruction = instructions[ci]
        if instruction[0] == "set":
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
        elif instruction[0] == "snd":
            outq.put(get_data(registers, instruction[1]))
            manager[f"send_count{id}"] += 1
        elif instruction[0] == "rcv":
            # add latest value in queue to register, if nothing is in queue wait
            manager[f"stopped{id}"] = True
            time.sleep(1)
            print(id, "stop", manager[f"stopped{id}"])
            registers[instruction[1]] = inq.get(block=True)
            print(id, "restart", manager[f"stopped{id}"])
            manager[f"stopped{id}"] = False
        elif instruction[0] == "jgz":
            if get_data(registers, instruction[1]) > 0:
                ci += get_data(registers, instruction[2])
                # skip the normal step of increasing current position by 1
                continue
        ci += 1
    manager[f"stopped{id}"] = True

def part2(data):
    q0, q1 = multiprocessing.Queue(), multiprocessing.Queue()
    manager = multiprocessing.Manager()
    stopped_dict = manager.dict()
    # worker one gets data from queue one and puts data in queue zero and vice versa
    # w0 = worker(data, q0, q1, 0)
    # w1 = worker(data, q1, q0, 1)

    p0 = multiprocessing.Process(target=process, args=(0, q0, q1, stopped_dict, data))
    p1 = multiprocessing.Process(target=process, args=(1, q1, q0, stopped_dict, data))
    # p.start()
    # if both queues are empty or both programs are finished, stop
    p0.start()
    p1.start()
    time.sleep(1)
    while not stopped_dict["stopped0"] and not stopped_dict["stopped1"]:
        print(stopped_dict["stopped0"], stopped_dict["stopped1"])
        time.sleep(2)
        pass
    print("done")
    p0.terminate()
    p1.terminate()
    return stopped_dict["send_count0"], stopped_dict["send_count1"]

# 127 too low
