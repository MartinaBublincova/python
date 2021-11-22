import tkinter


canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()


x, y = 50, 50
a1, a2 = 180, 100
s = (a1/2)+y
s1 = (a1/2)+x
canvas.create_rectangle(s1-(a1/2), s-(a1/2), s1-(a1/2) +
                        a1, s-(a1/2)+a1, fill="indian red")
canvas.create_rectangle(s1-(a2/2), s-(a2/2), s1-(a2/2) +
                        a2, s-(a2/2)+a2, fill="light blue")
canvas.create_text(s1-(a1/2)-5, s+(a1/2), text="A")
canvas.create_text(s1-(a1/2)-5, s-(a1/2)-5, text="D")
canvas.create_text(s1+(a1/2)+5, s+(a1/2), text="C")
canvas.create_text(s1+(a1/2)+5, s-(a1/2)-5, text="B")
canvas.create_text(s1+(a1/2)+15, s, text=str(a1))
canvas.create_text(s1, s+(a2/2)-10, text=str(a2))

tkinter.mainloop()
