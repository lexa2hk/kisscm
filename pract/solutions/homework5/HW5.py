import graphviz
import os

def parseString(str):
    last_el = " "+" ".join(str[6:])
    [str.pop() for i in range(6,len(str))]
    str.append(last_el[1:])
    return str

def createGraph(graph, path):
    file=open(path,'r')
    current_branch=os.path.basename(file.name)
    if current_branch=="master":
        list=parseString(file.readline()[:-1].split())
        graph.node(list[1],label=list[6]+" ("+current_branch+")")
    else:
        file.readline()

    while(1):
        line=file.readline()
        if not line:
            break
        list=parseString(line[:-1].split())
        graph.node(list[1],label=list[6]+" ("+current_branch+")")
        graph.edge(list[0],list[1])

        if list[6].find('merge')!=-1:
            arr=list[6].split()
            childname=arr[1][:-1]
            last_slash=path.rfind('/')
            path2=path[:-(len(path)-last_slash)+1]+childname
            file2=open(path2,'r')
            for readLine in file2:
                pass
            parent=parseString(readLine.split())[1] #last lane

            graph.edge(parent,list[1])

def main():
    print('Path to project: ', end='')
    path_commits=input().replace("\\","/") + '/.git/logs/refs/heads'

    dot = graphviz.Digraph('Graph')
    for filename in os.listdir(path_commits):
        f=os.path.join(path_commits,filename)

        if os.path.isfile(f):
            f=str(f).replace("\\",'/')
            createGraph(dot, f)
    dot.render("test.gv", view=True)

if __name__=="__main__":
    main()