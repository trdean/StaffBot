import abc

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


