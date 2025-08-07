import argparse

from gendiff.gendiff import generate_diff


def main():
    # Creating agruments parser
    parser = argparse.ArgumentParser(
                        prog='gendiff',
                        description='Compares two configuration files '
                        'and shows a difference.')

    # Arguments
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # Options
    parser.add_argument('-f', '--format', help='set format of output')

    # Arguments parsing
    args = parser.parse_args()

    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()