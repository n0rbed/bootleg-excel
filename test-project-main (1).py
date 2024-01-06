# tkinter imports
import tkinter
from tkinter import *
import tkinter.filedialog as fd
from tkinter import colorchooser
from tkinter import ttk


# matplotlib imports
import csv
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from scipy.stats import norm
from scipy.stats import multivariate_normal
import math
from mpl_toolkits.mplot3d import Axes3D

filename = None
def main():
    root = tkinter.Tk()
    root.title("bootleg excel")

    # graph name input
    tkinter.Label(root, text="graph name").grid(row=0, column=0, sticky=W, pady=2)

    Gname_input = tkinter.Entry(root)
    Gname_input.grid(row=1, column=0, sticky=W, pady=2)

    def store_Gname():
        global Gname
        Gname = Gname_input.get()

    # file upload
    def upload():
        global filename
        filename = fd.askopenfilename()
        return

    file_upload = tkinter.Button(root, text="upload csv file", command=upload)
    file_upload.grid(row=2, column=0, sticky=W, pady=2, padx=5)

    def graph_type():
        global final_choice
        final_choice = {'grid': False, 'scatter': False, 'linear': False, 'exponential': False, 'polynomial': False,
                        'logarithmic': False, 'n_distribution': False}
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

    # the degree entry
    degree = Entry(root)

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

    # the normal distribution selection
    axis = ['x-axis', 'y-axis', 'both']
    selection_ndist = ttk.Combobox(state="readonly", values=axis)

    def ndist_select():
        selection_ndist.grid(row=5, column=2, sticky=W, pady=2)

    def choose_ndist_asix():
        global ndist_axis
        ndist_axis = selection_ndist.get()

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

    def get_selection():
        global style_selection
        style_selection = selection_box.get()
        return style_selection

    # give it a label
    Label(root, text="choose line style").grid(row=6, column=0, sticky=W, pady=2)
    selection_box = ttk.Combobox(state="readonly", values=style_options)
    selection_box.grid(row=7, column=0, sticky=W, pady=2)

    #colour selection

    def choose_color_1():
        global col1
        color_code = colorchooser.askcolor(title="Choose color")
        if len(color_code) == 0:
            col1 = "#0000ff"
        else:
            col1 = str(color_code[1])

    col_choice_point = ttk.Button(text="choose color of line", command=choose_color_1)
    col_choice_point.grid(row=8, column=0, sticky=W, pady=2)

    def validate():
        # some required fields checked
        if Gname_input.get() == '' or filename == None :
            tkinter.messagebox.showwarning("Error", "missing fields")
            # if final_choice['linear'] == True or final_choice['exponential'] == True or final_choice[
            #     'polynomial'] == True or final_choice['logarithmic'] == True or final_choice['n_distribution'] == True:
        else:
            store_Gname()
            graph_type()
            get_selection()

            # if pol selected:
            if final_choice['polynomial']:
                get_pol_degree()

            # if ndist is selected:
            if final_choice['n_distribution']:
                choose_ndist_asix()

            root.destroy()
            global Color
            Color = col1
            return Color

    Final_Button = tkinter.Button(root, text="submit", command=validate)
    Final_Button.grid(row=9, pady=2)

    tkinter.mainloop()


main()
# print(filename)
# print(final_choice)
# print(Gname)
# print(Color)
# print(ndist_axis)


def calc_mean(var_list):
    counter = 0
    sum = 0
    for num in var_list:
        sum += num
        counter += 1
    mean = sum/counter
    return mean

def calc_stdev(var_list, mean):
    sum_variance = 0
    counter = 0
    for num in var_list:
        sum_variance += (num - mean)**2
        counter += 1
    stdev = math.sqrt(sum_variance / (counter-1))
    return stdev


def getx_values(data_list):
    x_list = []
    for xyvalue in data_list:
        x_list.append(float(xyvalue[0]))
    return x_list


def gety_values(data_ls):
    y_list = []
    for xyvalue in data_ls:
        y_list.append(float(xyvalue[1]))
    return y_list

def graph_polynomial(data_list, degree):
    x = np.array(getx_values(data_list))
    y = np.array(gety_values(data_list))

    if final_choice['scatter']:
        plt.scatter(x, y)

    # calculate equation for the graph (this is a polynomial)
    z = np.polyfit(x, y, degree)
    p = np.poly1d(z)

    x_new = np.linspace(x.min(), x.max(), 100)



    # add trendline to plot
    plt.plot(x_new, p(x_new), linestyle=style_selection)

