import sys,random

front_matter = """\documentclass{article}
\usepackage{graphics,tikz,tkz-graph}
\usetikzlibrary{shapes}
\\tikzset{EdgeStyle/.append style = {->, bend left}}
\\begin{document}
\\begin{tikzpicture}\n\n"""

back_matter = """\end{tikzpicture}
\end{document}"""

words1 = ["Intelligence", "Mission Command", "DOTMLPF", "Strategic Deterence", "Cybernetics", "JECC", "FBI", "UCP",\
        "STRATCOM", "Warfighter", "BCT", "Operational Art"]
words2 = ["Fix", "Disrupt", "Penetrate", "Isolate", "Interdict", "Breach", "Suppress", "Destroy",\
        "Planing", "Coordination", "Mass Combat Power", "Deny"]

colors = ["fill=blue!20", "fill=red!20", "fill=green!20", "fill=black!20", "fill=none"]
shapes = ["rectangle","diamond","circle","rectangle, rounded corners=0.8ex"]

document = front_matter

def make_random_node(id, x, y, label):
    node = "\\node[draw,%s,%s" % (random.choice(shapes),random.choice(colors))
    node += "] (%s) at (%d, %d) {%s};\n" % (id, x, y, label)
    return node

for i in range(5):
    document += make_random_node("x"+str(i), 2*random.randint(0,6), 2*random.randint(0,9), random.choice(words1))
    document += make_random_node("x"+str(i+5), 2*random.randint(0,6), 2*random.randint(0,9), random.choice(words2))

for i in range(10):
    a = random.randint(0,9)
    b = random.randint(0,9)

    if a == b:
        document += "\Loop[dist=2cm, dir=SO](x%d.east)\n" % a
    else:
        document += "\Edge(x%d)(x%d)\n" % (a, b)

document += back_matter

f = open(sys.argv[1], "w")
f.write(document)
