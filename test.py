import csv
import matplotlib.pyplot as plt
import numpy as np


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


with (open('fakedata.csv', 'r') as csvfile):
    csv_reader = csv.reader(csvfile)
    data_list = list(csv_reader)

    x_title = data_list[0][0]
    y_title = data_list[0][1]

    data_list.pop(0)

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

plt.show()

