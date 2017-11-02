#!/usr/bin/python

import tkinter as Tk
from tkinter import *

class MainWindow(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()
app = MainWindow(root)

root.mainloop()
