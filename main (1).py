from tkinter import *

mw = Tk()
mw.title("CALCULATOR")
mw.geometry("300x300")
mw.resizable(False,False)



equation = ""

def show(value):
    global equation
    equation+=value
    db.config(text=equation)

def clear():
    global equation
    equation =  ""
    db.config(text=equation)

def cal():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result = "error"
            equation = ""
    db.config(text=result)
    
db = Label(mw,width=25,text="",font=('arial',30))
db.pack()


b1=Button(mw,text="CLEAR",width=8,height=2,bg="red",command=lambda: clear())
b1.place(x=8,y=50)
b2=Button(mw,text="(",width=8,height=2,bg="yellow",command=lambda: show("("))
b2.place(x=80,y=50)
b3=Button(mw,text=")",width=8,height=2,bg="yellow",command=lambda: show(")"))
b3.place(x=152,y=50)
b16=Button(mw,text="%",width=8,height=2,bg="yellow",command=lambda: show("%"))
b16.place(x=222,y=50)

b4=Button(mw,text="1",width=8,height=2,bg="skyblue",command=lambda: show("1"))
b4.place(x=8,y=100)
b5=Button(mw,text="2",width=8,height=2,bg="skyblue",command=lambda: show("2"))
b5.place(x=80,y=100)
b6=Button(mw,text="3",width=8,height=2,bg="skyblue",command=lambda: show("3"))
b6.place(x=152,y=100)
b17=Button(mw,text="/",width=8,height=2,bg="yellow",command=lambda: show("/"))
b17.place(x=222,y=100)

b7=Button(mw,text="4",width=8,height=2,bg="skyblue",command=lambda: show("4"))
b7.place(x=8,y=150)
b8=Button(mw,text="5",width=8,height=2,bg="skyblue",command=lambda: show("5"))
b8.place(x=80,y=150)
b9=Button(mw,text="6",width=8,height=2,bg="skyblue",command=lambda: show("6"))
b9.place(x=152,y=150)
b18=Button(mw,text="*",width=8,height=2,bg="yellow",command=lambda: show("*"))
b18.place(x=222,y=150)

b10=Button(mw,text="7",width=8,height=2,bg="skyblue",command=lambda: show("7"))
b10.place(x=8,y=200)
b11=Button(mw,text="8",width=8,height=2,bg="skyblue",command=lambda: show("8"))
b11.place(x=80,y=200)
b12=Button(mw,text="9",width=8,height=2,bg="skyblue",command=lambda: show("9"))
b12.place(x=152,y=200)
b19=Button(mw,text="-",width=8,height=2,bg="yellow",command=lambda: show("-"))
b19.place(x=222,y=200)

b13=Button(mw,text=".",width=8,height=2,bg="yellow",command=lambda: show("."))
b13.place(x=8,y=250)
b14=Button(mw,text="0",width=8,height=2,bg="skyblue",command=lambda: show("0"))
b14.place(x=80,y=250)
b15=Button(mw,text="=",width=8,height=2,bg="orange",command=lambda: cal())
b15.place(x=152,y=250)
b20=Button(mw,text="+",width=8,height=2,bg="yellow",command=lambda: show("+"))
b20.place(x=222,y=250)


mw.mainloop()