def graph_normal_distribution(data_list, yx_or_both, x_title, y_title):
    x_data = []
    y_data = []
    mean = 0
    stdev = 0

    for row in data_list:
        x_data.append(float(row[0]))
        y_data.append(float(row[1]))

    if yx_or_both == 'both':
        meanx = calc_mean(x_data)
        stdevx = calc_stdev(x_data, meanx)

        meany = calc_mean(y_data)
        stdevy = calc_stdev(y_data, meany)

        x = np.linspace((meanx-(4*stdevx)), (meanx+(4*stdevx)), 500)
        y = np.linspace((meany-(4*stdevy)), (meany+(4*stdevy)), 500)
        X, Y = np.meshgrid(x, y)

        pos = np.empty(X.shape + (2,))
        pos[:, :, 0] = X; pos[:, :, 1] = Y
        rv = multivariate_normal([meanx, meany], [[stdevx, 0], [0, stdevy]])

        # Make a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(X, Y, rv.pdf(pos),cmap='viridis',linewidth=0, label=f"μx = {meanx}, σx = {round(stdevx, 3)}, μy = {meany}, σy = {round(stdevy, 3)}")
        ax.set_xlabel(x_title)
        ax.set_ylabel(y_title)
        ax.set_zlabel('Probability')
        if final_choice['grid']:
            ax.grid(b=True, which='major', linestyle='-')
        plt.legend(loc="upper right")


        return

    if yx_or_both == 'x-axis':
        mean += calc_mean(x_data)
        stdev += calc_stdev(x_data, mean)

    elif yx_or_both == 'y-axis':
        mean += calc_mean(y_data)
        stdev += calc_stdev(y_data, mean)

    # defining the domain of the plot
    start = mean - (4*stdev)
    end = mean + (4*stdev)

    # getting x values and their corresponding probabilities using the normal function
    x = np.linspace(start, end, 1000)
    prob = norm.pdf(x, mean, stdev)


    if final_choice['scatter']:
        plt.scatter(x_data, norm.pdf(x_data, mean, stdev))

    # plotting the results
    plt.plot(x, prob, linestyle=style_selection, label=f"μ = {mean}, σ = {round(stdev, 3)}")
    plt.legend()
    plt.axvline(mean, ls='--', color='lightgray')


def graph_logarithmic(data_list):
    x = np.array(getx_values(data_list))
    y = np.array(gety_values(data_list))

    if final_choice['scatter']:
        plt.scatter(x, y)

    eq = np.polyfit(np.log(x), y, 1)
    x_new = np.linspace(x.min(), x.max(), 1000)
    plt.plot(x_new, (((eq[0]*np.log(x_new)) + eq[1])), linestyle=style_selection)




def graph_exponential(data_list):
    x = np.array(getx_values(data_list))
    y = np.array(gety_values(data_list))

    if final_choice['scatter']:
        plt.scatter(x, y)

    eq = np.polyfit(x, np.log(y), 1, w=np.sqrt(y))

    x_new = np.linspace(x.min(), x.max(), 1000)

    plt.plot(x_new, ((np.exp(eq[1]))*np.exp(x_new*eq[0])), linestyle=style_selection)


def style(d, x_title, y_title, style_selection, Color):
    if d == 2:
        plt.xlabel(x_title)
        plt.ylabel(y_title)
        plt.grid(visible=final_choice['grid'], which='major')

    plt.style.use(style_selection)
    plt.gca().get_lines()[0].set_color(Color)

    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title(Gname)

with (open(filename, 'r') as csvfile):
    csv_reader = csv.reader(csvfile)
    data_list = list(csv_reader)

    x_title = data_list[0][0]
    y_title = data_list[0][1]
    data_list.pop(0)
    plt.style.use('Solarize_Light2')

    scatter = final_choice['scatter']

    if final_choice['linear']:
        graph_polynomial(data_list, 1)
        style(2, x_title, y_title, 'Solarize_Light2', Color)

    if final_choice['logarithmic']:
        graph_logarithmic(data_list)
        style(2, x_title, y_title, 'Solarize_Light2', Color)


    if final_choice['exponential']:
        graph_exponential(data_list)
        style(2, x_title, y_title, 'Solarize_Light2', Color)


    if final_choice['polynomial']:
        graph_polynomial(data_list, pol_deg)
        style(2, x_title, y_title, 'Solarize_Light2', Color)

    if final_choice['n_distribution']:
        graph_normal_distribution(data_list, ndist_axis, x_title, y_title)


plt.show()



# To do list:
# move all the functions at the beginning of the code, then run the "main code" seperatly as your
# TA told you
# make the program write the equation it graphed, the mean, median and the mode of each column of
# data into a file seperate from the csv the user inputted
