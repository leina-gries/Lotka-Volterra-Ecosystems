#! /usr/bin/env python3

#################################import tkinter as Tk

from tkinter import *

control = Tk()

scale = Scale(control, resolution=0.1, orient=HORIZONTAL,length=300,width=20,sliderlength=10,from_=.1,to=1.10,tickinterval=0.1)
scale.pack()

scale = Scale(control,orient=VERTICAL,length=300,width=20,sliderlength=10,from_=0,to=1000,tickinterval=200)
scale.pack()

control.mainloop()

