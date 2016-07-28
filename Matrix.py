import random

class Matrix:
    width = 3
    depth = 10

    types = { "state" : 0.40,\
            "decision" : 0.20,\
            "block" : 0.40 }

    matrix = [['' for i in range(width)] for j in range(depth)]

    def random_node(self, include_decision=True):
        choice = None
        while True:
            choice = random.choice(self.types.keys())
            if (include_decision == False) and (choice == "decision"):
                continue

            if random.random() < self.types[choice]:
                break

        return choice

    def __init__(self):
        #Start on left side, top left is state, bottom left is state
        for x in range(self.depth):
            if x == 0 or x == self.depth-1:
                self.matrix[x][0] = "absorbingstate"
            else:
                self.matrix[x][0] = self.random_node()

        #Now go row by row
        for x in range(1,self.depth-1):
            for y in range(1,self.width):
                if self.matrix[x-1][y] != "":
                    if random.random() < 0.3 and self.matrix[x][y-1] !=\
                    "decision":
                        continue

                    self.matrix[x][y] = self.random_node(include_decision=False)
                    continue

                if self.matrix[x][y-1] != "decision":
                    continue

                #Last column can't have decisions
                if y == self.width-1:
                    self.matrix[x][y] = self.random_node(include_decision=False)
                else:
                    self.matrix[x][y] = self.random_node()
                    if self.matrix[x][y] == "decision":
                        #We need a node in the next column
                        continue
                    else:
                        break

    @property
    def node_width(self):
        max_column = 0
        for row in self.matrix:
            for i,node in enumerate(row):
                if node != '' and i > max_column:
                    max_column = i

        return max_column

    def row_width(self,index):
        result = 0
        for node in self.matrix[index][1:]:
            if node != '':
                result += 1
            else:
                return result
        return result

    def column_start(self, index):
        result = 0
        for i in range(len(self.matrix)):
            if self.matrix[i][index] == '':
                result += 1
            else:
                return result
        return result

    def column_end(self, index):
        result = len(self.matrix)
        for i in range(len(self.matrix)-1,-1,-1):
            if self.matrix[i][index] == '':
                result -= 1
            else:
                return result
        return result

