from random import randint
from tkinter import *
from psutil import *
import matplotlib.pyplot as plt
import numpy as np



class Software:
    def __init__(self, colorbutton, color, colorletra):
        self.colorL = colorletra
        self.colorB = colorbutton
        self.color = color
        self.ws = Tk()
        self.ws.title('Laranja')
        width = self.ws.winfo_screenwidth() - 500
        height = self.ws.winfo_screenheight() - 110
        self.ws.geometry('%dx%d' % (width, height))
        self.ws.overrideredirect(True)
        self.ws.attributes('-transparentcolor', 'grey', '-alpha', 8)

        self.icon = PhotoImage(master=self.ws, file='Screenshots/orange.png')
        self.img = PhotoImage(file='Screenshots/orange.png')

        self.img1 = Label(self.ws, image=self.img, bg=color)
        self.img1.pack()

        self.ws.wm_iconphoto(True, self.icon)
        self.ws.config(bg=color)

        self.widget = Frame(self.ws)
        self.widget.pack(side='bottom')

        self.bto1 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto1['text'] = 'Investigate'
        self.bto1['command'] = self.scanner
        self.bto1.grid(row=0, column=0)

        self.bto2 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto2['text'] = 'Grafico'
        self.bto2['command'] = self.graphic
        self.bto2.grid(row=0, column=1)


        self.bto3 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto3['text'] = 'Otmizar'
        self.bto3['command'] = ''
        self.bto3.grid(row=0, column=2)

        self.bto4 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto4['text'] = 'FPS'
        self.bto4['command'] = ''
        self.bto4.grid(row=0, column=3)

        self.bto5 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto5['text'] = 'Net Control'
        self.bto5['command'] = ''
        self.bto5.grid(row=0, column=4)

        self.bto6 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto6['text'] = 'Ping'
        self.bto6['command'] = ''
        self.bto6.grid(row=0, column=5)

        self.bto7 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto7['text'] = 'Color'
        self.bto7['command'] = ''
        self.bto7.grid(row=0, column=6)

        self.bto8 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto8['text'] = 'Sair'
        self.bto8['command'] = self.widget.quit
        self.bto8.grid(row=0, column=7)
        self.ws.mainloop()

    def scanner(self):
        self.msg = Label(self.ws, bg=self.color, background=self.color)
        self.msg['text'] = 'Numero de Processadores'
        self.msg['font'] = font
        self.msg.place(x=20, y=60)

        self.msg = Label(self.ws, bg=self.color, background=self.color)
        self.msg['text'] = 'Frequencia do Processador'
        self.msg['font'] = font
        self.msg.place(x=20, y=100)

        self.msg = Label(self.ws, bg=self.color, background=self.color)
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

        self.msg = Label(self.ws, text=self.numero_cpu, bg=self.color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=40, y=80)

        self.msg = Label(self.ws, text=self.frequencia_cpu, bg=self.color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=40, y=120)

        self.msg = Label(self.ws, text=self.processos, bg=self.color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=40, y=160)
        self.ws.mainloop()

    def graphic(self):
        self.ws2 = Tk()
        width = 500
        height = 500
        self.ws2.geometry('%dx%d' % (width, height))
        self.ws2.overrideredirect(False)
        self.icon = PhotoImage(master=self.ws2, file='Screenshots/orange.png')
        for c in range(0, 5):
                plt.style.use('_mpl-gallery')

                # make data:
                np.random.seed(3)
                x = 0.5 + np.arange(8)
                y = np.random.uniform(2, 7, len(x))

                # plot
                fig, ax = plt.subplots()

                ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

                ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                       ylim=(0, 8), yticks=np.arange(1, 8))

                plt.show()

        return self.ws


font = 'Calibri', '10'
orcolor = '#00ff51'
vicolor = '#bf00ff'
rubcolor = '#e0115f'
darkcolor = '#000'
redcolor = '#ff0000'
brcolor = '#ffffff'

App = Software(colorbutton=rubcolor, color=brcolor, colorletra=redcolor)
