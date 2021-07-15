#Turning a python script into an exe file

import cx_Freeze
import sys
import PIL
import os

base = None

if sys.platform == "win64":
	base = "Win64GUI"

executables = [cx_Freeze.Executable("tkGui.py", base = base, icon="icon256.ico")]

os.environ['TCL_LIBRARY'] = r'D:\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Python35\tcl\tk8.6'


cx_Freeze.setup(
	name = "FGOAP-Client",
	options = {"build_exe": {"packages":["tkinter","PIL"], "include_files":["icon256.ico","page2bg2.png","startingBackgroundPng.png","button1gif.gif","classes","common","__pycache__"]}},
	version = "0.01",
	description = "Fate Grand Order fan made assisting executable program",
	executables = executables
	)
