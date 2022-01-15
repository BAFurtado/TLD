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
        self.interaction = interaction.Interaction()
        self.createmap_bt = tkinter.Button(self, text=u"Create maps", state='disabled',
                                           command=lambda: mapping.create_maps(self.sPath, self.mPath))
        self.run_bt = tkinter.Button(self, text=u"Start mapping", state='disabled', command=lambda:
                                     interaction.background(self.interaction.start_interactive_mapping,
                                                            (self.sPath, self.mPath)))
        self.start_bt = tkinter.Button(self, text=u"Start recording", state='normal',
                                       command=lambda: self.interaction.start_recording())
        self.stop_bt = tkinter.Button(self, text=u"Stop recording", state='normal',
                                      command=lambda: self.interaction.stop_recording())
        self.close_app = tkinter.Button(self, text=u"Close APP", state='normal',
                                        command=lambda: self.destroy())
        self.parent = None
        self.initialize()

    def initialize(self):
        tkinter.Tk.grid(self)
        maps_bt = tkinter.Button(self, text='Choose maps directory', command=self.choose_maps_dir)
        maps_bt.grid(column=0, row=0, columnspan=2, sticky='EW')
        screenshots_bt = tkinter.Button(self, text='Choose screenshots directory', command=self.choose_screen_dir)
        screenshots_bt.grid(column=0, row=1, columnspan=2, sticky='EW')

        self.run_bt.grid(column=0, row=2)
        self.createmap_bt.grid(column=1, row=2)
        self.start_bt.grid(column=0, row=3, columnspan=1)
        self.stop_bt.grid(column=1, row=3, columnspan=1)
        self.close_app.grid(column=0, row=4, columnspan=2)

        tkinter.Tk.grid_columnconfigure(self, index=0, weight=1)
        tkinter.Tk.resizable(self, False, False)

    def enable_buttons(self):
        if self.sPath != "" and self.mPath != "":
            self.run_bt['state'] = 'normal'
            self.createmap_bt['state'] = 'normal'

    def choose_screen_dir(self):
        # self.sPath = askdirectory() + "/"
        self.sPath = '/home/furtado/Desktop/'
        print(f'Directory set at Defautl {self.sPath}')
        self.enable_buttons()

    def choose_maps_dir(self):
        self.mPath = askdirectory() + "/"
        print(f'Directory set at {self.mPath}')
        self.enable_buttons()


# 4 - Execution
if __name__ == "__main__":
    app = TLDMappingToolTK()
    app.title('TLD Mapping Tool')
    app.mainloop()
