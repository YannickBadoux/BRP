import os 
import numpy as np

lines = np.loadtxt(r'/home/tobias/projects/BRP/Filters/Filter numbers', dtype=int)  - 1
filter_names = np.loadtxt(r'/home/tobias/projects/BRP/Filters/filter_info.txt', dtype=str, delimiter=',')
needed_filters = filter_names[lines]

file = open('needed_filters', 'w')
for i in needed_filters:
    file.write(i + '\n')
file.close
