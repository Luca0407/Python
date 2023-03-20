import random
import tkinter

window = tkinter.Tk()

colors = ['blue', 'red', 'yellow', 'orange', 'purple', 'black', 'white', 'green']

for x in range(0, 10):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors) - 1)
    label = tkinter.Label(window, text=":)", bg=colors[color], fg=colors[color2])
    label.place(x=random.randint(0, 100), y=random.randint(0, 100))

window.mainloop()
