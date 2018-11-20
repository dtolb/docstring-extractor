#!/usr/bin/python

# import modules

import os
import glob
import shutil
import pprint
import sys
import getopt

CMD_HELP = 'example_find.py -i <inputfolder> -o <outputfolder>'

pp = pprint.PrettyPrinter(indent=2)


def po(o):
    pp.pprint(o)


def parse_args(argv):
    in_path = ''
    out_path = ''
    if len(argv) < 2:
        print(CMD_HELP)
        sys.exit(2)
    try:
        opts, args = getopt.getopt(argv, "hi:o:",
                                   ["ipath=", "opath="])
    except getopt.GetoptError:
        print(CMD_HELP)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(CMD_HELP)
            sys.exit()
        elif opt in ("-i", "--ipath"):
            in_path = arg
        elif opt in ("-o", "--opath"):
            out_path = arg
            print('Input path is "{}"'.format(in_path))
            print('Output path is "{}"'.format(out_path))
    input_exists = os.path.exists(in_path)
    output_writable = os.access(os.path.dirname(out_path), os.W_OK)
    # Make sure that we can read the input and write to the output
    if input_exists and output_writable:
        return (in_path, out_path)
    else:
        print('Directories not valid, please try again')
        sys.exit(2)


def leading_spaces(line):
    return len(line) - len(line.lstrip(' '))


def open_directory(dir):
    search_value = '{}/**/*.py'.format(dir)
    files = glob.iglob(search_value, recursive=True)
    return files
    # for file in files:
    #     extract_example(file)


def build_file_name(line):
    file_name = line.strip()
    file_name = file_name.replace('::', '')
    file_name = file_name.replace('Example: ', '')
    file_name = file_name.replace(' ', '_')
    file_name = file_name.lower()
    file_name = file_name + '.py'
    return file_name


def build_comment(line):
    comment = line.strip() + '\n'
    comment = comment.replace('::', ' ')
    comment = '# ' + comment
    return comment


def find_examples_from_files(files):
    examples = []
    for file in files:
        file_examples = find_examples_in_file(file)
        examples.extend(file_examples)
    return examples


def extract_example_code(line_number, content):
    line = content[line_number]
    example = build_comment(line)
    spaces = leading_spaces(line)
    is_example = True
    first_code_line = True
    j = line_number
    while is_example:
        j += 1
        next_line = content[j]
        next_line_spaces = leading_spaces(next_line)
        if next_line_spaces is 0:
            continue
        elif next_line_spaces == spaces:
            is_example = False
            continue
        elif first_code_line:
            indents = next_line_spaces
            first_code_line = False
        example = example + next_line[indents:]
    return example


def find_examples_in_file(file):
    print('Opening: {}'.format(file))
    with open(file, 'r') as f:
        content = f.readlines()
    i = 0
    examples = []
    while i < len(content):
        line = content[i]
        if line.endswith('::\n'):
            file_name = build_file_name(line)
            example = extract_example_code(i, content)
            code_example = CodeExample(example, file_name)
            examples.append(code_example)
        i += 1
    return examples


def setup_out_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_files(examples, directory):
    for e in examples:
        location = os.path.join(directory, e.file_name)
        print(location)
        with open(location, 'w') as py_file:
            py_file.write(e.content)


class CodeExample:
    """
    Python Example
    """
    def __init__(self, content, file_name):
        self.content = content
        self.file_name = file_name


def main(argv):
    in_path, out_path = parse_args(argv)
    files = open_directory(in_path)
    examples = find_examples_from_files(files)
    setup_out_folder(out_path)
    write_files(examples, out_path)


# Call the main() function to begin the program.
if __name__ == '__main__':
    main(sys.argv[1:])
