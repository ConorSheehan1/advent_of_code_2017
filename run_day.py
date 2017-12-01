import sys
import importlib
import time

'''
all days have the same input and should log the same output
use this script to load the input file and main function from the module for a given day
log out and dat/time to module folder

usage:
python run_day.py folder_name, input_file_name
'''

try:
    target_folder = sys.argv[1]
except IndexError:
    print("Please pass the name of a module to be run")
    exit()

module = importlib.import_module(target_folder + ".main")

# for using test input
if len(sys.argv) == 3:
    file_name = sys.argv[2]
    write_output = False
# for running real input
else:
    file_name = "input.txt"
    write_output = True

# read the data file and pass it to the main function for the given day
with open("{}/{}".format(target_folder, file_name)) as input_file:
    data = input_file.readlines()

output = module.main(data)
if write_output:
    # with open("{}/{}{}{}".format(target_folder, "output", time.strftime("%Y-%m-%d_%H_%M"), ".txt"), "w") as out_file:
    #     pass
else:
    print(output)