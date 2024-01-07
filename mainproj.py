import csv
import matplotlib.pyplot as plt
from matplotlib import style

import gui
gui.maintk()
filename = gui.filename
final_choice = gui.final_choice
gname = gui.gname
color = gui.color

# importing analysis after gui.maintk() is ran is crucial
# in order for the gui import in the analysis file to be correct.
from data_plotting import *


with (open(filename, 'r') as csvfile):
    csv_reader = csv.reader(csvfile)
    data_list = list(csv_reader)

    x_title = data_list[0][0]
    y_title = data_list[0][1]
    data_list.pop(0)
    plt.style.use('Solarize_Light2')

    scatter = final_choice['scatter']

    output_file = filename[:-4] + '.txt'

    with (open(output_file, 'w') as f):

        if final_choice['linear']:
            equation = graph_polynomial(data_list, 1)
            f.write(f'Equation:\n{equation}')
            style(2, x_title, y_title, 'Solarize_Light2', color)

        if final_choice['logarithmic']:
            equation = graph_logarithmic(data_list)
            f.write(f'Equation:\n{equation}')
            style(2, x_title, y_title, 'Solarize_Light2', color)


        if final_choice['exponential']:
            equation = graph_exponential(data_list)
            f.write(f'Equation:\n{equation}')
            style(2, x_title, y_title, 'Solarize_Light2', color)


        if final_choice['polynomial']:
            equation = graph_polynomial(data_list, gui.pol_deg)
            f.write(f'Equation:\n{equation}')
            style(2, x_title, y_title, 'Solarize_Light2', color)

        if final_choice['n_distribution']:
            output_n = graph_normal_distribution(data_list, gui.ndist_axis, x_title, y_title)
            f.write(f'Data used:\n{output_n}')




plt.show()


