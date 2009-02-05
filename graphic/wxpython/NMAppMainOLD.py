#!/usr/bin/env python
from wxPython.wx import *


class NMFrame(wxFrame):
    def __init__(self):
    	versione='0'
    	revisione='0'
        # Chiama il costruttore di wxFrame.
        #wxFrame.__init__(self,None, -1, "Nokiomane V"+self.versione+"."+self.revisione)
       
        wxFrame.__init__(self, None, -1, "Nokiomane V")

        ID_INFO = wxNewId()
        ID_IMPOST = wxNewId()
        ID_ESCI = wxNewId()
#
#-----------------Menu File---------------------------------
#        
        menu_file = wxMenu()
        
        menu_file.Append(ID_IMPOST, "&Impostazioni",
                         "Qualche impostazione del programma")
        menu_file.AppendSeparator()
        menu_file.Append(ID_ESCI, "&Esci",
                         "Esci dal programma")
        
        
#
#-----------------Menu Help---------------------------------
#        
        menu_help = wxMenu()   
        
        menu_help.Append(ID_INFO, "&Aiuto",
                         "Qualche informazione sul programma")
          
        menu_help.Append(ID_INFO, "&Informazioni...",
                         "Qualche informazione sul programma")                          
       
        EVT_MENU(self, ID_INFO, self.OnInfo)
        EVT_MENU(self, ID_IMPOST, self.OnImpost)
        EVT_MENU(self, ID_ESCI, self.OnEsci)

        menu_bar = wxMenuBar()
        menu_bar.Append(menu_file, "&File");
        menu_bar.Append(menu_help, "&Help");
        self.SetMenuBar(menu_bar)

        # Crea una barra di stato con due pannelli.
        self.CreateStatusBar()
        # Imposta il testo della barra di stato.
        self.SetStatusText("Semplice barra di stato")

    def OnInfo(self, event):
        # Mostra un semplice messaggio.
        wxMessageBox("Questo programma mostra "
                     "come usare i menu")
    def OnImpost(self, event):
    	# Mostra un semplice messaggio.
        wxMessageBox("Questo programma mostra "
                     "dfghjkmnbgyjh")

    def OnEsci(self, event):
        # Distrugge il frame.
        self.Close(1)


class NMApp(wxApp):
    def OnInit(self):
        frame = NMFrame()
        frame.Show(1)
        self.SetTopWindow(frame)
        return 1
