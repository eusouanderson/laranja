from tkinter import *
from tkinter import ttk
import psutil

'''import matplotlib.pyplot as plt
import numpy as np'''


class Application:
    def __init__(self, master=None):
        self.img = PhotoImage(file='orange.png', height=550)
        self.menubar = Menu(ws, background='#ff8000', foreground='black', activebackground='white',
                            activeforeground='black', bg=color)
        self.file = Menu(self.menubar, tearoff=1, background='#ffcc99', foreground='black')
        self.file.add_command(label="New")
        self.menubar.add_cascade(label="Arquivo", menu=self.file)
        self.menubar.add_cascade(label="Opções", menu=self.file)
        self.menubar.add_cascade(label="Game", menu=self.file)
        self.menubar.add_cascade(label="Help", menu=self.file)

        ws.config(menu=self.menubar)
        self.widget1 = Frame(master, bg=color)
        self.widget1.pack(side='bottom')

        self.msg = Label(self.widget1, image=self.img, text="Todos os direitos rservados", bg=color)
        self.msg["font"] = ("Verdana", "20", "italic", "bold")
        self.msg.pack(fill='both')

        self.test = Button(self.widget1, bg=color, activebackground=color, bd=1)
        self.test["text"] = "Otimizar"
        self.test["font"] = ("Calibri", "10")
        self.test["width"] = 10
        self.test["command"] = ''
        self.test.place(x=5, y=10)

        self.sair = Button(self.widget1, bg=color, activebackground=color, bd=1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair["command"] = self.widget1.quit
        self.sair.pack()

        self.test = Button(self.widget1, bg=color, activebackground=color, bd=1)
        self.test["text"] = "Testar"
        self.test["font"] = ("Calibri", "10")
        self.test["width"] = 10
        self.test["command"] = self.testar
        self.test.pack()

        self.msg4 = Label(ws, text='', bg=color)
        self.msg4["font"] = ("Verdana", "10", "italic", "bold")
        self.msg4.place(x=30, y=140)

    def testar(self):
        self.msg = Label(ws, text='Numero de Processadores', bg=color)
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.place(x=40, y=60)

        self.msg = Label(ws, text='Frequencia do Processador', bg=color)
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.place(x=40, y=100)

        self.msg = Label(ws, text='Processos abertos', bg=color)
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.place(x=40, y=150)

        self.pb = ttk.Progressbar(ws, orient='horizontal', mode='determinate', length=600)
        self.pb.place(x=0, y=0)
        self.pb.start()
        self.numero_cpu = psutil.cpu_count()
        self.frequencia_cpu = psutil.cpu_freq().current
        self.todosProcessos = psutil.pids()
        self.processos = psutil.Process()
        self.processos.parent()
        self.processos = (len(self.todosProcessos))

        for proc in psutil.process_iter(['pid', 'name']):
            processos = proc.info

            print(processos)

            self.msg = Label(ws, text=processos, bg=color, width=80, height=20)
            self.msg["font"] = ("Verdana", "5", "italic", "bold")
            self.msg.place(x=40, y=250)

        self.msg = Label(ws, text=self.numero_cpu, bg=color)
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.place(x=40, y=80)

        self.msg = Label(ws, text=self.frequencia_cpu, bg=color)
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.place(x=40, y=120)

        self.msg = Label(ws, text=self.processos, bg=color)
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.place(x=40, y=180)

        '''
        plt.style.use('_mpl-gallery')
        self.xpoints = ([(float(psutil.cpu_freq().min)), 2, 6, 8])
        self.ypoints = np.array([3, 8, 1, (float(psutil.cpu_freq().max))])

        plt.plot(self.xpoints, self.ypoints)
        plt.show()
        plt.autoscale()
        '''

ws = Tk()
ws.title('Laranja')
icon = PhotoImage(master=ws, file='orange.png')
ws.wm_iconphoto(True, icon)
ws.geometry('600x600+400+50')
color = '#ffa525'
ws.config(bg='#ffa500')
Application(ws)
ws.mainloop()
