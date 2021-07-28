"""Initialize the code."""


import pathlib
import argparse
import datetime


def parse_args(arg_list):
    parser = argparse.ArgumentParser()
    for arg in arg_list:
        parser.add_argument(arg)
    args = parser.parse_args()
    return args


def main():
    args = parse_args(['contest_name', 'problem'])
    dir_path = pathlib.Path(args.contest_name.upper())
    if not dir_path.exists():
        dir_path.mkdir()
    file_path = pathlib.Path(args.contest_name.upper() + '/' +\
        args.contest_name.lower() + '_' + args.problem.lower() + '.py')
    file_path.touch()

    dt_now = datetime.datetime.now()
    date_str = "# " + dt_now.strftime('%Y/%m/%d') + '\n\n'
    file_path.write_text(date_str)



if __name__ == '__main__':
    main()