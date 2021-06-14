import matplotlib.pyplot as plt
import numpy as np
import json




def create_a_picture_from_data(filename):

    with open('./data/'+filename, 'r') as infile:
        data = dict(json.load(infile))

        
    simple_int = data['simple_int']
    simple_float = data['simple_float']
    better_int = data['better_int']
    better_float = data['better_float']

    x_range_len = len(simple_int)

    x = np.array(range(2, x_range_len + 2))
    y = x
    
    
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    plt.tight_layout(pad = 2.0)

    fig.set_size_inches(1.62*10, 10)

    axs[0, 0].plot(x, simple_int, label='Simple int')
    axs[0, 0].plot(x, simple_float, label='Simple float')
    axs[0, 0].plot(x, better_int, label='Better int')
    axs[0, 0].plot(x, better_float, label='Better float')
    axs[0, 0].set_title('Time taken to populate a set with {} vectors.'.format(x_range_len))
    axs[0, 0].legend(loc='upper left')

    
    def fit_line_to_data(result, title, axis_coords, x_range = range(2, x_range_len+2)):
        x = np.array(x_range)
        y = np.array(result)
        slope, additive_c = np. polyfit(x, y, 1)
        
        axis_x, axis_y = axis_coords
        
        axs[axis_x, axis_y].plot(x, y, 'o', label='Measurements')
        axs[axis_x, axis_y].plot(x, slope*x + additive_c, label='Best fit')
        
        axs[axis_x, axis_y].set_title(title + "\nSlope {:2f} and constant {:2f}.".format(slope, additive_c))
        axs[axis_x, axis_y].legend(loc='upper left')

        
    fit_line_to_data(simple_int, "SIMPLE INT vector population.", [0,1])
    fit_line_to_data(simple_float, "SIMPLE FLOAT vector population.", [1,0])
    fit_line_to_data(better_int, "BETTER INT vector population.", [1,1])

    
    y = np.array(better_float)
    slope, additive_c = np. polyfit(x, y, 1)
    print("Better float slope is {}.".format(slope))
    
    
    for ax in axs.flat:
        ax.set(xlabel='Vector dimension', ylabel='Set filling time in ms.')


    fileroot = filename.split('.')[0]
    plt.savefig('./img/'+fileroot+'.png')
            
    plt.show()


create_a_picture_from_data('hash_speedtest_dim-2000_intmax-100_vectorlistlen-2.json')
create_a_picture_from_data('hash_speedtest_dim-2000_intmax-100_vectorlistlen-10.json')
create_a_picture_from_data('hash_speedtest_dim-2000_intmax-100_vectorlistlen-20.json')
create_a_picture_from_data('hash_speedtest_dim-2000_intmax-100_vectorlistlen-200.json')
