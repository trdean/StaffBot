import Node
import Edge

class Graph:
    '''
    TODO: Add intefaces to return or manipulate lists
    '''
    _edgelist = None 
    _nodelist = None

    _header = '''\documentclass{article}
\usepackage{graphics,tikz,tkz-graph}
\usetikzlibrary{shapes}
\\tikzset{EdgeStyle/.append style = {->, bend left}}
\\begin{document}
\\begin{tikzpicture}\n'''
    _formating_options = ''
    _footer = '''\end{tikzpicture}\n\end{document}'''

    def __init__(self):
        self._edgelist = Edge.EdgeList()
        self._nodelist = Node.NodeList()

    def add_formating_option(self, option):
        pass

    def get_tikz(self):
        output = self._header + self._formating_options
        output += self._nodelist.get_tikz()
        output += self._edgelist.get_tikz()
        #Redraw the nodes so they sit on top of the edges
        output += self._nodelist.get_tikz()
        output += self._footer
        return output
