import tkinter
import random
canvas = tkinter.Canvas(height=480,width=640,bg="gray")
canvas.pack()

def farba(vzd):
    x =255- int((vzd/400)*255)
    return  "#{:02x}{:02x}{:02x}".format(x,x,x)
def vzdialenost(x,y):
    return ((x-320)**2 +(y-240)**2)**0.5
def vytvor_stvorec(x,y,velkost,farba):
    suradnice = x-velkost/2,y-velkost/2,x+velkost/2,y+velkost/2
    canvas.create_rectangle(suradnice,fill = farba)

for i in range(100):
    x =random.randrange(640)
    y =random.randrange(480)
    vzd = vzdialenost(x,y)
    f = farba(vzd)
    vytvor_stvorec(x,y,vzd/6,f)



canvas.mainloop()
