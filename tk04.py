import tkinter

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

n, x, c = 40, 0, 0
a = 10*n
s = a/2

while (x < n+1):
    c = c+1
    if (c > 3):
        c = 1
    r = a/2
    colors = ["red", "blue", "yellow"]
    canvas.create_rectangle(s-r, s-r, s+r, s+r, fill=colors[c-1])
    a = a-10
    x = x+1

tkinter.mainloop()
