import tkinter
from tkinter import *
import tkinter.filedialog as fd
from tkinter import colorchooser
from tkinter import ttk


filename = None
final_choice = {'grid': False, 'scatter': False, 'linear': False, 'exponential': False, 'polynomial': False,
                'logarithmic': False, 'n_distribution': False}
style_selection = None
color = None
gname = None
ndist_axis = None

def store_Gname():
    global gname
    gname = Gname_input.get()

# file upload
def upload():
    global filename
    filename = fd.askopenfilename()
    return

def graph_type():
    grid = CheckVar1.get()
    scat = CheckVar2.get()
    lin = CheckVar3.get()
    exp = CheckVar4.get()
    poly = CheckVar5.get()
    log = CheckVar6.get()
    ndist = CheckVar7.get()
    if grid != "":
        final_choice['grid'] = True
    if scat != "":
        final_choice['scatter'] = True
    if lin != "":
        final_choice['linear'] = True
    if exp != "":
        final_choice['exponential'] = True
    if poly != "":
        final_choice['polynomial'] = True
    if log != "":
        final_choice['logarithmic'] = True
    if ndist != "":
        final_choice['n_distribution'] = True

def showDeg():
    degree.grid(row=3, column=2, sticky=W, pady=2)

def get_pol_degree():
    global pol_deg
    try:
        pol_deg = int(degree.get())
    except ValueError:
        tkinter.messagebox.showwarning("Error", "expecting integer")
    return

# checkbox action functions

def des_lin():
    exponential_checkbox.deselect()
    polynomial_checkbox.deselect()
    logarithmic_checkbox.deselect()
    n_distribution_checkbox.deselect()
    degree .grid_forget()
    selection_ndist .grid_forget()

def des_exp():
    linear_checkbox.deselect()
    polynomial_checkbox.deselect()
    logarithmic_checkbox.deselect()
    n_distribution_checkbox.deselect()
    degree .grid_forget()
    selection_ndist .grid_forget()

def des_poly():
    linear_checkbox.deselect()
    exponential_checkbox.deselect()
    logarithmic_checkbox.deselect()
    n_distribution_checkbox.deselect()
    selection_ndist .grid_forget()

def des_log():
    linear_checkbox.deselect()
    exponential_checkbox.deselect()
    polynomial_checkbox.deselect()
    n_distribution_checkbox.deselect()
    degree .grid_forget()
    selection_ndist .grid_forget()

def des_ndist():
    linear_checkbox.deselect()
    exponential_checkbox.deselect()
    polynomial_checkbox.deselect()
    logarithmic_checkbox.deselect()
    degree.grid_forget()


def ndist_select():
    selection_ndist.grid(row=5, column=2, sticky=W, pady=2)

def choose_ndist_asix():
    global ndist_axis
    ndist_axis = selection_ndist.get()


def get_selection():
    global style_selection
    style_selection = selection_box.get()
    return

def choose_color_1():
    global col1
    color_code = colorchooser.askcolor(title="Choose color")
    if len(color_code) == 0:
        col1 = "#0000ff"
    else:
        col1 = str(color_code[1])

def validate():
    x = 0
    for item in final_choice:
        x += final_choice[item]

    graph_type()
    # some required fields checked
    if Gname_input.get() == '' or filename == None or selection_box.get() == '' or x == 0 or col1 == '':
        tkinter.messagebox.showwarning("Error", "missing fields")
        return
    else:
        store_Gname()
        get_selection()

        # if pol selected:
        if final_choice['polynomial']:
            get_pol_degree()

        # if ndist is selected:
        if final_choice['n_distribution']:
            choose_ndist_asix()

        root.destroy()
        global color
        color = col1

