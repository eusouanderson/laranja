from tkinter import Button, Frame, Label, PhotoImage, Tk, ttk
import tkinter as tk


class Software:

    def __init__(self, color, colorbutton, msg, msg1):
        self.color = color
        self.ws = tk.Tk()
        width = self.ws.winfo_screenwidth() - 500
        height = self.ws.winfo_screenheight() - 100
        self.ws.geometry("%dx%d" % (width, height))
        self.ws.overrideredirect(True)
        self.icon = PhotoImage(master=self.ws, file='orange.png')

        self.img = PhotoImage(file='orange.png')
        self.img1 = Label(self.ws, image=self.img, background=color)
        self.img1.pack()

        self.ws.wm_iconphoto(True, self.icon)
        self.ws.config(bg=self.color)

        self.widget = Frame(self.ws)
        self.widget.pack(side='bottom')

        self.bto = Button(self.widget, bg=colorbutton, activebackground=self.color, bd=1, borderwidth=4
                          )
        self.bto['text'] = 'Pesquisar'
        self.bto['command'] = self.func
        self.bto.grid(row=0, column=0)

        self.bto = Button(self.widget, bg=colorbutton, activebackground=self.color, bd=1, borderwidth=4
                          )

        self.bto['text'] = 'N sei'
        self.bto['command'] = self.widget.quit
        self.bto.grid(row=0, column=1)

        self.bto = Button(self.widget, bg=colorbutton, activebackground=self.color, bd=1, borderwidth=4
                          )

        self.bto['text'] = 'N sei2'
        self.bto['command'] = self.widget.quit
        self.bto.grid(row=0, column=2)

        self.ws.mainloop()

    def func(self):
        self.msg = Label(self.ws, bg=color)
        self.msg['text'] = "Numero de Processadores"
        self.msg['font'] = font
        self.msg.place(x=20, y=60)

        self.msg = Label(self.ws, bg=color)
        self.msg['text'] = "Frequencia do Processador"
        self.msg['font'] = font
        self.msg.place(x=20, y=100)

        self.msg = Label(self.ws, bg=color)
        self.msg['text'] = 'Processos abertos'
        self.msg['font'] = font
        self.msg.place(x=20, y=140)

    def colorir(self):
        if self.colorir:
            self.color = orcolor
        else:
            self.color = vicolor
        self.ws.update()
        return


informação = "Numero de Processadores"
font = 'Calibri', '10'
msg = 'Sair'
msg1 = 'Pesquisar'
orcolor = '#ffa525'
vicolor = '#bf00ff'
rubcolor = '#e0115f'
darkcolor = '#000'
color = vicolor

App = Software(color=vicolor, colorbutton=orcolor, msg=msg, msg1=msg1)
