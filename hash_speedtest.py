import json
import random
import time
import numpy as np
import matplotlib.pyplot as plt


from CustomVectors import SimpleVector, BetterVector

VECTOR_LIST_LENGTH = 2000
DIMENSION_MAX = 100
INT_BOUNDS = (0,10)

random.seed(42)


def speed_test(vector_collection, vector_type, verbose = False):
    if verbose: print("Doing test on {}.".format(vector_type.__name__))
    tic = time.time()
    vectors = set()
    for vector_components in vector_collection:
        vector_instance = vector_type(vector_components)
        vectors.add(vector_instance)
    toc = time.time()
    time_lapsed = toc-tic
    time_lapsed_in_ms = 1000*time_lapsed
    if verbose: print("It took me: {:10.4f}ms".format(time_lapsed_in_ms))
    return time_lapsed
    
def create_integer_vector_list(dimension, length, limits = (0,10)):
    int_min, int_max = limits
    list_of_vectors = [ tuple((random.randint(int_min, int_max) for j in range(dimension)))
                        for index in range(length)]
    return list_of_vectors

def create_float_vector_list(dimension, length):
    list_of_vectors = [ tuple((random.random() for j in range(dimension)))
                        for index in range(length)]
    return list_of_vectors


def generate_comparison_lists(vector_list_length = VECTOR_LIST_LENGTH,
                              dimension_max = DIMENSION_MAX,
                              int_bounds = INT_BOUNDS,
                              verbose = True):
    
    simple_int_results   = []
    simple_float_results = []
    better_int_results   = []
    better_float_results = []
    
    for dimension in range(2,dimension_max + 1):
        if verbose: print("\rWorking with dimension {}.".format(dimension), end = '')
        int_vectors   = create_integer_vector_list(dimension, vector_list_length, limits = int_bounds)
        float_vectors = create_float_vector_list(dimension, vector_list_length)
        
        simple_int_results.append(speed_test(int_vectors, SimpleVector))
        simple_float_results.append(speed_test(float_vectors, SimpleVector))
        better_int_results.append(speed_test(int_vectors, BetterVector))
        better_float_results.append(speed_test(float_vectors, BetterVector))

    if verbose: print()

    return simple_int_results, simple_float_results, better_int_results, better_float_results




def main(vector_list_length = VECTOR_LIST_LENGTH,
         dimension_max = DIMENSION_MAX,
         int_bounds = INT_BOUNDS):
    simple_int_results, simple_float_results, better_int_results, better_float_results = generate_comparison_lists(int_bounds = int_bounds)    


    output_data = { "simple_int" :   simple_int_results,
                    "simple_float" : simple_float_results,
                    "better_int" :   better_float_results,
                    "better_float" : better_float_results}
    
    filename = './data/hash_speedtest_dim-{}_intmax-{}_vectorlistlen-{}.json'.format(vector_list_length, dimension_max, int_bounds[-1]-1)


    with open(filename, 'w') as outfile:
        json.dump(output_data, outfile)


for int_max_bound in [2, 10, 20, 200]:
    main(int_bounds = (0, int_max_bound+1))
