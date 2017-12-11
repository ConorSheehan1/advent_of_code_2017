def clean_data(data):
    return data

def part1(data):
    lvars = []
    instructions = {'inc': "+=", 'dec':"-="}
    for line in data:
        var, instruction, amount, *condition = line.split(" ")
        if var not in lvars:
            lvars.append(var)
            exec("{} = 0".format(var))
        for v in [condition[1], condition[-1]]:
            # negative integers return false for is digit, so remove sign before checking if its a digit
            if v not in lvars and not v.lstrip("-").isdigit():
                exec("{} = 0".format(v))
                lvars.append(v)
        exec("{}: {} {} {}".format(" ".join(condition).strip(), var, instructions[instruction], amount))
    
    return eval("max([{}])".format(",".join(lvars)))

def part2(data):
    # this wouldn't work for all cases (if all numbers were negative)
    # but since I know the answer to part1 is >0 I can set current_max to 0
    current_max = 0
    lvars = []
    instructions = {'inc': "+=", 'dec':"-="}
    for line in data:
        var, instruction, amount, *condition = line.split(" ")
        if var not in lvars:
            lvars.append(var)
            exec("{} = 0".format(var))
        for v in [condition[1], condition[-1]]:
            # negative integers return false for is digit, so remove sign before checking if its a digit
            if v not in lvars and not v.lstrip("-").isdigit():
                exec("{} = 0".format(v))
                lvars.append(v)
        exec("{}: {} {} {}".format(" ".join(condition).strip(), var, instructions[instruction], amount))
        new_max =  eval("max([{}])".format(",".join(lvars)))
        if new_max > current_max:
            current_max = new_max
    return current_max