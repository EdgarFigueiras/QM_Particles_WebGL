import numpy as np
import random
import math
import codecs, json

#File load, return the array with the 3dData of the selected path
def load_data(path):
    #File with binary data
    file_with_binary_data = open(path, 'rb+')

    #Gets the binary data as an array
    array_with_all_data = np.load(file_with_binary_data)

    #Matrix with the data of the 3D grid
    array_3d = array_with_all_data['arr_0']

    return array_3d

array = load_data("gauss.3d")

json_list = array.tolist() # nested lists with same data, indices
file_path = "/Users/edgarfigueiras/Desktop/gauss.json" ## your path variable
json.dump(json_list, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) ### this saves the array in .json format

