import Node
import Edge
import Graph
import random

g = Graph.Graph()

for i in range(10):
    name = "a%d" % i
    n = Node.AbsNode(random.randint(0,10),random.randint(0,10),name,\
            shape="diamond")
    g._nodelist.add_node(n)

for i in range(10):
    e = g._nodelist.generate_random_edge()
    g._edgelist.add_edge(e)

for i in range(2):
    e = g._nodelist.generate_random_loop()
    g._edgelist.add_edge(e)

print g.get_tikz()
