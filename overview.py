import wx

from filterpanel import WheelPanel
from focusREI import FocusREIPanel
#from grismpanel import GrismPanel
from guideinfopanel import GuideInfoPanel
from kmirrorpanel import KmirrorPanel
#from maskpanel import MaskPanel
from schematicpanel import SchematicPanel

class OverviewPanel(wx.ScrolledWindow):
    def __init__(self, parent, *args, **kwargs):
        super(OverviewPanel, self).__init__(parent)
        
        self.SetScrollbars(20,20,55,40)

        # Attributes
        self.Schematic = SchematicPanel(self)
        self.Mask = WheelPanel(self, 'mask')
        self.FilterOne = WheelPanel(self, 'filter1')
        self.FilterTwo = WheelPanel(self, 'filter2')
        self.Grism = WheelPanel(self, 'grism')
        self.Kmirror = KmirrorPanel(self)
        self.GuideInfo = GuideInfoPanel(self)
        self.FocusREI12 = FocusREIPanel(self, 'Focus REI-1-2', 0)
        self.FocusREI34 = FocusREIPanel(self, 'Focus REI-3-4', 1)
        
        self.__DoLayout()

    def __DoLayout(self):
        ## Layout for this panel:
        ##
        ##    0               1
        ##   +---------------+---------------+
        ## 0 | k-mirror      | guiding       |
        ##   +---------------+---------------+
        ## 1 | schematic     | self.new_dec  |
        ##   +---------------+---------------+
        ##
        sbox = wx.StaticBox(self, label="")
        boxSizer = wx.StaticBoxSizer(sbox, wx.HORIZONTAL)
        sizer = wx.GridBagSizer(vgap=2, hgap=2)
        
        # Add controls to gridbag
        sizer.Add(self.Kmirror, pos=(0,0), span=(1,1), flag=wx.LEFT|wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.FocusREI12, pos=(0,1), span=(1,1), flag=wx.LEFT|wx.ALIGN_BOTTOM)
        sizer.Add(self.GuideInfo, pos=(1,2), span=(1,1), flag=wx.LEFT|wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.Schematic, pos=(1,0), span=(6,2), flag=wx.LEFT|wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.FocusREI34, pos=(2,2), span=(1,1), flag=wx.LEFT|wx.ALIGN_BOTTOM)
        sizer.Add(self.Mask, pos=(3,2), span=(1,1), flag=wx.LEFT|wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.FilterOne, pos=(4,2), span=(1,1), flag=wx.LEFT|wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.FilterTwo, pos=(5,2), span=(1,1), flag=wx.LEFT|wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(self.Grism, pos=(6,2), span=(1,1), flag=wx.LEFT|wx.ALIGN_CENTER_VERTICAL)
                
        
        # Add the grid bag to the static box and make everything fit
        boxSizer.Add(sizer, wx.EXPAND)
        self.SetSizerAndFit(boxSizer)
