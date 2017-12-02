# advent of code 2017

Each day has its own python module, which contains a main script and input data.  
run_day.py reads and formats input data, then sends it to the main script for a given day.

* Usage:
    ```
    python run_day.py $target_folder, $method, $input_file_name, $write_output
    ```

* Example:
    ```
    python run_day.py day1, part1, input.txt, True
    ```

    The only required parameter is target_folder, which selects the day to be run
    ```
    python run_day.py day1
    ```

    | param           | default_value |
    |-----------------|---------------|
    | method          | "part1"       |
    | input_file_name | "input.txt"   |
    | write_output    | False         |