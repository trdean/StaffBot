import math
import random

class Edge:
    _start = ''
    _end = ''
    _style = ''
    
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __repr__(self):
        if self._style != '':
            return "\\Edge[style=%s](%s)(%s)\n" %\
                    (self._style, self._start._name, self._end._name)
        else:
            return "\\Edge(%s)(%s)\n" %\
                    (self._start._name, self._end._name)
 


    def length(self):
        dx = self._start._x_location - self._end._x_location
        dy = self._start._y_location - self._end._y_location
        return math.sqrt( dx**2 + dy**2 )

class Loop:
    _node = ''
    _dist = ''
    _loop_dir = ''
    _side = ''

    def __init__(self, node, dist='2cm', loop_dir='SO', side='east'):
        self._node = node
        self._dist = dist
        self._loop_dir = loop_dir
        self._side = side

    def __repr__(self):
        return "\\Loop[dist=%s, dir=%s](%s.%s)\n" %\
                (self._dist, self._loop_dir, self._node._name, self._side)

class EdgeList:
    _edgelist = []

    def add_edge(self, edge):
        #Do we need to do any edge validation?
        self._edgelist.append(edge)
        try:
            edge._start._edges.append(edge)
            edge._end._edges.append(edge)
        except AttributeError:
            pass

    def fix_edges(self, nodelist, allow_partitions=True):
        '''
        Checks all nodes to see if they are degree zero and randomly
        give them an edge
        TODO: Check if the graph is partitioned
        '''
        if allow_partitions == False:
            raise NotImplementedError

        if len(nodelist) < 2:
            return 

        for node in nodelist:
            if len(node._edges) == 0:
                new = node
                while new == node:
                    new = random.choice(nodelist)
                nodelist.add_node(new)


    def get_tikz(self):
        output = ''
        for edge in self._edgelist:
            output += repr(edge)

        return output
