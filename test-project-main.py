import tkinter
from tkinter import *
import tkinter.filedialog as fd
from tkinter import colorchooser
from tkinter import ttk

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

    def graph_type():
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


    def validate():
        #some required fields checked
        if len(inputtxt.get()) != 0 and (not filename):
            store_Gname()
            graph_type()
            root.destroy()
            get_selection()
        else:
            tkinter.messagebox.showwarning("error", "missing fields")

    def submit():
        store_Gname()
        graph_type()
        validate()
        root.destroy()

    file_upload = tkinter.Button(root, text="upload", command=upload)
    file_upload.pack()
    def des():
        scatter_checkbox.deselect()
    CheckVar2 = tkinter.StringVar()
    CheckVar1 = tkinter.StringVar()
    grid_checkbox = tkinter.Checkbutton(root, text = "Grid", variable = CheckVar2, onvalue="grid", offvalue="", command=des)
    scatter_checkbox = tkinter.Checkbutton(root, text = "scatterplot", variable = CheckVar1, onvalue="scatter", offvalue="")

    grid_checkbox.pack()
    scatter_checkbox.pack()

    options = ['dashed', 'solid']

    def get_selection():
        selection = selection_box.get()
        return selection

    selection_box = ttk.Combobox(state="readonly",values=options)
    selection_box.pack()

    def choose_color_1():
        color_code = colorchooser.askcolor(title="Choose color")
        col1 = str(color_code[1])
        # color_picked.configure(text=col1)
    def choose_color_2():
        color_code = colorchooser.askcolor(title="Choose color")
        col2 = str(color_code[1])

    col_choice_point = ttk.Button(text="choose color of point", command=choose_color_1)
    col_choice_point.pack()

    # color_picked = tkinter.Label(root, text="").pack
    Final_Button = tkinter.Button(root, text="submit", command=validate)
    Final_Button.pack()

    tkinter.mainloop()


main()
print(filename)
print(final_choice)
