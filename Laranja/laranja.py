from tkinter import *
from tkinter import ttk
import psutil
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from time import sleep


class Application:
    def __init__(self, master=None):
        self.img = PhotoImage(file='orange.png')

        self.widget1 = Frame(master, bg=color)
        self.widget1.pack(side='bottom')
        self.img1 = Label(master, image=self.img, background=color)
        self.img1.pack()

        self.otm = Button(self.widget1, bg=color, activebackground=color1, bd=1)
        self.otm["text"] = "Otimizar"
        self.otm["font"] = ("Calibri", "10")
        self.otm["width"] = 10
        self.otm["command"] = self.otmizar
        self.otm.pack()

        self.test = Button(self.widget1, bg=color, activebackground=color1, bd=1)
        self.test["text"] = "Testar"
        self.test["font"] = ("Calibri", "10")
        self.test["width"] = 10
        self.test["command"] = self.testar
        self.test.pack()

        self.graf = Button(self.widget1, bg=color, activebackground=color, bd=1)
        self.graf["text"] = "Gráfico"
        self.graf["font"] = ("Calibri", "10")
        self.graf["width"] = 10
        self.graf["command"] = self.grafico
        self.graf.pack()

        self.sair = Button(self.widget1, bg=color, activebackground=color1, bd=1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair["command"] = self.widget1.quit
        self.sair.pack()

    def otmizar(self):
        self.load = Image.open('orange.png')
        self.render = PhotoImage(self.load)
        self.img = Label(self, image=self.render)
        self.fps.overrideredirect(True)
        self.imgFPS.pack(side=TOP, ipadx=25, pady=25)

    def testar(self):
        self.msg = Label(ws, text='Numero de Processadores', bg=color)
        self.msg["font"] = ("BungeeSpice Regular", "10", "italic")
        self.msg.place(x=20, y=60)

        self.msg = Label(ws, text='Frequencia do Processador', bg=color)
        self.msg["font"] = ("BungeeSpice Regular", "10", "italic")
        self.msg.place(x=20, y=100)

        self.msg = Label(ws, text='Processos abertos', bg=color)
        self.msg["font"] = ("BungeeSpice Regular", "10", "italic")
        self.msg.place(x=20, y=150)

        self.pb = ttk.Progressbar(ws, orient='horizontal', mode='determinate', length=600, maximum=50)
        self.pb.winfo_visual()
        self.pb.place(x=0, y=0)
        self.pb.start()
        if self.pb['value'] < 100:
            self.pb.stop()

        self.numero_cpu = psutil.cpu_count()
        self.frequencia_cpu = psutil.cpu_freq().current
        self.todosProcessos = psutil.pids()
        self.processos = psutil.Process()
        self.processos.parent()
        self.processos = (len(self.todosProcessos))

        ronw = 0
        lin = 50
        for proc in psutil.process_iter(['name']):
            processos = proc.info
            print(processos)

        self.msg = Label(ws, text=self.numero_cpu, bg=color)
        self.msg["font"] = ("BungeeSpice Regular", "10", "italic")
        self.msg.place(x=40, y=80)

        self.msg = Label(ws, text=self.frequencia_cpu, bg=color)
        self.msg["font"] = ("BungeeSpice Regular", "10", "italic")
        self.msg.place(x=40, y=120)

        self.msg = Label(ws, text=self.processos, bg=color)
        self.msg["font"] = ("BungeeSpice Regular", "10", "italic")
        self.msg.place(x=40, y=180)

    def grafico(self):
        self.plt = plt.style.use('_mpl-gallery')
        self.xpoints = ([(float(psutil.cpu_freq().min)), 2, 6, 8])
        self.ypoints = np.array([3, 8, 1, (float(psutil.cpu_freq().max))])
        while not self.test.__init__():
            self.plt = plt.style.use('_mpl-gallery')
            self.xpoints = ([(float(psutil.cpu_freq().min)), 2, 6, 8])
            self.ypoints = np.array([3, 8, 1, (float(psutil.cpu_freq().max))])
            self.plot = plt.plot(self.xpoints, self.ypoints)
            self.plot = plt.show()
            return


ws = Tk()
ws.overrideredirect(True)
ws.title('Laranja')
icon = PhotoImage(master=ws, file='orange.png')
ws.wm_iconphoto(True, icon)
ws.geometry('600x600+400+50')
color = '#ffa525'
color1 = '#ffa125'
ws.config(bg='#ffa500')
Application(ws)
ws.mainloop()
