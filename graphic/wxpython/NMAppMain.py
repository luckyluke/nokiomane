#!/usr/bin/python

import wx
versione="0"
revisione="1"


class LeftPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
        #button1 = wx.Button(self, -1, 'Connessione..', (10, 500))


class RightPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
	button1 = wx.Button(self, -1, 'Connessione..', (30, 250))

class NMFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800, 600))
        
        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(-1, 'Quit', 'Quit application')
        menubar.Append(file, '&File')
        self.SetMenuBar(menubar)


        panel = wx.Panel(self, -1)
        self.rightPanel = RightPanel(panel, -1)

        leftPanel = LeftPanel(panel, -1)

        hbox = wx.BoxSizer()
        hbox.Add(leftPanel, 3, wx.EXPAND | wx.ALL, 3)
        hbox.Add(self.rightPanel, 1, wx.EXPAND | wx.ALL, 3)

        panel.SetSizer(hbox) 
        self.Centre()
        self.Show(True)

app = wx.App()
NMFrame(None, -1, "Nokiomane V"+versione+"."+revisione)
app.MainLoop()