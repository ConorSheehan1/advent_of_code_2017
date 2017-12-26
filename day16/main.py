import string

def clean_data(data):
    instructions = []
    for line in data:
        instructions.extend(line.split(","))
    return instructions

def part1(instructions, letters=[c for c in string.ascii_lowercase[:16]]):
    for instruction in instructions:
        if instruction[0] == "s":
            # move n letters to front of list
            num = int(instruction[1:])
            letters = letters[-num:] + letters[:len(letters)-num]
        elif instruction[0] == "x":
            # swap two letters at position xa/b
            a,b = list(map(int, instruction[1:].split("/")))
            letters[a], letters[b] = letters[b], letters[a]   
        elif instruction[0] == "p":
            namea, nameb = instruction[1:].split("/")
            a = letters.index(namea)
            b = letters.index(nameb)
            letters[a], letters[b] = letters[b], letters[a]
    return "".join(letters)


def part2(instructions):
    count = 0
    letters = string.ascii_lowercase[:16]
    seen = [letters[:]]
    while True:
        tmp = part1(instructions, [v for v in letters], part2=True)
        letters = tmp
        # break as soon as cycle starts
        if letters in seen:
            break
        seen.append(letters)
        count += 1
    return seen[1000000000%len(seen)]
