#!/usr/bin/env python3
#coding:utf-8


import os,sys,time
import tkinter as tk
import subprocess
import json 

def exitProg():
    quit()

print(os.path.dirname(__file__)+"/wakeuponlan_ui.json")
f=open(os.path.dirname(__file__)+"/wakeuponlan_ui.json","r")
macaddr = json.load(f);


def start(self):
    subprocess.call(["wakeonlan",macaddr[self]])
    
root = tk.Tk()
root.title("Wake up on LAN")
#root.geometry("150x200")
label = tk.Label(root, text="wake up on lan")
label.grid()

for machine in macaddr.keys():
    button = tk.Button(root,text=machine, command=lambda: start(machine))
    button.grid()

exit = tk.Button(root,text="exit", command=exitProg)
exit.grid()


root.mainloop()
