# Написать на выбранном вами языке программирования программу, которая принимает в качестве аргумента командной строки имя пакета, а возвращает граф его зависимостей в виде текста на языке Graphviz.
# На выбор: для npm или для pip. Пользоваться самими этими менеджерами пакетов запрещено. Главное, чтобы программа работала даже с неустановленными пакетами и без использования pip/npm.


import os
import sys
import requests
import graphviz as gv
import pydot


# read arguments given to program
def read_args():
    args = []
    for arg in sys.argv[1:]:
        args.append(arg)
    return args

def get_dependencies(package_name) -> list:
    url = 'https://pypi.org/pypi/{}/json'
    json = requests.get(url.format(package_name)).json()
    try:
        requirements = json['info']['requires_dist']
    except:
        return []
    data = []
    if requirements is not None:
        for req in requirements:
            data.append(req.split(' ')[0])
    return data



def build_graph_right(name, deps):
    dot = gv.Digraph(comment='Dependencies of {}'.format(name))
    dot.node(name,name)
    for dep in deps:
        dot.node(dep, dep)
        dot.edge(name, dep)
    
    dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
    (graph,) = pydot.graph_from_dot_file('test-output/round-table.gv')
    graph.write_png('test-output/round-table.png')
        
    print(dot.source)
    
def build_graph(name, deps):
    dot = gv.Digraph(comment='Dependencies of {}'.format(name))
    dot.node('A',name)
    i = 'B'
    for dep in deps:
        dot.node(i, dep)
        i=chr(ord(i)+1)
    
    i='B'
    for dep in deps:
        dot.edge('A',i)
        i=chr(ord(i)+1)
    dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
    (graph,) = pydot.graph_from_dot_file('test-output/round-table.gv')
    graph.write_png('test-output/round-table.png')
        
    print(dot.source)
        

deptree = []
def parse_deps(deps: list,first: bool = True):
    print(deps.__len__())
    if(deps.__len__() != 0):
        for dep in deps:
            deptree.append((dep, get_dependencies(dep)))


def recursiveNodes(graph,name,depth=0):
    deps = get_dependencies(name)
    
    if(deps.__len__() == 0 or depth > 1):
        return
    for dep in deps:
        graph.node(dep, dep)
        graph.edge(name, dep)
        recursiveNodes(graph,dep,depth+1)

def main(args):
    if len(args) == 0:
        print("No package name given")
        return
    
    dot = gv.Digraph(comment='Dependencies of {}'.format(args[0]))
    dot.node(args[0],args[0])
    
    recursiveNodes(dot,args[0])
    
    dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
    (graph,) = pydot.graph_from_dot_file('test-output/round-table.gv')
    graph.write_png('test-output/round-table.png')
    

if __name__ == "__main__":
    main(read_args())