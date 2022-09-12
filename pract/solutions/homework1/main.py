# pws la cd cat
from ast import Try
from re import T
import zipfile
import os
import sys

# read arguments given to program
def read_args():
    args = []
    for arg in sys.argv[1:]:
        args.append(arg)
    return args

# array of tuples of path and list of files in that path
def deflatten(names):
    names.sort(key=lambda name:len(name.split('/')))
    deflattened = []
    while len(names) > 0:
        name = names[0]
        if name[-1] == '/':
            subnames = [subname[len(name):] for subname in names if subname.startswith(name) and subname != name]
            for subname in subnames:
                names.remove(name+subname)
            deflattened.append((name, deflatten(subnames)))
        else:
            deflattened.append(name)
        names.remove(name)
    return deflattened


def ls1(deflattened, path):
    for name in deflattened:
        print(name[0])
        print(path)
        if name[0][:-1:] == path:
            print(name[0])
            ls1(name[1], path)
    

#parse deflattened list of names to find specific file
def ls(names, file1, recurse=False):
    result = []

    if file1 == "":
        for name in names:
            print(name[0])
    else:
        path = file1.split('/')
        cnt_path = 0

        for name in names:
            if name[0][:-1:] == path[cnt_path]:
                if cnt_path == len(path)-1:
                    result.append(name)
                else:
                    cnt_path += 1
                    ls(name[1], '/'.join(path[cnt_path:]), True)
    
    for name in result:
        for i in name[1]:
            if type(i)==tuple:
                print(i[0])
            else:
                print(i)
    
    return result


# vshell emulation
def vshell(zip_file):
    try:
        zip_file = zipfile.ZipFile(zip_file)
        deflattened = deflatten(zip_file.namelist())
        # emulate shell inside of zip file
        curdir = ""
        while True:

            path = zipfile.Path(zip_file, curdir)
            command = input("vs /"+ curdir +" > ")
            if command == "exit":
                break
            elif command == "":
                continue
            elif command == "pwd":
                if curdir == "":
                    print("/")
                else:
                    print("/" + curdir)
            elif command.split()[0] == "cd":
                if command.split()[1] == "..":
                    if curdir == "/":
                        continue
                    else:
                        temp = curdir.split('/')
                        curdir = curdir[:-len(temp[-1])-1]
                else:
                    if curdir == "":
                        curdir = command.split()[1]
                    else:
                        curdir += '/' + command.split()[1]
                    
            elif command.split()[0] == 'cat':
                for i in list(zip_file.open(curdir + '/' + command.split()[1], mode="r").read()):
                    print(chr(i), end='')
                print()
                
            elif command == "ls":
                # print(deflattened)
                ls(deflattened, curdir)
            else:
                print("Invalid command")
    except FileNotFoundError:
        print("File not found")
        return
    except EOFError:
        print("EOF")
        return
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        return
    except Exception as e:
        print(e)
        return
    
    

# open zip file given as argument 1
def main(args):
    if len(args) == 0:
        print("No arguments given")
        return
    elif len(args) == 1:
        print("No zip file given")
        print("Usage: python main.py -zip <zipfile>")
        return
    elif len(args) > 2 and args[0] != "-zip":
        print("Invalid arguments given")
        print("Usage: python main.py -zip <zipfile>")
        return
    elif len(args) == 2 and args[0] == "-zip":
        zip_file = args[1]
        if not zipfile.is_zipfile(zip_file):
            print("Invalid zip file given")
            return
        else:
            print("Opening zip file: " + zip_file)
            vshell(zip_file)
            return
    else:
        print("Invalid arguments given")
        print("Usage: python main.py -zip <zipfile>")
        return



if __name__ == '__main__':
    main(read_args())