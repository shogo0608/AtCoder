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
    args = parse_args(['problem_no'])
    dir_path = pathlib.Path("typical90")
    assert dir_path.exists()
    file_path = pathlib.Path("typical90/" + args.problem_no + '.py')
    file_path.touch()

    dt_now = datetime.datetime.now()
    date_str = "# " + dt_now.strftime('%Y/%m/%d') + '\n\n'
    file_path.write_text(date_str)



if __name__ == '__main__':
    main()