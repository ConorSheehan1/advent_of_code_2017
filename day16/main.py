import string

def clean_data(data):
    instructions = []
    for line in data:
        instructions.extend(line.split(","))
    return instructions

def part1(instructions, letters=[c for c in string.ascii_lowercase[:16]]):
    # # test input
    # letters = [c for c in string.ascii_lowercase[:5]]
    for instruction in instructions:
        if instruction[0] == "s":
            # move n letters to front of list
            num = int(instruction[1:])
            letters = letters[-num:] + letters[:len(letters)-num]
        if instruction[0] == "x":
            # swap two letters at position xa/b
            a,b = list(map(int, instruction[1:].split("/")))
            letters[a], letters[b] = letters[b], letters[a]   
        if instruction[0] == "p":
            namea, nameb = instruction[1:].split("/")
            indexa = letters.index(namea)
            indexb = letters.index(nameb)
            letters[indexa], letters[indexb] =  letters[indexb], letters[indexa]
    return "".join(letters)

def part2(instructions):
    # l = 0
    letters = [c for c in string.ascii_lowercase[:16]]
    for i in range(1000000000):
        # if len(str(i)) > l:
        #     print(i)
        #     l+=1
        tmp = part1(instructions, letters)
        letters = [c for c in tmp]
    return "".join(letters)

