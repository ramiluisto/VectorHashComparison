import matplotlib.pyplot as plt
import numpy as np
import json
import os



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


def main():
    json_filenames =  [filename for filename in os.listdir('./data/') if filename[-4:]=='json']
    a, b, c, d = json_filenames
    json_filenames = [d,a,c,b]

    for filename in json_filenames:
        create_a_picture_from_data(filename)



    simple_int_results = {}
    x_lengths = set()
    for filename in json_filenames:
        with open('./data/'+filename, 'r') as infile:
            data = dict(json.load(infile))
        results = data['simple_int']
        simple_int_results[filename] = data['simple_int']


        fileroot = filename.split('.')[0]
        int_number = fileroot.split('-')[-1]
        
        x = np.array(range(2, len(results)+2))
        y = np.array(results)
        plt.plot(x, y, label = 'max_int = {}'.format(int_number))
        plt.legend(loc = 'upper left')
        plt.title('How the integer range affects the timing.')
        plt.xlabel("Vector dimension")
        plt.ylabel("Set filling time in ms.")

    plt.savefig('./img/ComparisonImg.png')
    plt.show()
        
        
if __name__ == '__main__':
    main()
        
        


    




