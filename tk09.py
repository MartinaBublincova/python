import tkinter
import random
canvas = tkinter.Canvas(height=1000, width=300)
canvas.pack()

n, x, y, a, b, total = 44, 20, 20, 50, 20, 0


for i in range(0, n):
    canvas.create_rectangle(x, y, x+a, y+b)
    value = random.choice((1, 2, 5, 10, 20, 50))
    canvas.create_text(x+a/2, y+b/2, text=str(value)+"€")
    total = total+value
    y = y+b+2

canvas.create_text(120, 30, text="Spolu:"+str(total)+"€")

tkinter.mainloop()
