import tkinter as tk

def calc(event):
    event_text = event.widget.cget("text")
    try:
        if(event_text == "="):
            entry_text = entry.get()
            entry.delete(0,tk.END)
            entry.insert(tk.END,eval(entry_text))

        elif(event_text == "C"):
            entry.delete(0,tk.END)
        else:
            entry.insert(tk.END,event_text)

    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"ERROR..!")

root=tk.Tk()
root.title("calculator")


entry = tk.Entry(root,font=["Arial",22])
entry.pack(fill=tk.BOTH,expand=True)

btnframe = tk.Frame(root)
btnframe.pack()

buttons = ['7','8','8','/',
           '4','5','6','*',
           '1','2','3','-',
           '0','C','=','+']

rows=1
cols=0
for text in buttons:
    btn = tk.Button(btnframe,text=text,font=["Arial",15],padx=20,pady=20)
    btn.grid(row=rows,column=cols)
    cols+=1
    if(cols>3):
        cols=0
        rows+=1

    btn.bind("<Button-1>",calc)
    
