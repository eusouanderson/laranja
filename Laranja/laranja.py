from random import randint
from tkinter import *
import pygame
from psutil import *




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
        self.ws.overrideredirect(False)
        self.ws.attributes('-transparentcolor', 'grey', '-alpha', 8)

        self.icon = PhotoImage(master=self.ws, file='orange.png')
        self.img = PhotoImage(file='orange.png')

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
        self.bto2 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto3 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto4 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto5 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto6 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto7 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )
        self.bto8 = Button(
            self.widget,
            bg=self.colorB,
            activebackground=self.color,
            bd=1,
            borderwidth=4,
            width=10,
            fg=brcolor,
        )

        def upcolor():
            self.ws.config = vicolor
            return



        def FPS():

            self.ws1 = Tk()
            width = 50
            height = 50
            self.ws1.geometry('%dx%d' % (width, height))
            self.ws1.attributes('-topmost', 'true')
            self.ws1.overrideredirect(True)
            self.ws1.attributes('-transparentcolor', 'grey', '-alpha', 8)
            self.img1 = Label(self.ws1, bg=self.color, height=height, width=width)
            self.img1.pack()
            clock = pygame.time.Clock()
            while True:
                clock.tick()

                self.img1['text'] = clock.get_fps()
                break



        self.bto1['text'] = 'Investigate'
        self.bto1['command'] = self.scanner
        self.bto1.grid(row=0, column=0)

        self.bto2['text'] = 'Grafico'
        self.bto2['command'] = self.graphic
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
        width = self.ws.winfo_screenwidth()
        height = self.ws.winfo_screenheight()
        self.ws2.geometry('%dx%d' % (width, height))
        self.ws2.overrideredirect(True)
        self.icon = PhotoImage(master=self.ws2, file='orange.png')

        return self.ws


font = 'Calibri', '10'
orcolor = '#00ff51'
vicolor = '#bf00ff'
rubcolor = '#e0115f'
darkcolor = '#000'
redcolor = '#ff0000'
brcolor = '#ffffff'

App = Software(colorbutton=vicolor, color=rubcolor, colorletra=redcolor)
