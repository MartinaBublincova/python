import tkinter
canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

x, y = 70, 100
r = 50
dx, dy = 120, 60

canvas.create_oval(x-r, y-r, x+r, y+r, width=15, outline="blue")
canvas.create_oval(x+10, dy+y-r, x+2*r+10, y+dy+r, width=15, outline="yellow")
canvas.create_oval(x+dx-r, y-r, dx+x+r, y+r, width=15)
canvas.create_oval(x+dx+10, dy+y-r, dx+x+2*r+10, y+dy+r,
                   width=15, outline="lime green")
canvas.create_oval(2*dx+x-r, y-r, 2*dx+x+r, y+r, width=15, outline="red")

tkinter.mainloop()