def maintk():
    global root
    global grid_checkbox
    global scatter_checkbox
    global linear_checkbox
    global exponential_checkbox
    global polynomial_checkbox
    global logarithmic_checkbox
    global n_distribution_checkbox
    global degree
    global selection_ndist
    global CheckVar1
    global CheckVar2
    global CheckVar3
    global CheckVar4
    global CheckVar5
    global CheckVar6
    global CheckVar7
    global file_upload
    global Gname_input
    global selection_box
    

    root = tkinter.Tk()
    root.title("bootleg excel")

    # graph name input
    tkinter.Label(root, text="graph name").grid(row=0, column=0, sticky=W, pady=2)

    Gname_input = tkinter.Entry(root)
    Gname_input.grid(row=1, column=0, sticky=W, pady=2)

    file_upload = tkinter.Button(root, text="upload csv file", command=upload)
    file_upload.grid(row=2, column=0, sticky=W, pady=2, padx=5)


    # the degree entry
    degree = Entry(root)

    # the normal distribution selection
    axis = ['x-axis', 'y-axis', 'both']
    selection_ndist = ttk.Combobox(state="readonly", values=axis)

    # checkboxes
    CheckVar2 = tkinter.StringVar()
    CheckVar1 = tkinter.StringVar()
    CheckVar3 = tkinter.StringVar()
    CheckVar4 = tkinter.StringVar()
    CheckVar5 = tkinter.StringVar()
    CheckVar6 = tkinter.StringVar()
    CheckVar7 = tkinter.StringVar()


    grid_checkbox = tkinter.Checkbutton(root, text="Grid", variable=CheckVar1, onvalue="grid", offvalue="")
    scatter_checkbox = tkinter.Checkbutton(root, text="scatterplot", variable=CheckVar2, onvalue="scatter", offvalue="")
    linear_checkbox = tkinter.Checkbutton(root, text="linear", variable=CheckVar3, onvalue="linear", offvalue="",
                                          command=des_lin)
    exponential_checkbox = tkinter.Checkbutton(root, text="exponential", variable=CheckVar4, onvalue="exponential",
                                               offvalue="", command=des_exp)
    polynomial_checkbox = tkinter.Checkbutton(root, text="polynomial", variable=CheckVar5, onvalue="polynomial",
                                              offvalue="", command=lambda: [des_poly(), showDeg()])
    logarithmic_checkbox = tkinter.Checkbutton(root, text="logarithmic", variable=CheckVar6, onvalue="logarithmic",
                                               offvalue="", command=des_log)
    n_distribution_checkbox = tkinter.Checkbutton(root, text="n_distribution", variable=CheckVar7,
                                                  onvalue="n_distribution", offvalue="",
                                                  command=lambda: [des_ndist(), ndist_select()])

    # displaying checkboxes
    Label(root, text="Graph style").grid(row=3, column=0, sticky=W, pady=2)
    grid_checkbox.grid(row=4, column=0, sticky=W, pady=2)
    scatter_checkbox.grid(row=5, column=0, sticky=W, pady=2)
    Label(root, text="Trendlines").grid(row=0, column=1, sticky=W, pady=2)
    linear_checkbox.grid(row=1, column=1, sticky=W, pady=2)
    exponential_checkbox.grid(row=2, column=1, sticky=W, pady=2)
    polynomial_checkbox.grid(row=3, column=1, sticky=W, pady=2)
    logarithmic_checkbox.grid(row=4, column=1, sticky=W, pady=2)
    n_distribution_checkbox.grid(row=5, column=1, sticky=W, pady=2)



    # graph style selection box
    style_options = ['dashed', 'solid']

    # give it a label
    Label(root, text="choose line style").grid(row=6, column=0, sticky=W, pady=2)
    selection_box = ttk.Combobox(state="readonly", values=style_options)
    selection_box.grid(row=7, column=0, sticky=W, pady=2)

    #colour selection


    col_choice_point = ttk.Button(text="choose color of line", command=choose_color_1)
    col_choice_point.grid(row=8, column=0, sticky=W, pady=2)


    Final_Button = tkinter.Button(root, text="submit", command=validate)
    Final_Button.grid(row=9, pady=2)

    tkinter.mainloop()

