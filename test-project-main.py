import tkinter
from tkinter import *
import tkinter.filedialog as fd
from tkinter import colorchooser
from tkinter import ttk


def main():
    root = tkinter.Tk()
    root.title("bootleg excel")

    Gname_input = tkinter.Entry(root)
    Gname_input.pack()

    tkinter.Label(root, text="graph name").pack()

    filename = None

    def store_Gname():
        global Gname
        Gname = Gname_input.get()

    def graph_type():
        global final_choice
        final_choice = {'grid': False, 'scatter': False, 'linear': False, 'exponential': False, 'polynomial': False,
                        'logarithmic': False, 'n_distribution': False}
        grid = CheckVar2.get()
        scat = CheckVar1.get()
        lin = CheckVar3.get()
        exp = CheckVar4.get()
        poly = CheckVar3.get()
        log = CheckVar3.get()
        ndist = CheckVar3.get()
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

    def upload():
        global filename
        filename = fd.askopenfilename()
        return

    def choose_color_1():
        global col1
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code == '':
            col1 = "#0000ff"
        else:
            col1 = str(color_code[1])

    def validate():
        # some required fields checked
        if Gname_input.get() == '' and (not filename):
            # if final_choice['linear'] == True or final_choice['exponential'] == True or final_choice[
            #     'polynomial'] == True or final_choice['logarithmic'] == True or final_choice['n_distribution'] == True:
            tkinter.messagebox.showwarning("Error", "missing fields")
        else:
            store_Gname()
            graph_type()
            get_selection()
            get_pol_degree()
            choose_ndist_asix()
            root.destroy()
            global Color
            Color = col1
            return Color

    # def submit():
    # store_Gname()
    # graph_type()
    # validate()
    # root.destroy()

    file_upload = tkinter.Button(root, text="upload", command=upload)
    file_upload.pack()
    degree = Entry(root)

    def showDeg():
        degree.pack()

    def des_lin():
        exponential_checkbox.deselect()
        polynomial_checkbox.deselect()
        logarithmic_checkbox.deselect()
        n_distribution_checkbox.deselect()
        degree.pack_forget()
        selection_ndist.pack_forget()

    def des_exp():
        linear_checkbox.deselect()
        polynomial_checkbox.deselect()
        logarithmic_checkbox.deselect()
        n_distribution_checkbox.deselect()
        degree.pack_forget()
        selection_ndist.pack_forget()

    def des_poly():
        linear_checkbox.deselect()
        exponential_checkbox.deselect()
        logarithmic_checkbox.deselect()
        n_distribution_checkbox.deselect()
        selection_ndist.pack_forget()

    def des_log():
        linear_checkbox.deselect()
        exponential_checkbox.deselect()
        polynomial_checkbox.deselect()
        n_distribution_checkbox.deselect()
        degree.pack_forget()
        selection_ndist.pack_forget()

    def des_ndist():
        linear_checkbox.deselect()
        exponential_checkbox.deselect()
        polynomial_checkbox.deselect()
        logarithmic_checkbox.deselect()
        degree.pack_forget()

    axis = ['x-axis', 'y-axis', 'both']
    selection_ndist = ttk.Combobox(state="readonly", values=axis)

    def ndist_select():
        selection_ndist.pack()

    CheckVar2 = tkinter.StringVar()
    CheckVar1 = tkinter.StringVar()
    CheckVar3 = tkinter.StringVar()
    CheckVar4 = tkinter.StringVar()
    CheckVar5 = tkinter.StringVar()
    CheckVar6 = tkinter.StringVar()
    CheckVar7 = tkinter.StringVar()
    grid_checkbox = tkinter.Checkbutton(root, text="Grid", variable=CheckVar2, onvalue="grid", offvalue="")
    scatter_checkbox = tkinter.Checkbutton(root, text="scatterplot", variable=CheckVar1, onvalue="scatter", offvalue="")
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

    grid_checkbox.pack()
    scatter_checkbox.pack()
    Label(root, text="Trendlines").pack()
    linear_checkbox.pack()
    exponential_checkbox.pack()
    polynomial_checkbox.pack()

    logarithmic_checkbox.pack()
    n_distribution_checkbox.pack()

    def choose_ndist_asix():
        global ndist_axis
        ndist_axis = selection_ndist.get()

    def get_pol_degree():
        global pol_deg
        pol_deg = degree.get()
        return pol_deg

    options = ['dashed', 'solid']

    def get_selection():
        global style_selection
        style_selection = selection_box.get()
        return style_selection

    selection_box = ttk.Combobox(state="readonly", values=options)
    selection_box.pack()

    #        color_picked.configure(text=col1)

    # def choose_color_2():
    #     color_code = colorchooser.askcolor(title="Choose color")
    #     col2 = str(color_code[1])

    col_choice_point = ttk.Button(text="choose color of point", command=choose_color_1)
    col_choice_point.pack()

    #    color_picked = tkinter.Label(root, text="").pack
    Final_Button = tkinter.Button(root, text="submit", command=validate)
    Final_Button.pack()

    tkinter.mainloop()


main()
print(filename)
print(final_choice)
print(Gname)
print(style_selection)
print(ndist_axis)
print(Color)
