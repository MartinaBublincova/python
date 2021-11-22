import tkinter

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

height = 220
width = 200
s = 120
c = 0


for i in range(4):

    colours = ["dark green", "green", "lime green", "yellow green"]
    canvas.create_rectangle(s-width/2, height, s+width /
                            2, height-50, fill=colours[c])
    height = height-50
    width = width-50
    c = c+1
tkinter.mainloop()
