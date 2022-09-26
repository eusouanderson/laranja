from tkinter import Button, Frame, Label, PhotoImage, Tk, ttk

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.lines import Line2D
from psutil import (Process, cpu_count, cpu_freq, net_io_counters, pids,
                    process_iter)


class Application:
    def __init__(self, master=None):
        self.msg = None
        self.img = PhotoImage(file='orange.png')
        self.widget1 = Frame(master, bg=color)
        self.widget1.pack(side='bottom')
        self.img1 = Label(master, image=self.img, background=color)
        self.img1.pack()

        self.otm = Button(
            self.widget1, bg=color, activebackground=color1, bd=1
        )
        self.otm['text'] = 'Otimizar'
        self.otm['font'] = ('Calibri', '10')
        self.otm['width'] = 10
        self.otm['command'] = ''
        self.otm.pack()

        self.test = Button(
            self.widget1, bg=color, activebackground=color1, bd=1
        )
        self.test['text'] = 'Testar'
        self.test['font'] = ('Calibri', '10')
        self.test['width'] = 10
        self.test['command'] = self.testar
        self.test.pack()

        self.graf = Button(
            self.widget1, bg=color, activebackground=color, bd=1
        )
        self.graf['text'] = 'Gráfico'
        self.graf['font'] = ('Calibri', '10')
        self.graf['width'] = 10
        self.graf['command'] = Scope
        self.graf.pack()

        self.sair = Button(
            self.widget1, bg=color, activebackground=color1, bd=1
        )
        self.sair['text'] = 'Sair'
        self.sair['font'] = ('Calibri', '10')
        self.sair['width'] = 10
        self.sair['command'] = self.widget1.quit
        self.sair.pack()

    def testar(self):
        self.msg = Label(ws, text='Numero de Processadores', bg=color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=20, y=60)

        self.msg = Label(ws, text='Frequencia do Processador', bg=color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=20, y=100)

        self.msg = Label(ws, text='Processos abertos', bg=color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=20, y=150)

        self.pb = ttk.Progressbar(
            ws, orient='horizontal', mode='determinate', length=600, maximum=50
        )
        self.pb.winfo_visual()
        self.pb.place(x=0, y=0)
        self.pb.start()
        if self.pb['value'] < 100:
            self.pb.stop()

        self.numero_cpu = cpu_count()
        self.frequencia_cpu = cpu_freq().current
        self.todosProcessos = pids()
        self.processos = Process()
        self.processos.parent()
        self.processos = len(self.todosProcessos)

        for proc in process_iter(['name']):
            processos = proc.info
            print(processos)

        self.msg = Label(ws, text=self.numero_cpu, bg=color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=40, y=80)

        self.msg = Label(ws, text=self.frequencia_cpu, bg=color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=40, y=120)

        self.msg = Label(ws, text=self.processos, bg=color)
        self.msg['font'] = ('BungeeSpice Regular', '10', 'italic')
        self.msg.place(x=40, y=180)


class Scope:
    def __int__(self, ax, maxt=1, dt=1):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(
            self.tdata,
            self.ydata,
            linewidth=10,
            color='#ffa525',
            gapcolor='red',
            fillstyle='full',
        )
        self.ax.add_line(self.line)
        self.pEnvi = [net_io_counters().packets_sent]
        self.plis = np.array((self.pEnvi[:1]))
        self.lim = 1000
        self.ax.set_ylim(-0.1, self.plis + self.lim + self.lim)
        self.ax.set_xlim(0, self.maxt)

    def update(self, y):

        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_ylim(self.ydata[0], self.ydata[0], self.ydata[0] + 100)
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)

        return (self.line,)


def emitter(p=0.1):
    """Return a random value in [0, 1) with probability p, else 0."""

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

scope = Scope(ax)
ani = animation.FuncAnimation(
    fig, scope.update, emitter, interval=100, blit=False
)
plt.show()


ws = Tk()
ws.overrideredirect(True)
ws.title('Laranja')
icon = PhotoImage(master=ws, file='orange.png')
ws.wm_iconphoto(True, icon)
ws.geometry('600x600+400+50')
color = '#ffa525'
color1 = '#ffa125'
ws.config(bg='#ffa500')
App = Application(ws)

ws.mainloop()
