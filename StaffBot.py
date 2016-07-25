import Node
import Edge
import Graph
import random

g = Graph.Graph()

MAX_TRIES = 20

shapes = ["diamond","rectangle","circle"]
colors = ["blue!20", "red!20", "white"]
labels = ["Withdraw", "Endstate", "Aviation", "FPOL", "ADA", "Coordinate",\
        "Assess", "Threat CoA", "Civil Considerations", "Evaluate", "DPCIM",\
        "Dispersed Attack", "Defense In Depth"]
for i in range(10):
    added = False
    for j in range(MAX_TRIES):
        name = "a%d" % i
        n = Node.AbsNode(random.randint(0,12),random.randint(0,14),name,\
                shape=random.choice(shapes),color=random.choice(colors),\
                text=random.choice(labels))
        #Trues true if the node is at least 3 distance away from any other node
        if g._nodelist.add_node(n,validate=True) == True:
            break

for i in range(11):
    e = g._nodelist.generate_random_edge()
    g._edgelist.add_edge(e)

for i in range(2):
    e = g._nodelist.generate_random_loop()
    g._edgelist.add_edge(e)

g._edgelist.fix_edges(g._nodelist)

print g.get_tikz()
