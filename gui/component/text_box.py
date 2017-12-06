from tkinter import StringVar
from tkinter import Entry

from gui.component.listener import Listener

class TextBox(Entry):

    def __init__(self, master, value, data_scource, index):

        Entry.__init__(self, master=master)

        self.index = index
        self.data_scource = data_scource
        self.value = value
        self.config(textvariable=self.value, width=15)

        self.value.set(value)
        self.data_scource.addListener(Listener(self, "<<naviage_record>>"), lambda e: self.on_data_source_change)

    def on_data_source_change(self):

        self.value.set(self.data_scource.current_record()[self.index])