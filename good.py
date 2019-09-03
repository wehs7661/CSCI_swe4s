import argparse
import sys

parser = argparse.ArgumentParser(
                                 description='The right way the pass parameters',
                                 prog='good')
# prog: the name of the program shown in the help message
# It is not necessary to be the same as the default sys.argv[0]

parser.add_argument('-f',             # shortcut
                    '--input_file',   # verbose mode (compare to only "-f")
                    type=str,
                    help='Name of the file',
                    required=True)

parser.add_argument('-c',
                    '--column_number',
                    type=str,
                    help='The column number',
                    required=True)

parser.add_argument('--op',
                    type=str,
                    help='Aggregation opperation')

args = parser.parse_args()

try:
    f = open(args.input_file)
except FileNotFoundError:
    print('Sorry, ' + args.input_file, 'could not be found.')
    sys.exit(1)    # stop the program
except PermissionError:
    print('Sorry, ' + args.input_file + 'could not be opened.')
    parser.print_help()  # print out the help message
    sys.exit(1)

raise FileNotFoundError
print('Keep going.')
