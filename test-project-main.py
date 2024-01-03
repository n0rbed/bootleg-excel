#tkinter imports
import tkinter
from tkinter import *
import tkinter.filedialog as fd
from tkinter import colorchooser
from tkinter import ttk

#matplotlib imports
import csv
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from scipy.stats import norm
from scipy.stats import multivariate_normal
import math
from mpl_toolkits.mplot3d import Axes3D



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
        try:
            pol_deg = int(degree.get())
        except ValueError:
            print('Please enter a valid integer')
        return

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
#print(filename)
#print(final_choice)
#print(Gname)
#print(style_selection)
#print(ndist_axis)
#print(Color)


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
    plt.plot(x_new, p(x_new))

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
    plt.plot(x, prob, label=f"μ = {mean}, σ = {round(stdev, 3)}")
    plt.legend()
    plt.axvline(mean, ls='--', color='lightgray')


def graph_logarithmic(data_list):
    x = np.array(getx_values(data_list))
    y = np.array(gety_values(data_list))

    if final_choice['scatter']:
        plt.scatter(x, y)

    eq = np.polyfit(np.log(x), y, 1)
    x_new = np.linspace(x.min(), x.max(), 1000)
    plt.plot(x_new, (eq[0]*np.log(x_new)) + eq[1])

   


def graph_exponential(data_list):
    x = np.array(getx_values(data_list))
    y = np.array(gety_values(data_list))

    if final_choice['scatter']:
        plt.scatter(x, y)

    eq = np.polyfit(x, np.log(y), 1, w=np.sqrt(y))

    x_new = np.linspace(x.min(), x.max(), 1000)

    plt.plot(x_new, (np.exp(eq[1]))*np.exp(x_new*eq[0]))


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




# add a scatter plot function to modulate the code more


