import tkinter

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

m = 20
a = 135
b = 90

canvas.create_rectangle(m, m, m+a, m+b, fill="yellow")
canvas.create_rectangle(m, m, m+a, m+b/3*2, fill="red")
canvas.create_rectangle(m, m, m+a, m+b/3, fill="black")

canvas.create_rectangle(2*m+a, m, 2*m+2*a, m+b, fill="red")
canvas.create_rectangle(2*m+a, m, 2*m+a+a/3*2, m+b, fill="white")
canvas.create_rectangle(2*m+a, m, 2*m+a+a/3, m+b, fill="green")


canvas.create_rectangle(m, 2*m+b, m+a, 2*m+2*b, fill="red")
canvas.create_rectangle(m, 2*m+b, m+a/3*2, 2*m+2*b, fill="white")
canvas.create_rectangle(m, 2*m+b, m+a/3, 2*m+2*b, fill="blue")


canvas.create_rectangle(2*m+a, 2*m+b, 2*m+2*a, 2*m+2*b, fill="red")
canvas.create_rectangle(2*m+a, 2*m+b, 2*m+2*a, 2*m+b+b/3*2, fill="blue")
canvas.create_rectangle(2*m+a, 2*m+b, 2*m+2*a, 2*m+b+b/3,  fill="white")

tkinter.mainloop()
