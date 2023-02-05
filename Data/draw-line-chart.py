import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

china_data = np.array([0])


def read_data(file_path):
    table = pd.read_csv(file_path, sep=';')
    return table


def process_data(carbon_emission_list):
    global china_data
    carbon_emission_array = np.array(carbon_emission_list)
    china_data += carbon_emission_array
    return


def draw(country, carbon_emission_list):
    plt.rcParams.update({'font.size': 30})
    plt.figure(figsize=(36, 18))
    carbon_emission_array = np.array(carbon_emission_list)
    # print(carbon_emission_array)
    np.save('./data-by-country/'+country+'.npy', carbon_emission_array)
    print('Save the data of {0} in ./data-by-country/{0}.npy'.format(country))
    year = np.array(list(range(1960, 2022)))
    plt.plot(year, carbon_emission_array, 'o-', linewidth=2)
    plt.title(country, pad=50)
    plt.xlabel('Year', labelpad=20)
    plt.ylabel('Territorial emissions in MtCO₂', labelpad=20)
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(5))
    plt.grid()
    # plt.show()
    # fig = plt.figure()
    # fig.tight_layout()
    file_name = './line-chart-by-country/' + country + '.png'
    plt.savefig(file_name)
    print('Save the line chart of {0} in ./line-chart-by_country/{0}.png'.format(country))
    # exit(0)
    # print(carbon_emission_array)
    return


file = 'original-data-table.csv'
table = read_data(file)
flag = True  # Avoid reading the contents of column 0

for index, value in table.iteritems():
    if flag:
        flag = False
        continue
    if index == 'China':
        china_data = np.array(value)
    elif index == 'Hong Kong' or index == 'Macao' or index == 'Taiwan':
        process_data(value)
    else:
        draw(index, value)

draw('China (included Hong Kong, Macao and Taiwan)', china_data)
