import sys
import importlib
import time

class AocUtil:
    @staticmethod
    def read_data(input_file_name):
        with open("{}".format(input_file_name)) as input_file:
            # read lines and remove new line chars
            return  list(map(lambda x: x.replace("\n", ""), input_file.readlines()))

    @staticmethod
    def write_data(data, method):
        output_file_name = "{}_{}.{}".format(method, time.strftime("%Y-%m-%d_%H_%M"), "txt")
        with open(output_file_name, "w") as out_file:
            out_file.write(str(data))

    @staticmethod
    def run(method, input_file_name="input.txt", write_output=False):
        print("method: {}".format(method, method))
        '''
        method:          string: name of method to call (for part one or two)
        input_file_name: string: name of file containing data (used to read test files as well as real input)
        write_output:    bool:   option to output of method to file to target_folder
        '''
        data = AocUtil.read_data(input_file_name)
        # print(locals(), globals())
        output = locals()["main."+method](data)
        if write_output:
            AocUtil.write_data(output, method.__name__)
        else:
            print(output)

    @staticmethod
    def handle_args():
        # unpack additional args and pass to main function
        AocUtil.run(*sys.argv[1:])
