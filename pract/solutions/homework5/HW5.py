import graphviz
import os

def parseString(str):
    last_el=''
    for i in range(6,len(str)):
        last_el+=' '+str[i]

    for i in range (6,len(str)):
        str.pop()

    str.append(last_el[1:])
    return str

def createGraph(graph, path):
    file=open(path,'r')
    current_branch=os.path.basename(file.name)
    if current_branch=="master":
        str=file.readline()
        str=str[:len(str)-1]
        str=str.split()
        list=parseString(str)
        graph.node(list[1],label=list[6]+" ("+current_branch+")")
    else:
        file.readline()

    while(1):
        line=file.readline()
        if not line:
            break
        line=line[:len(line)-1]
        line=line.split()
        list=parseString(line)
        graph.node(list[1],label=list[6]+" ("+current_branch+")")
        graph.edge(list[0],list[1])

        if list[6].find('merge')!=-1:
            child=list[1]
            arr=list[6].split()
            childname=arr[1][:-1]
            last_slash=path.rfind('/')
            path2=path[:-(len(path)-last_slash)+1]+childname
            file2=open(path2,'r')
            for str in file2:
                pass
            last_line = str
            list2=parseString(last_line.split())
            parent=list2[1]

            graph.edge(parent,child)


def main():
    print('Path to project: ', end='')
    path=input()
    path=path.replace("\\","/")
    path+='/.git'

    add_path="/logs/refs/heads"

    path_commits=path+add_path

    dot = graphviz.Digraph('Graph')
    for filename in os.listdir(path_commits):
        f=os.path.join(path_commits,filename)

        if os.path.isfile(f):
            f=str(f)
            f=f.replace("\\",'/')
            createGraph(dot, f)
    dot.render("test.gv", view=True)





if __name__=="__main__":
    main()