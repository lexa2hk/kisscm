# Написать на выбранном вами языке программирования программу, которая принимает в качестве аргумента командной строки имя пакета, а возвращает граф его зависимостей в виде текста на языке Graphviz.
# На выбор: для npm или для pip. Пользоваться самими этими менеджерами пакетов запрещено. Главное, чтобы программа работала даже с неустановленными пакетами и без использования pip/npm.


import os
import sys
import requests
import graphviz as gv
import pydot

os.system("pip3 show {} > mpl.txt".format('matplotlib'))
file = open('mpl.txt', 'r').readlines()
line = file[8]
info = line.split()[1:]
arr = [i[:-1] for i in info]
dot = gv.Digraph(comment='Dependencies of {}'.format('matplotlib'))
dot.node('matplotlib','matplotlib')
for dep in arr:
    dot.node(dep, dep)
    dot.edge('matplotlib', dep)

dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
(graph,) = pydot.graph_from_dot_file('test-output/round-table.gv')
graph.write_png('test-output/round-table.png')