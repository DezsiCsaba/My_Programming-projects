import numpy as np
from Tile import Tile_C

class Cell_C():
    collapsed = False
    #options = []
    options = np.empty(5, int)

    def _CellInit(self, value):
        self.collapsed = False
        if (isinstance(value, list)):
            self.options = value
        else:
            self.options = np.empty((1(1)))
            for i in range(0,value):
                #self.options.append(i)
                self.options[i] = i

    #def _CellInit(self):
    #    self.options = []
    #    self.collapsed = False