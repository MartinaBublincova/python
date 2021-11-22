
import tkinter

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

x, y = 10, 100
d = 20
n = 17
a = 0

for i in range(n):

    if (a != 1):
        canvas.create_line(x, y, x+d, y+d, width=3, fill="blue")
        x = x+d
        a = 1
    else:
        canvas.create_line(x, y+d, x+d, y, width=3, fill="blue")
        x = x+d
        a = 0

tkinter.mainloop()
