import tkinter

canvas = tkinter.Canvas(height=250, width=375)
canvas.pack()

x, y = 0, 0
a, c = 15, 250
r = 255
g = 0
b = 0

for i in range(0, 25):
    rgb_color = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_rectangle(x, y, x+a, y+c, fill=rgb_color, outline=rgb_color)
    x = x+a
    r = r-10
    b = b+10
tkinter.mainloop()
