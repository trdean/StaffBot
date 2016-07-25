import Node
import Edge
import Graph
import random

g = Graph.Graph()

shapes = ["diamond","rectangle","circle"]
colors = ["blue!20", "red!20", "none"]
labels = ["Withdraw", "Endstate", "Aviation", "FPOL", "ADA", "Coordinate",\
        "Assess", "Threat CoA", "Civil Considerations", "Evaluate", "DCPIM",\
        "Dispersed Attack", "Defense In Depth"]
for i in range(10):
    name = "a%d" % i
    n = Node.AbsNode(random.randint(0,12),random.randint(0,14),name,\
            shape=random.choice(shapes),color=random.choice(colors),\
            text=random.choice(labels))
    g._nodelist.add_node(n)

for i in range(13):
    e = g._nodelist.generate_random_edge()
    g._edgelist.add_edge(e)

for i in range(2):
    e = g._nodelist.generate_random_loop()
    g._edgelist.add_edge(e)

g._edgelist.fix_edges(g._nodelist)

print g.get_tikz()
