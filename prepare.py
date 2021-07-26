"""Prepare a contest

Make a directory and some source files.
Usage:
    prepare.py CONTEST_NAME
Outputs:
    CONTEST_NAME
    ├ contest_name_a.py
    ├ contest_name_b.py
    ├ contest_name_c.py
    ├ contest_name_d.py
    ├ contest_name_e.py
    ├ contest_name_f.py
    ├ contest_name_g.py
    └ contest_name_h.py
"""


import pathlib
import argparse


def make_parser(arg_list):
    parser = argparse.ArgumentParser()
    for arg in arg_list:
        parser.add_argument(arg)
    return parser


def main():
    parser = make_parser(['contest_name'])
    args = parser.parse_args()

    dir_path = pathlib.Path(args.contest_name)
    if not dir_path.exists():
        dir_path.mkdir()

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    problems = []
    for alpha in alphabets:
        problems.append(args.contest_name.lower() + '_' + alpha + '.py')

    for file_name in problems:
        file_path = pathlib.Path(args.contest_name + '/' + file_name)
        if not file_path.exists():
            file_path.touch()


if __name__ == '__main__':
    main()
