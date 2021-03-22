# 3 - GUI

import tkinter
import tkinter.filedialog
from tkinter.filedialog import askdirectory

import interaction
import mapping


class TLDMappingToolTK(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.createmap_bt = tkinter.Button(self,
                                           text=u"Create maps",
                                           state='disabled',
                                           command=lambda: mapping.create_maps(self.sPath, self.mPath))
        self.run_bt = tkinter.Button(self,
                                     text=u"Start mapping",
                                     state='disabled',
                                     command=lambda: self.interaction.start_interactive_mapping(self.sPath, self.mPath))
        self.mPath = ""
        self.sPath = ""

        self.parent = None
        self.interaction = interaction.Interaction()
        self.initialize()

    def initialize(self):
        tkinter.Tk.grid(self)
        maps_bt = tkinter.Button(self, text='Choose maps directory', command=self.choose_maps_dir)
        maps_bt.grid(column=0, row=0, columnspan=2, sticky='EW')

        screenshots_bt = tkinter.Button(self, text='Choose screenshots directory', command=self.choose_screen_dir)
        screenshots_bt.grid(column=0, row=1, columnspan=2, sticky='EW')

        self.run_bt.grid(column=0, row=2)

        self.createmap_bt.grid(column=1, row=2)

        tkinter.Tk.grid_columnconfigure(self, index=0, weight=1)
        tkinter.Tk.resizable(self, False, False)

    def enable_buttons(self):
        if self.sPath != "" and self.mPath != "":
            self.run_bt['state'] = 'normal'
            self.createmap_bt['state'] = 'normal'

    def choose_screen_dir(self):
        self.sPath = askdirectory() + "/"
        self.enable_buttons()

    def choose_maps_dir(self):
        self.mPath = askdirectory() + "/"
        self.enable_buttons()


# 4 - Execution
if __name__ == "__main__":
    app = TLDMappingToolTK()
    app.title('TLD Mapping Tool')
    app.mainloop()
