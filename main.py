# 3 - GUI

import tkinter
import tkinter.filedialog
from tkinter.filedialog import askdirectory

import interaction
import mapping


class TLDMappingToolTK(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.mPath = ""
        self.sPath = ""

        self.parent = None
        self.interaction = interaction.Interaction()
        self.initialize()

    def initialize(self):
        tkinter.Tk.grid(self)
        maps_bt = tkinter.Button(self, text='Choose maps directory', command=self.chooseMapsDir)
        maps_bt.grid(column=0, row=0, columnspan=2, sticky='EW')

        screenshots_bt = tkinter.Button(self, text='Choose screenshots directory', command=self.chooseScreenDir)
        screenshots_bt.grid(column=0, row=1, columnspan=2, sticky='EW')

        self.run_bt = tkinter.Button(self,
                                     text=u"Start mapping",
                                     state='disabled',
                                     command=lambda: self.interaction.startInteractiveMapping(self.sPath, self.mPath))
        self.run_bt.grid(column=0, row=2)

        self.createmap_bt = tkinter.Button(self,
                                           text=u"Create maps",
                                           state='disabled',
                                           command=lambda: mapping.createMaps(self.sPath, self.mPath))
        self.createmap_bt.grid(column=1, row=2)

        tkinter.Tk.grid_columnconfigure(self, index=0, weight=1)
        tkinter.Tk.resizable(self, False, False)

    def enableButtons(self):
        if self.sPath != "" and self.mPath != "":
            self.run_bt['state'] = 'normal'
            self.createmap_bt['state'] = 'normal'

    def chooseScreenDir(self):
        self.sPath = askdirectory() + "/"
        self.enableButtons()

    def chooseMapsDir(self):
        self.mPath = askdirectory() + "/"
        self.enableButtons()


# 4 - Execution
if __name__ == "__main__":
    app = TLDMappingToolTK()
    app.title('TLD Mapping Tool')
    app.mainloop()
