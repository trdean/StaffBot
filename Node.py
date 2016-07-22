import abc
import random
import Edge

class NodeBase:
    __metaclass__ = abc.ABCMeta
    _shape = ''
    _color = ''
    _text = ''
    _name = ''

class AbsNode(NodeBase):
    '''
    Node with absolute positioning
    '''
    _x_location = 0
    _y_location = 0

    def __repr__(self):
        return '\\node[draw,%s,%s] (%s) at (%d, %d) {%s};\n' %\
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
    _nodelist = []
    _variance = 1.33

    def add_node(self, node, validate=False):
        '''
        Add node to self._nodelist.  If validate is set to true, determine if
        the node overlaps with other nodes - if it does, do not add it to the
        node list and return false.  Otherwise, add and return true
        '''
        if validate == True:
            raise NotImplementedError

        self._nodelist += Node
        return True

    def generate_random_edge(self,variance=self._variance):
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
            if new_edge.length() < math.abs(reject_criteria):
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
