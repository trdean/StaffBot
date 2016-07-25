import abc
import random, math
import Edge

class NodeBase:
    __metaclass__ = abc.ABCMeta
    _shape = ''
    _color = ''
    _text = ''
    _name = ''

    _edges = []

class AbsNode(NodeBase):
    '''
    Node with absolute positioning
    '''
    _x_location = 0
    _y_location = 0

    def __init__(self, x, y, name, **kwargs):
        self._edges = []
        self._x_location = x
        self._y_location = y
        self._name = name

        if "shape" in kwargs:
            self._shape = kwargs["shape"]
        if "color" in kwargs:
            self._color = kwargs["color"]
        else:
            self._color = "none"
        if "text" in kwargs:
            self._text = kwargs["text"]

    @property
    def x(self):
        return self._x_location

    @property
    def y(self):
        return self._y_location

    def distance_from(self, other_node):
        dx = self._x_location - other_node.x
        dy = self._y_location - other_node.y
        return math.sqrt( dx**2 + dy**2 )

    def __repr__(self):
        return '\\node[draw,%s,fill=%s] (%s) at (%d, %d) {%s};\n' %\
                (self._shape, self._color, self._name, self._x_location,\
                self._y_location, self._text)

class ParentRelNode(NodeBase):
    '''
    If you're using relative positioning, you have one parent node with 
    no location
    '''

    def __repr__(self):
        return '\\node[draw,%s,%s] (%s) {%s};\n' %\
                (self._shape, self._color, self._name,\
                self._text)


class RelNode(NodeBase):
    '''
    Node with relative positioning
    '''
    _location = ''

    def __repr__(self):
        return '\\node[draw,%s,%s,%s] (%s) {%s};\n' %\
                (self._shape, self._color, self._location, self._name,\
                self._text)


class NodeList:
    '''
    TODO: Check if the graph is partitioned?
    '''
    _nodelist = []
    _variance = 1.50

    def __iter__(self):
        return iter(self._nodelist)

    def __len__(self):
        return len(self._nodelist)

    def __getitem__(self,key):
        return self._nodelist[key]

    def add_node(self, node, validate=False):
        '''
        Add node to self._nodelist.  If validate is set to true, determine if
        the node overlaps with other nodes - if it does, do not add it to the
        node list and return false.  Otherwise, add and return true
        '''
        if validate == True:
            for existing_node in self._nodelist:
                if node.distance_from(existing_node) < 3:
                    return False

        self._nodelist.append(node)
        return True

    def generate_random_edge(self,variance=_variance):
        '''
        Use rejection sampling to favor edges which are short in length. If we
        reject too many times then just accept. This should only take one to two
        iterations if the input variance is around the average distance between
        node
        '''
        new_edge = None
        for i in range(40):
            #Pick two nodes uniformly without replacement
            (start, end) = random.sample(self._nodelist, 2)

            new_edge = Edge.Edge(start, end)
            reject_criteria = random.gauss(0, variance)
            if new_edge.length() < abs(reject_criteria):
                break

        return new_edge
                

    def generate_random_loop(self):
        '''
        TODO: Be smart about the direction of the loop and the size of the loop
        by looking at the node chosen
        '''
        return Edge.Loop(random.choice(self._nodelist))

    def get_tikz(self):
        output = ''
        for node in self._nodelist:
            output += repr(node)

        return output
