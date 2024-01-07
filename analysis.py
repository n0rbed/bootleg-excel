import csv
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from scipy.stats import norm
from scipy.stats import multivariate_normal
import math
from mpl_toolkits.mplot3d import Axes3D


import gui
gname = gui.gname
color = gui.color
style_selection = gui.style_selection
final_choice = gui.final_choice

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

    print(style_selection)
    plt.plot(x_new, ((np.exp(eq[1]))*np.exp(x_new*eq[0])), linestyle=style_selection)


def style(d, x_title, y_title, style_t, Color):
    if d == 2:
        plt.xlabel(x_title)
        plt.ylabel(y_title)
        plt.grid(visible=final_choice['grid'], which='major')

    plt.style.use(style_t)
    plt.gca().get_lines()[0].set_color(Color)

    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title(gname)


