import tkinter

l = int(input("Pocet stlpcov: "))
r = int(input("Pocet riadkov: "))

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

a = 30
col1, col2 = 'maroon', 'gold'
x, y = 10, 10
m = 3
c = 0

for i in range(0, r):
    for i in range(0, l):
        if (c == 0):
            color = col1
        else:
            color = col2
        canvas.create_rectangle(x, y, x+a, y+a, fill=color)
        x = x+a+m
        c = c+1
        if (c > 1):
            c = 0
    x = 10
    y = y + a + m
    if ((l % 2) == 0):
        if (c == 0):
            c = 1
        else:
            c = 0

tkinter.mainloop()
