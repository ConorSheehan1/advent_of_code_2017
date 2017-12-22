import sys
sys.path.append("..")

# from day10.main import part1 as knot_hash
from day10 import main

def clean_data(data):
  return data[0]


# # count all the ones in the hashes
# def part1(data):
#   # return bin(int("a0c2017", 16))[2:]
#   # test output is 8188 not 8108
#   total = 0
#   for i in range(128):
#     current = "{}-{}".format(data, i)
#     current_hex = main.part2(current)
#     # exclud leading 0b
#     current_binary = bin(int(current_hex,16))[2:]
#     current_binary = "0" * (128 - len(current_binary)) + current_binary

#     total += current_binary.count("1")
#   return total

#8180 too low
#8188 too low

from collections import Counter
def part1(puzzleInput):
    puzzleInput = puzzleInput.strip()
    binaryString = ""
    for i in range(0,128):
        row = str(main.part2(puzzleInput+"-"+str(i)))
        binaryRow = bin(int(row, 16))[2:]
        binaryRow = "0" * (128 - len(binaryRow)) + binaryRow
        binaryString += binaryRow

    c = Counter(list(binaryString))

    # return c["1"]
    return binaryString.count("1")


# import numpy as np
# from scipy.ndimage.measurements import label

# def part1(data):
#     s = ''.join(f"{int(main.part2(f'{data}-{i}'), 16):0128b}" for i in range(128))
#     return s.count('1'), label(np.fromiter(s, dtype=int).reshape(128, 128))[1]
