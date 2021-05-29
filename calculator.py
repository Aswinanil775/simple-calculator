
from tkinter import *

def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnclearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator = ""

windows =Tk()
windows.title("calculator")
operator=""
text_Input=StringVar()
textDisplay=Entry(windows,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg='red',justify='right').grid(columnspan=5)
Button7 =Button(windows,command=lambda:btnclick(7),text="7",bd=8,padx=16,fg="black",font=('arial',20,'bold'))
Button7.grid(row=1,column=0)

Button8 =Button(windows,text="8",command=lambda:btnclick(8),bd=8,padx=16,fg="black",font=('arial',20,'bold'))
Button8.grid(row=1,column=1)
Button9 =Button(windows,text="9",padx=16,command=lambda:btnclick(9),bd=8,fg="black",font=('arial',20,'bold'))
Button9.grid(row=1,column=2)

addition =Button(windows,padx=16,text="+",command=lambda:btnclick("+"),bd=8,fg="black",font=('arial',20,'bold'))
addition.grid(row=1,column=3)

Button4 =Button(windows,padx=16,text="4",bd=8,fg="black",command=lambda:btnclick(4),font=('arial',20,'bold'))
Button4.grid(row=2,column=0)

Button5 =Button(windows,text="5",padx=16,bd=8,fg="black",command=lambda:btnclick(5),font=('arial',20,'bold'))
Button5.grid(row=2,column=1)

Button6 =Button(windows,padx=16,text="6",bd=8,fg="black",command=lambda:btnclick(6),font=('arial',20,'bold'))
Button6.grid(row=2,column=2)

mull =Button(windows,padx=16,text="x",bd=8,fg="black",command=lambda:btnclick("*"),font=('arial',20,'bold'))
mull.grid(row=2,column=3)

Button1 =Button(windows,padx=16,text="1",bd=8,fg="black",command=lambda:btnclick(1),font=('arial',20,'bold'))
Button1.grid(row=3,column=0)

Button2 =Button(windows,padx=16,text="2",bd=8,fg="black",command=lambda:btnclick(2),font=('arial',20,'bold'))
Button2.grid(row=3,column=1)

Button3 =Button(windows,padx=16,text="3",bd=8,fg="black",command=lambda:btnclick(3),font=('arial',20,'bold'))
Button3.grid(row=3,column=2)

minu =Button(windows,padx=16,text="-",bd=8,fg="black",command=lambda:btnclick("-"),font=('arial',20,'bold'))
minu.grid(row=3,column=3)


zero =Button(windows,padx=16,text="0",bd=8,fg="black",command=lambda:btnclick(0),font=('arial',20,'bold'))
zero.grid(row=4,column=0)

point =Button(windows,text=".",padx=16,bd=8,fg="black",command=lambda:btnclick("."),font=('arial',20,'bold'))
point.grid(row=4,column=1)

eq =Button(windows,text="=",bd=8,padx=16,fg="black",command=btnEqualsInput,font=('arial',20,'bold'))
eq.grid(row=4,column=2)

div =Button(windows,text="/",bd=8,padx=16,fg="black",command=lambda:btnclick("/"),font=('arial',20,'bold'))
div.grid(row=4,column=3)

clear =Button(windows,text="AC",padx=16,bd=8,fg="black",command=btnclearDisplay,font=('arial',20,'bold'))
clear.grid(row=5,column=0)

comma =Button(windows,text=",",padx=16,bd=8,fg="black",command=lambda:btnclick(","),font=('arial',20,'bold'))
comma.grid(row=5,column=1)

brak =Button(windows,text="(",padx=16,bd=8,fg="black",command=lambda:btnclick("("),font=('arial',20,'bold'))
brak.grid(row=5,column=2)

brak2 =Button(windows,text=")",padx=16,bd=8,fg="black",command=lambda:btnclick(")"),font=('arial',20,'bold'))
brak2.grid(row=5,column=3)














windows.mainloop()