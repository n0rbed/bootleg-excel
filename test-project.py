import tkinter
import tkinter.filedialog as fd

def main():
    root = tkinter.Tk()
    root.title("bootleg excel")

    inputtxt = tkinter.Entry(root)
    inputtxt.pack()

    lbl_Gname = tkinter.Label(root, text = "graph name").pack()
    filename = None
    def store_Gname():
        Gname = inputtxt.get()
        return Gname

    def type():
        global final_choice
        final_choice = {'grid': False, 'scatter': False}
        grid = CheckVar2.get()
        scat = CheckVar1.get()
        if grid != "":
            final_choice['grid']= True
        if scat != "":
            final_choice['scatter'] = True

    def upload():
        global filename
        filename = fd.askopenfilename()
        return

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

    def submit():
        store_Gname()
        type()
        validate()
        root.destroy()

    file_upload = tkinter.Button(root, text="upload", command=upload)
    file_upload.pack()

    CheckVar2 = tkinter.StringVar()
    CheckVar1 = tkinter.StringVar()
    grid_checkbox = tkinter.Checkbutton(root, text = "Grid", variable = CheckVar2, onvalue="grid", offvalue="")
    scatter_checkbox = tkinter.Checkbutton(root, text = "scatterplot", variable = CheckVar1, onvalue="scatter", offvalue="")

    grid_checkbox.pack()
    scatter_checkbox.pack()

    Final_Button = tkinter.Button(root, text="submit", command=submit)
    Final_Button.pack()

    tkinter.mainloop()


main()
print(filename)
print(final_choice)
