import os
import sys


# read arguments given to program
def read_args():
    args = []
    for arg in sys.argv[1:]:
        args.append(arg)
    return args

def checkLine(line):
    lenl = len(line)

    
    if line[-1] == '\n':
        line = line[:-1]
        lenl -= 1
    
    if lenl%2 != 0 or not all(c in '(){}\n' for c in line):
        return False
    
    for i in range(0, lenl//2):
        if line[i] == '(' and line[lenl-i-1] != ')':
            return False
        if line[i] == '{' and line[lenl-i-1] != '}':
            return False
        
    return True
    
    
        

def main(args):
    if len(args)==0 or args[0] == '-h' :
        print('Usage: bracketsAnalyzer.py <path>')
        return
    
    if all(checkLine(line) for line in open(args[0], 'r').readlines()):
        print('Success')
    else:
        print('Failure')
    
    return 0

if __name__ == '__main__':
    main(read_args())