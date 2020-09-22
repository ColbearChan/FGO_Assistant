import tkinter as tk
from tkinter import ttk #CSS for tkinter
from PIL import Image, ImageTk
import fgo_auto as fa
import threading
import os
import sys

LARGE_FONT = ("Verdana", 12)

class Foundation(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="icon256.ico")
        tk.Tk.wm_title(self, "FGOAP")
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, PageMenu):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bgPic_open = Image.open('startingBackgroundPng.png')
        bgPic_render = ImageTk.PhotoImage(bgPic_open)
        label_img = tk.Label(self, image = bgPic_render)
        label_img.photo = bgPic_render
        label_img.place(x=0, y=0, relwidth=1, relheight=1)
        
        label = tk.Label(self, text = "Fate Grand Order Assisting Pal", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        buttonPic = tk.PhotoImage(file = "button1gif.gif")
        button1 = tk.Button(self, image = buttonPic, compound = 'bottom',text="Enter", command = lambda: controller.show_frame(PageMenu))
        button1.photo = buttonPic
        button1.config(height = 150, width = 230)
        button1.place(x =175, y =160)


class PageMenu(tk.Frame):   

        
    def __init__(self, parent, controller):

        def startRolling(times, curStamina, maxStamina):
            if times == 0:
                labelException1 = ttk.Label(self, text = "请增加次数")
                labelException1.place(x = 200,y = 40)
            else:
                thread = threading.Thread(target = fa.main, args = (fa.roles[1],times, curStamina, maxStamina))
                thread.daemon = True
                thread.start()

        def stopRolling():

            #os.execv(sys.executable, ['python'] + sys.argv)
            os.startfile('tkGui.exe')
            sys.exit()

        def eatAGoldApple():
        	threadGoldApple = threading.Thread(target = fa.eatGoldApples)
        	threadGoldApple.daemon = True
        	threadGoldApple.start()

        def eatASilverApple():
        	threadSilverApple = threading.Thread(target = fa.eatSilverApples)
        	threadSilverApple.daemon = True
        	threadSilverApple.start()

        tk.Frame.__init__(self, parent)

        bgPic_open = Image.open('page2bg2.png')
        bgPic_render = ImageTk.PhotoImage(bgPic_open)
        label_img = tk.Label(self, image = bgPic_render)
        label_img.photo = bgPic_render
        label_img.place(x=0, y=0, relwidth=1, relheight=1)
        
        label = tk.Label(self, text = "这次想打些什么呢", font = LARGE_FONT)
        label.place(x = 20,y = 30)

        labelcs = tk.Label(self, text = "times", font = LARGE_FONT)
        labelcs.place(x = 180,y = 150)
        times = tk.IntVar()
        textFieldt = tk.Entry(self, textvariable = times)
        textFieldt.place(x = 180, y = 170)


        labelcs = tk.Label(self, text = "current Stamina", font = LARGE_FONT)
        labelcs.place(x = 40,y = 125)
        curStamina = tk.IntVar()
        textFieldcs = tk.Entry(self, textvariable = curStamina)
        textFieldcs.place(x = 40, y = 145)

        labelmx = tk.Label(self, text = "max Stamina", font = LARGE_FONT)
        labelmx.place(x = 40,y = 180)
        maxStamina = tk.IntVar()
        textFieldmx = tk.Entry(self, textvariable = maxStamina)
        textFieldmx.place(x = 40, y = 200)


  
        labelcs = tk.Label(self, text = "狂阶", font = LARGE_FONT)
        labelcs.place(x = 40,y = 80)

        button5 = tk.Button(self, text="   Back    ", command = lambda: controller.show_frame(StartPage), font = LARGE_FONT)
        button5.place(x = 40, y = 240)

        button6 = tk.Button(self, text="    Exit    ", command = lambda: sys.exit(), font = LARGE_FONT)
        button6.place(x = 40, y = 280)

        button7 = tk.Button(self, text="=-=-=Start=-=-=",  command = lambda: startRolling(times.get(), curStamina.get(), maxStamina.get()),font = LARGE_FONT)
        button7.place(x = 180, y = 240)

        button8 = tk.Button(self, text="----Stop----", font = LARGE_FONT, command = lambda: stopRolling())
        button8.place(x = 205, y = 280)

        #button9 = tk.Button(self, text="补充一个金苹果", font = LARGE_FONT, command = lambda: eatAGoldApple())
        #button9.place(x = 180, y = 120)

        #button10 = tk.Button(self, text="补充一个银苹果", font = LARGE_FONT, command = lambda: eatASilverApple())
        #button10.place(x = 180, y = 80)


if __name__ == "__main__":
    app = Foundation()
    app.geometry('600x350')
    app.resizable(0,0)
    app.mainloop()
