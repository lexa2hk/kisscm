import os
import sys


# read arguments given to program
def read_args():
    args = []
    for arg in sys.argv[1:]:
        args.append(arg)
    return args

def checkline(line):
    return all(c in '01\n' for c in line)

def main(args):
    if args[0] == '-h':
        print('Usage: binAnalyzer.py <path>')
        return
    if len(args)==0:
        print('Usage: binAnalyzer.py <path>')
        return
    
    file = open(args[0], 'r')
    
    
    if all(checkline(line) for line in file.readlines()):
        print('Success')
    else:
        print('Failure')
    
    return 0

if __name__ == '__main__':
    main(read_args())