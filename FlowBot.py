import Node, Edge, Graph, Matrix, WordChoice
import random

branch_depth = 1
chart_depth = 0
branch_prob = [0, 0.3, 0.20, 0]
merge_prob = [0, 0.2, 0.2]
recurse_left_prob = 0.5
recurse_right_prob = 0.5

g = Graph.Graph(bend_arrows=False)

n = Node.ParentRelNode("c0b0", shape="rectangle", color="white", text="Parent")
g._nodelist.add_node(n)

m = Matrix.Matrix()
output = '\documentclass{article}\n'
output += '\usepackage{graphics,tikz,tkz-graph}\n'
output += '\usetikzlibrary{shapes}\n'
output += '\usetikzlibrary{positioning}\n'
output += '\usetikzlibrary{matrix}\n'
output += '\\begin{document}\n'
output += '\\begin{tikzpicture}[\n'
output += 'start/.style={draw, rectangle, rounded corners=1.5ex, fill=white},\n'
output += 'end/.style={draw, rectangle, rounded corners=1.5ex, fill=white},\n'
output += 'decision/.style={draw, diamond, fill=blue!20},\n'
output += 'state/.style={draw, rectangle, rounded corners=0.8ex, fill=green!20},\n'
output += 'block/.style={draw,trapezium, trapezium left angle=70,\
trapezium right angle=-70, fill=red!20},\n'
output += 'line/.style={draw, -latex\'}]\n'
output += '\\matrix [column sep=1cm, row sep=1cm] {\n'
for i, row in enumerate(m.matrix):
    for j,node in enumerate(row):
        if node != '':
            word = WordChoice.pick_word(node)
            output += "\\node[%s] (%db%d) {%s}; " % (node, i,j, word)

        if j != len(row) - 1:
            output += "& "
    output += "\\\\\n"

output += '};\n'

for i, row in enumerate(m.matrix[1:]):
    #First row must have stuff in every square
    output += "\path [line] (%db%d) -- (%db%d);\n" % (i,0,i+1,0)
    for j, node in enumerate(row[1:]):
        if node == '':
            if m.matrix[i][j+1] != '':
                next_box = m.row_width(i+1)
                output += "\path [line] (%db%d) |- (%db%d);\n" %\
                (i,j+1,i+1,next_box)
            else:
                continue
        #j is index minus one since list is sliced from 1:
        if row[j] == 'decision':
            output += "\path [line] (%db%d) -- (%db%d);\n" % (i+1,j,i+1,j+1)
        if m.matrix[i][j+1] != '' and row[j+1] != '':
            output += "\path [line] (%db%d) -- (%db%d);\n" % (i,j+1,i+1,j+1)
            
#draw bottom arrows
for i, node in enumerate(m.matrix[-2][1:]):
    if node != '':
        output += "\path [line] (%db%d) |- (%db%d);\n" % \
                (len(m.matrix)-2,i+1,len(m.matrix)-1,0)

#Pick arrows going backwards
if random.random() < recurse_left_prob:
    first_decision = -1
    for i, row in enumerate(m.matrix):
        if row[0] == "decision":
            first_decision = i

    #case 1: no branches, pick random recursion
    if first_decision == -1:
        nodes = random.sample(range(1,len(m.matrix)),2)
        nodes.sort()
        output += "\path [line] (%db0) -- ++(-2,0) |- (%db0);\n" % (nodes[1],\
                nodes[0]) 
    else:
        #pick recursion on left, start below last branch, end above first branch
        end = 1
        if first_decision != 1:
            end = random.choice(range(1,first_decision))
        if first_decision == (len(m.matrix) - 1):
            start = first_decision
        else:
            start = random.choice(range(first_decision, len(m.matrix)-1))
        output += "\path [line] (%db0) -- ++(-2,0) |- (%db0);\n" % (start,\
                end) 

#Now do the same from the right side
if random.random() < recurse_right_prob:
    column = m.node_width
    c_start = m.column_start(column)
    c_end = m.column_end(column)

    start = random.choice(range(c_start,c_end))
    start_column = m.row_width(start)
    if start != 1:
        end = random.choice(range(1,start))
        end_column = m.row_width(end)
        output += "\path [line] (%db%d) -- ++(%d,0) |- (%db%d);\n" % \
                (start,start_column,column+1, end, end_column)


output += '\\end{tikzpicture}\n\\end{document}\n'
print output
