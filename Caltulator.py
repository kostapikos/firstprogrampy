from tkinter import*

def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
def btnCleardisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
def btnclickokey(numberstrvar):
    global operator
    operator=operator + str(numberstrvar.get)
    text_Input.set(operator)
def sqrtclick():
    global operator
    operator=""
    sqrtt= Tk()
    sqrtt.geometry("250x200")
    numberstrvar = StringVar()
    number = Entry(sqrtt,font=('arial',14,'bold'), textvariable = numberstrvar ,bd=30, insertwidth=5,
                   bg="light blue", justify='center').grid(row=0,columnspan=5)
    sqrtt.title("useless title")

    sqrtokey=Button(sqrtt,font=('arial',14,'bold'), bd=10,text="okey" , bg="red",
                    command=lambda:btnclickokey(numberstrvar.get)).grid(row=1,column=0)
cal = Tk()
cal.title("Calculator By Amethyst")
operator=""
text_Input=StringVar()
#============================================================== First Row 1
txtDisplay = Entry(cal,font=('arial',14,'bold'), textvariable=text_Input, bd=30, insertwidth=5,
                   bg="light blue", justify='right').grid(columnspan=5)
btn7=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="7",bg="blue",command=lambda:btnclick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="8",command=lambda:btnclick(8),bg="blue").grid(row=1,column=1)

btn9=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="9",command=lambda:btnclick(9),bg="blue").grid(row=1,column=2)
plusplus=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="+",command=lambda:btnclick("+"),bg="blue").grid(row=1,column=3)
#================================================================ next row 2
btn4=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="4",command=lambda:btnclick(4),bg="blue").grid(row=2,column=0)

btn5=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="5",command=lambda:btnclick(5),bg="blue").grid(row=2,column=1)

btn6=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="6",command=lambda:btnclick(6),bg="blue").grid(row=2,column=2)

minus=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="-",command=lambda:btnclick("-"),bg="blue").grid(row=2,column=3)
#================================================================ next row 3
btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="1",command=lambda:btnclick(1),bg="blue").grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="2",command=lambda:btnclick(2),bg="blue").grid(row=3,column=1)

btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="3",command=lambda:btnclick(3),bg="blue").grid(row=3,column=2)

pollaplasiasmos=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="*",command=lambda:btnclick("*"),bg="blue").grid(row=3,column=3)
#================================================================ next row 4
btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="0",command=lambda:btnclick(0),bg="blue").grid(row=4,column=0)
btnclear=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="C",bg="blue",command=btnCleardisplay).grid(row=4,column=1)

btnEquals=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="=",bg="blue",command=btnEqualsInput).grid(row=4,column=2)

divine=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="/",command=lambda:btnclick("/"),bg="blue").grid(row=4,column=3)

btnparen1=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="(",command=lambda:btnclick("("),bg="yellow").grid(row=5,column=0)

btnparen2=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text=")",command=lambda:btnclick(")"),bg="yellow").grid(row=5,column=1)
btnpower=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="^",command=lambda:btnclick("**"),bg="yellow").grid(row=5,column=2)
btnpower1=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
            text="√",command=lambda:sqrtclick(),bg="purple").grid(row=5,column=2)
btngap=Button(cal,padx=16,bd=8,fg="black",font=('arial',14,'bold'),
              text="",bg="purple").grid(row=5,column=3)


cal.mainloop()
