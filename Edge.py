import math

class Edge:
    _start = ''
    _end = ''
    _style = ''

    def __repr__(self):
        return "\\Edge[style=%s](%s)(%s)" %\
                (self._style, self._start, self._end)

    def length(self):
        dx = self._start._x_location - self._end._x_location
        dy = self._start._y_location - self._end._y_location
        return math.sqrt( dx**2 + dy**2 )

class Loop:
    _node = ''
    _dist = ''
    _loop_dir = ''
    _side = ''

    def __repr__(self):
        return "\\Loop[dist=%s, dir=%s](%s.%s)\n" \
                (self._dist, self._loop_dir, self._node, self._side)
