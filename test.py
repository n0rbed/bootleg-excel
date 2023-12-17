import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import math


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


def getx_values(data_ls):
    x_list = []
    for xyvalue in data_ls:
        x_list.append(int(xyvalue[0]))
    return x_list


def gety_values(data_ls):
    y_list = []
    for xyvalue in data_ls:
        y_list.append(int(xyvalue[1]))
    return y_list

def graph_polynomial(data_list):
    plt.xlabel(x_title)
    plt.ylabel(y_title)

    x = np.array(getx_values(data_list))
    y = np.array(gety_values(data_list))
    plt.scatter(x, y)

    # calculate equation for the graph (this is a polynomial)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)

    x_new = np.linspace(x.min(), x.max(), 100)

    # add trendline to plot
    plt.plot(x_new, p(x_new))

def graph_normal_distribution(data_list, yx_or_both):
    y_data = []
    x_data = []

    for i in data_list:
        y_data.append(data_list[i][1])
        x_data.append(data_list[i][0])

    if yx_or_both == 'y':
        mean = calc_mean(y_data)


    elif yx_or_both == 'x':
        mean = calc_mean(x_data)

    else:
        meanx = calc_mean(x_data)
        meany = calc_mean(y_data)

    

with (open('fakedata.csv', 'r') as csvfile):
    csv_reader = csv.reader(csvfile)
    data_list = list(csv_reader)

    x_title = data_list[0][0]
    y_title = data_list[0][1]
    data_list.pop(0)




plt.show()


# this is a test to see if github is working
