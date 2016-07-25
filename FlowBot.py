import Node, Edge, Graph
import random

branch_depth = 0
chart_depth = 0
branch_prob = [0.25, 0.1, 0]
merge_prob = [0, 0.2, 0.2]
recurse_prob = 0.3

g = Graph.Graph(bend_arrows=False)

n = Node.ParentRelNode("c0", shape="rectangle", color="white", text="Parent")
g._nodelist.add_node(n)

while chart_depth < 9:
    name = "c%d" % (chart_depth+1)
    text = "Child %d,%d" % (chart_depth, branch_depth)
    location = "below=1cm of c%d.south" % (chart_depth)

    if random.random() < branch_prob[branch_depth]:
        shape = "diamond"
        n = Node.RelNode(location,name, shape=shape, color="white",text=text)
        g._nodelist.add_node(n)

        if random.random() < recurse_prob and chart_depth > 0:
            end = random.randint(0,chart_depth-1)
            e =\
            Edge.Edge(g._nodelist[chart_depth+1],g._nodelist[end],\
            options='bend left',start_anchor='west',end_anchor='west')
            g._edgelist.add_edge(e)
    else:
        shape = "rectangle"
        n = Node.RelNode(location,name, shape=shape, color="white",text=text)
        g._nodelist.add_node(n)

    chart_depth += 1

for i in range(len(g._nodelist[:-1])):
    e = Edge.Edge(g._nodelist[i], g._nodelist[i+1])
    g._edgelist.add_edge(e)

print g.get_tikz()
