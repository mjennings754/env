def read_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()

file_path = "/Users/mitchell/env/03022026/03022026 v2/test.txt"

for line in read_file(file_path):
    print(line)