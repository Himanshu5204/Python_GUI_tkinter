import tkinter as tk

def add():
    no1 = int(num1txt.get())
    no2 = int(num2txt.get())
    a = no1+no2
    ans.config(text=f"Addition of {no1} and {no2} is {a}")

def sub():
    no1 = int(num1txt.get())
    no2 = int(num2txt.get())
    a = no1-no2
    ans.config(text=f"Subtraction of {no1} and {no2} is {a}")

def mul():
    no1 = float(num1txt.get())
    no2 = float(num2txt.get())
    a = no1*no2
    ans.config(text=f"Multiplication of {no1} and {no2} is {a}")

def div():
    no1 = float(num1txt.get())
    no2 = float(num2txt.get())
    a = no1/no2
    ans.config(text=f"Division of {no1} and {no2} is {a}")



parent = tk.Tk()
parent.title("MY CALCULATOR")
parent.geometry("500x500")

welcommelbl = tk.Label(parent,text="Welcome to my calc").pack()

num1 = tk.Label(parent,text="Enter First number ")
num1.pack(pady=10)
num1txt = tk.Entry(parent)
num1txt.pack()

num2 = tk.Label(parent,text="Enter Second number ")
num2.pack(pady=10)
num2txt = tk.Entry(parent)
num2txt.pack()

btnadd = tk.Button(parent,text="ADD",command=add)
btnadd.pack(pady=10)

btnsub = tk.Button(parent,text="SUB",command=sub)
btnsub.pack(pady=10)

btnmul = tk.Button(parent,text="MUL",command=mul)
btnmul.pack(pady=10)

btndiv = tk.Button(parent,text="DIV",command=div)
btndiv.pack(pady=10)


ans = tk.Label(parent,text="")
ans.pack(pady=20)


