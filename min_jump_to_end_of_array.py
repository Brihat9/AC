#!/usr/bin/python3
''' Minimum jump to reach end of array (Dynamic Programming) '''

# Input Array
input_arr = [2, 1, 3, 2, 3, 4, 5, 1, 2, 8]
# input_arr = [2, 4, 1, 2, 1, 5, 3, 2, 1, 2]

input_length = len(input_arr)
max_arr_elem = max(input_arr)

# Initialize minimum jump array
# 1st elem = 0, other = infinity
min_jump_arr = [max_arr_elem * 10] * input_length
min_jump_arr[0] = 0

# Last jump stop for each position, intially from 0
jump_path_arr = [0] * input_length

'''
    Algorithm
    ---------
    Get input Array
    Initialize min_jump_arr to [0, inf, inf, ...] and last_jump_stop to [0, ...]
    for index1 from 1 to last
        for index2 from 0 to index1
            if index1 is reachable from index2
                1. calculate jumps required to reach index1 and store minimum
                   value in min_jump_arr[index1]
                2. set last_jump_stop = index2
                break
    Return last element of min_jump_arr
'''

for i in range(1, input_length):
    for j in range(0, i):
        if(i <= (j + input_arr[j])):
            min_jump_arr[i] = min(min_jump_arr[i], min_jump_arr[j] + 1)
            jump_path_arr[i] = j
            # print('min jump is ' + str(min_jump_arr[i]))
            # print('and last jump stop is ' + str(jump_path_arr[i]))
            break

print("I: ", input_arr)
# print("N: ", input_length)
# print("M: ", max_arr_elem)
print("M: ", min_jump_arr)
print("L: ", jump_path_arr)

print("Minimum jump required is", min_jump_arr[-1])
