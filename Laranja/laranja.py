import random
from tkinter import *

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from psutil import (
    Process,
    cpu_count,
    cpu_freq,
    net_io_counters,
    pids,
    process_iter,
)


class Software:
    def __init__(self, colorbutton):

        self.color = color
        self.ws = Tk()
        self.ws.title('Laranja')
        width = self.ws.winfo_screenwidth() - 500
        height = self.ws.winfo_screenheight() - 100
        self.ws.geometry('%dx%d' % (width, height))
        self.ws.overrideredirect(False)
        self.ws.attributes('-transparentcolor', 'grey', '-alpha', 8)

        self.icon = PhotoImage(master=self.ws, file='orange.png')

        self.img = PhotoImage(file='orange.png')
        self.img1 = Label(self.ws, image=self.img, background=self.color)
        self.img1.pack()

        self.ws.wm_iconphoto(True, self.icon)
        self.ws.config(bg=self.color)

        self.widget = Frame(self.ws)
        self.widget.pack(side='bottom')

        self.bto1 = Button(
            self.widget,
            bg=colorbutton,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto2 = Button(
            self.widget,
            bg=colorbutton,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto3 = Button(
            self.widget,
            bg=colorbutton,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto4 = Button(
            self.widget,
            bg=colorbutton,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto5 = Button(
            self.widget,
            bg=colorbutton,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto6 = Button(
            self.widget,
            bg=colorbutton,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto7 = Button(
            self.widget,
            bg=colorbutton,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto8 = Button(
            self.widget,
            bg=colorbutton,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.color = color

        def upcolor():

            cor = random.randint(0, 5)
            if cor == 0:
                self.ws.config(bg=vicolor)
            if cor == 1:
                self.ws.config(bg=orcolor)
            if cor == 2:
                self.ws.config(bg=rubcolor)
            if cor == 3:
                self.img1 = Label(
                    self.ws, image=self.img, background=darkcolor
                )
                self.ws.config(bg=darkcolor)
            if cor == 4:
                self.ws.config(bg=redcolor)
                self.ws.update_idletasks()

        def FPS():
            self.color = color
            self.ws1 = Tk()
            self.ws1.title('Laranja')
            self.ws1.geometry('200x200+1150+500')
            self.ws1.overrideredirect(True)
            self.ws1.attributes('-transparentcolor', 'grey', '-alpha', 0.5)
            img = PhotoImage(open('orange.png'))

            canvas = Canvas(self.ws1, width=600, height=400)
            canvas.create_image(10, 10, anchor=NW, image=img)
            canvas.pack()

            return self.ws.wm_minsize()

            ...

        self.bto1['text'] = 'Investigate'
        self.bto1['command'] = self.func
        self.bto1.grid(row=0, column=0)

        self.bto2['text'] = 'Grafico'
        self.bto2['command'] = self.newwindow
        self.bto2.grid(row=0, column=1)

        self.bto3['text'] = 'Otmizar'
        self.bto3['command'] = ''
        self.bto3.grid(row=0, column=2)

        self.bto4['text'] = 'Force FPS'
        self.bto4['command'] = FPS
        self.bto4.grid(row=0, column=3)

        self.bto5['text'] = 'Internet Control'
        self.bto5['command'] = ''
        self.bto5.grid(row=0, column=4)

        self.bto6['text'] = 'Brute Ping'
        self.bto6['command'] = ''
        self.bto6.grid(row=0, column=5)

        self.bto7['text'] = 'Color'
        self.bto7['command'] = upcolor
        self.bto7.grid(row=0, column=6)

        self.bto8['text'] = 'Sair'
        self.bto8['command'] = self.widget.quit
        self.bto8.grid(row=0, column=7)

        self.ws.mainloop()

    def func(self):
        color = vicolor
        self.msg = Label(self.ws, bg=color)
        self.msg['text'] = 'Numero de Processadores'
        self.msg['font'] = font
        self.msg.place(x=20, y=60)

        self.msg = Label(self.ws, bg=color)
        self.msg['text'] = 'Frequencia do Processador'
        self.msg['font'] = font
        self.msg.place(x=20, y=100)

        self.msg = Label(self.ws, bg=color)
        self.msg['text'] = 'Processos abertos'
        self.msg['font'] = font
        self.msg.place(x=20, y=140)

        self.numero_cpu = cpu_count()
        self.frequencia_cpu = cpu_freq().current
        self.todosProcessos = pids()
        self.processos = Process()
        self.processos.parent()
        self.processos = len(self.todosProcessos)
        for proc in process_iter(['name']):
            processos = proc.info
            print(processos)

        self.msg = Label(self.ws, text=self.numero_cpu, bg=color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=40, y=80)

        self.msg = Label(self.ws, text=self.frequencia_cpu, bg=color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=40, y=120)

        self.msg = Label(self.ws, text=self.processos, bg=color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=40, y=160)
        self.ws.mainloop()

    def newwindow(self):

        self.color = color
        self.ws = Tk()
        width = self.ws.winfo_screenwidth()
        height = self.ws.winfo_screenheight()
        self.ws.geometry('%dx%d' % (width, height))
        self.ws.overrideredirect(True)
        self.icon = PhotoImage(master=self.ws, file='orange.png')

        self.figura = plt.Figure(figsize=(10, 4), dpi=60)
        self.ax = self.figura.add_subplot(111)

        canva = FigureCanvasTkAgg(self.figura, self.ws)
        canva.get_tk_widget().grid(row=0, column=0)

    def emitter(p=0.1):
        global pEnvi

        while True:
            # bRece = [psutil.net_io_counters().bytes_recv]
            pEnvi = [net_io_counters().packets_sent]
            print(pEnvi)
            vp = 1
            if vp > p:
                yield np.array((pEnvi[:1]))

            else:
                yield np.random.rand(1)
        np.random.seed(19680801 // 10)

        fig, ax = plt.subplots()

        ani = animation.FuncAnimation(
            fig, update, emitter, interval=100, blit=False
        )
        plt.show()

        self.ws.mainloop()


font = 'Calibri', '10'
orcolor = '#00ff51'
vicolor = '#bf00ff'
rubcolor = '#e0115f'
darkcolor = '#000'
redcolor = '#ff0000'
color = vicolor
brcolor = '#ffffff'

App = Software(colorbutton=orcolor)
