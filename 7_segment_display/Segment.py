class Segment_C():

    name = ""
    isOn = False

    def _segmenInit_(self, name):
        self.name = name
        self.isOn = False

    def SegmentSwitch(self, on_or_off):
        if (on_or_off == True or on_or_off == "on"):
            self.isOn = True
        elif (on_or_off == False or on_or_off == "off"):
            self.isOn = False


    