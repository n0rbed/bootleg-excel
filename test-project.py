import tkinter
import tkinter.filedialog as fd

root = tkinter.Tk()
root.title("bootleg excel")

inputtxt = tkinter.Entry(root)
inputtxt.pack()

lbl_Gname = tkinter.Label(root, text = "graph name").pack()
def store_Gname():
    Gname = inputtxt.get()
    return Gname

def type():
    final_choice = []
    grid = CheckVar2.get()
    scat = CheckVar1.get()
    if grid != "0":
        final_choice.append(grid)
    if scat != "0":
        final_choice.append(scat)
    print(scat)
    print(final_choice)

def upload():
    filename = fd.askopenfilename()
    return filename

# def theOnlyFuncIprobablyNeedToT():
#     pass

def validate():
    #some required fields checked
    if len(inputtxt.get()) != 0:
        store_Gname()
        type()
    else:
        pass
        #gives error message

B = tkinter.Button(root, text="upload", command=upload)
B.pack()

CheckVar2 = tkinter.StringVar()
CheckVar1 = tkinter.StringVar()
A = tkinter.Checkbutton(root, text = "Grid", variable = CheckVar2, onvalue="grid", offvalue="0")
M = tkinter.Checkbutton(root, text = "scatterplot", variable = CheckVar1, onvalue="scatter", offvalue="0")

A.pack()
M.pack()

Final_Button = tkinter.Button(root, text="submit", command=lambda:[store_Gname(), type(), validate()])
Final_Button.pack()

tkinter.mainloop()