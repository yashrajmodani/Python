

def merge_files(file_list, output_file):
    unique_lines = set()

    for file in file_list:
        with open(file, 'r',encoding='utf-8') as f:
            unique_lines.update(f.read().splitlines())

    unique_lines = sorted(list(unique_lines))

    with open(output_file, 'w',encoding = 'utf-8') as f:
        for line in unique_lines:
            f.write(line + '\n')

file_list = ['file1.txt', 'file2.txt', 'file3.txt']
output_file = 'merged_file.txt'

merge_files(file_list, output_file)