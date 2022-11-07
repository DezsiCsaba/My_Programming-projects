class _CellC():
    collapsed = False
    options = []
    
    def _CellInit(self, value):
        self.collapsed = False
        if (type(value) == []):
            self.options = value
        else:
            self.options = []
            for i in range(0,value):
                self.options.append(i)