from pprint import pprint
import numpy as np


m = 12
k = 4
o = 2
p = 3

# Initialize arrays
p_array = np.ones(m) * p
overlap_array = np.ones(m) * (o + 1)
overlaps_dic = {}
array = np.array([], dtype='int').reshape(0, m)
sequences = []

index = 0
capacity = 0

flag = True
#while(flag):
for i in range(2):
    # Initialize the array
    array_line = np.zeros(m, dtype='int')
    # Throw a sequence
    bulding_sequence_index = 0
    while bulding_sequence_index < k:
        # Get p_index
        p_index = index
        # Check p_index
        if p_array[p_index] > 0:
            p_flag = True
        # Get o index
        # o_index = index
        # Check overlap index
        # if overlap_array[o_index] > 0:
        #    o_flag = True
        # Check for local overlaps
        overlaps_dic[capacity] = {index:0 for index in range(0, capacity)}
        o_dic = overlaps_dic[capacity]
        # Check every element of past sequencesif o_dic[sequence_index]

        local_overlap_flag = True
        for sequence_index in range(capacity):
            if o_dic[sequence_index] > o:
                local_overlap_flag = False

        # Lay the element
        if p_flag and local_overlap_flag:
            array_line[index] = capacity + 1
            p_array[index] -= 1
            bulding_sequence_index += 1
            index += 1

        else:
            index += 1

        # Add overlap
        for sequence_index in range(capacity):
            # If there is an element
            if array[sequence_index, index] == 1:
                o_dic[sequence_index] += 1

    # After finishing adding the sequence
    capacity += 1
    array = np.vstack((array, array_line))
    pprint(array)

