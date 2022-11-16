import numpy
from Segment import Segment_C


class Digit_C():

    Segments = numpy.full(7, None)
    def _digitInit_(self):
        A,B,C,D,E,F,G = Segment_C(),Segment_C(),Segment_C(),Segment_C(),Segment_C(),Segment_C(),Segment_C()
        
        A._segmenInit_("A")
        B._segmenInit_("B")
        C._segmenInit_("C")
        D._segmenInit_("D")
        E._segmenInit_("E")
        F._segmenInit_("F")
        G._segmenInit_("G")

        self.Segments[0] = A
        self.Segments[1] = B
        self.Segments[2] = C
        self.Segments[3] = D
        self.Segments[4] = E
        self.Segments[5] = F
        self.Segments[6] = G
    
    def SegmentSwitch(self, name, onOrOff):
        for i in range(len(self.Segments)):
            if (self.Segments[i].name == name):
                self.Segments[i].SegmentSwitch(onOrOff)
                break

    def DisplayDigit(self, num):
        for i in range(len(self.Segments)):
            if(self.Segments[i].isOn):
                print(self.Segments[i].name)

    
