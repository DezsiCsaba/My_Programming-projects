import pygame

class Segment_C():

    name = ""
    isOn = False
    segmentRect = pygame.rect(0,0,0,0)

    def _segmenInit_(self, name, rectangle):
        self.name = name
        self.isOn = True
        self.segmentRect = rectangle

    def SegmentSwitch(self, on_or_off):
        if (on_or_off == True or on_or_off == "on"):
            self.isOn = True
        elif (on_or_off == False or on_or_off == "off"):
            self.isOn = False


    