import tkinter
canvas =  tkinter.Canvas(height=480,width = 640,bg="lightblue")
canvas.pack()
def kresli_gulu1(x,y,r):                 # r je polomer gule
    return canvas.create_oval(x+r,y+r,x-r,y-r,fill="white",outline="black")
def kresli_gulu2(x,y,r):           
    return canvas.create_oval(x+r,y+r,x-r,y-r,fill="white",outline="black")
def kresli_gulu3(x,y,r):               
    return canvas.create_oval(x+r,y+r,x-r,y-r,fill="white",outline="black")

def kresli_snowmana():
    print(kresli_gulu1(320,380,90))
    print(kresli_gulu2(320,250,70))
    print(kresli_gulu3(320,150,30))

kresli_snowmana()
canvas.mainloop()
