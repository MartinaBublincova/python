import tkinter
import math
canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

x, y = 50, 50
a, b = 250, 400
n = 3-a
canvas.create_rectangle(x, y, x+b, y+a, fill="red")
canvas.create_rectangle(x, y, x+b, y+a/2, fill="white")
v = math.sqrt(a**2-(a/2)**2)
canvas.create_polygon(x, y, x, y+a, x+v, y+a/2, fill="navy")


tkinter.mainloop()
