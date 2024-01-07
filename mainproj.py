import csv
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from scipy.stats import norm
from scipy.stats import multivariate_normal
import math
from mpl_toolkits.mplot3d import Axes3D

import gui


gui.maintk()
filename = gui.filename
final_choice = gui.final_choice
color = gui.color
ndist_axis = gui.ndist_axis

from analysis import *


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
        style(2, x_title, y_title, 'Solarize_Light2', color)

    if final_choice['logarithmic']:
        graph_logarithmic(data_list)
        style(2, x_title, y_title, 'Solarize_Light2', color)


    if final_choice['exponential']:
        graph_exponential(data_list)
        style(2, x_title, y_title, 'Solarize_Light2', color)


    if final_choice['polynomial']:
        graph_polynomial(data_list, pol_deg)
        style(2, x_title, y_title, 'Solarize_Light2', color)

    if final_choice['n_distribution']:
        graph_normal_distribution(data_list, ndist_axis, x_title, y_title)


plt.show()



# To do list:
# move all the functions at the beginning of the code, then run the "main code" seperatly as your
# TA told you
# make the program write the equation it graphed, the mean, median and the mode of each column of
# data into a file seperate from the csv the user inputted
