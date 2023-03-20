import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight=20)
window.columnconfigure(1, weight=20)

lista = ["He leído y acepto los terminos y condiciones",
         "Acepto recibir notificaciones via mail de futuras actualizaciones",
         "Acepto enviar mis datos de uso para mejorar la experiencia de usuario a futuro"]

checking1 = tkinter.StringVar()
checking2 = tkinter.StringVar()
checking3 = tkinter.StringVar()

cb1 = ttk.Checkbutton(window, text=lista[0], variable=checking1)
cb2 = ttk.Checkbutton(window, text=lista[1], variable=checking2)
cb3 = ttk.Checkbutton(window, text=lista[2], variable=checking3)
label = ttk.Label(window, text="(no leiste los terminos y condiciones)")

cb1.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)
cb2.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)
cb3.grid(column=0, row=2, sticky=tkinter.W, padx=5, pady=5)
label.grid(column=1, row=19, sticky=tkinter.SE, ipadx=5, ipady=5)

window.mainloop()
