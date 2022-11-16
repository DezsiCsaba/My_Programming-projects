import numpy
import pygame
from Segment import Segment_C


class Digit_C():
    basex = int
    basey = int
    Segments = numpy.full(7, None)



    def _digitInit_(self, x, y):
        A,B,C,D,E,F,G = Segment_C(),Segment_C(),Segment_C(),Segment_C(),Segment_C(),Segment_C(),Segment_C()
        long = 50
        short = 10
        displace = 15
        self.basex = x
        self.basey = y

        A._segmenInit_("A", (self.basex+displace, y, long, short))
        B._segmenInit_("B", (self.basex+displace+long, y+short, short, long))
        C._segmenInit_("C", (self.basex+displace+long, y+long+2*short, short, long))
        D._segmenInit_("D", (self.basex+displace, y+2*long+2*short, long, short))
        E._segmenInit_("E", (self.basex+displace-short, y+long+2*short, short, long))
        F._segmenInit_("F", (self.basex+displace-short, y+short, short, long))
        G._segmenInit_("G", (self.basex+displace, y+long+short, long, short))
        

        self.Segments[0] = A
        self.Segments[1] = B
        self.Segments[2] = C
        self.Segments[3] = D
        self.Segments[4] = E
        self.Segments[5] = F
        self.Segments[6] = G
    
    def Switch(self, name, onOrOff):
        for segment in self.Segments:
            if (segment.name == name):
                segment.SegmentSwitch(onOrOff)
                break

    def DisplayDigit(self, surface, color):
        print("\n" + str(self))
        for i in range(len(self.Segments)):
            if(self.Segments[i].isOn):
                pygame.draw.rect(surface, color, (self.Segments[i].segmentRect))
                print(self.Segments[i].name)

    
