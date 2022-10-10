import requests
import os
import sys
import graphviz as gv
import pydot

def read_args():
    args = []
    for arg in sys.argv[1:]:
        args.append(arg)
    return args

def get_dependencies() -> list:
    json = open('express.json', 'r').readlines()[1:-1]
    lines = [j.split()[0] for j in json]
    ans = []
    for line in lines:
        for c in line:
            if c in """',\n:""":
                line = line.replace(c, '')
        ans.append(line)
    return ans

def buildtree(name):
    deps = get_dependencies()
    dot = gv.Digraph(comment='Dependencies of {}'.format(name))
    dot.node(name,name)
    for dep in deps:
        dot.node(dep, dep)
        dot.edge(name, dep)
    
    dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
    (graph,) = pydot.graph_from_dot_file('test-output/round-table.gv')
    graph.write_png('test-output/round-table.png')

os.system("npm info {} dependencies > express.json".format('express'))

buildtree('express')

