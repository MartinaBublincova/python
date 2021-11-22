import tkinter
import math
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()

x, y = 50, 250
a = 280
n = 3-a
v = math.sqrt(a**2-(a/2)**2)
canvas.create_polygon(x, y, x+a, y, x+a/2, y-v, fill="blue")


tkinter.mainloop()
