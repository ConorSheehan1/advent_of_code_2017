import sys
import importlib
import time

'''
all days have the same input and should log the same output
use this script to load the input file and main function from the module for a given day
log the output and date/time to the module folder

usage:
python run_day.py target_folder, method, input_file_name, write_output
'''


def main(target_folder, method="part1", input_file_name="input.txt", write_output=False):
    '''
    target_folder:   string: name of folder where script and data for current day is
    method:          string: name of method to call (for part one or two)
    input_file_name: string: name of file containing data (used to read test files as well as real input)
    write_output:    bool:   option to output of method to file to target_folder
    '''

    module = importlib.import_module(target_folder + ".main")
    with open("{}/{}".format(target_folder, input_file_name)) as input_file:
        # read lines and remove new line chars
        data = map(lambda x: x.replace("\n", ""), input_file.readlines())

    # call part1 or part2 method, apply function to all lines in input_file (used mainly for test input)
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
