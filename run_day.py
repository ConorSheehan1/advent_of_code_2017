import sys
import importlib
import time

'''
all days have the same input and should log the same output
use this script to load the input file and main function from the module for a given day
log out and dat/time to module folder

usage:
python run_day.py target_folder, method, input_file_name, write_output
'''


def main(target_folder, method="part1", input_file_name="input.txt", write_output=False):
    module = importlib.import_module(target_folder + ".main")

    # read the first line of the file and pass it to the main function for the given day
    with open("{}/{}".format(target_folder, input_file_name)) as input_file:
        # read lines and remove new line chars
        data = map(lambda x: x.replace("\n", ""), input_file.readlines())

    # call part 1 or part 2, apply to all lines in input_file
    output = list(map(getattr(module, method), data))
    if write_output:
        output_file_name = "{}/{}_{}.{}".format(target_folder, method, time.strftime("%Y-%m-%d_%H_%M"), "txt")
        with open(output_file_name, "w") as out_file:
            out_file.write(str(output))
    else:
        print("output:", output)


if __name__ == "__main__":
    try:
        target_folder = sys.argv[1]
    except IndexError:
        print("Please pass the name of a module to be run")
        exit()

    # unpack additional args and pass to main function
    main(target_folder, *sys.argv[2:])

