# Enter your code here. Read input from STDIN. Print output to STDOUT
# Will attempt later
import sys
n = raw_input()
d_i = []
d_i = map(int,raw_input().strip().split(' '))

def swap(first, second):
    return(second,first)

def reverse(array_to_be_reversed):
    return array_to_be_reversed.reverse()

#default case
def check_default():
    start = 0
    if d_i[0] == start:
        start = d_i[1]
    for num in d_i:
        if num > start:
            start = num
        else:
            return False
    print('yes')

#case 1.a
def check_swap():
    counter = 0
    chances = 0
    time_alloted = len(d_i) - 2
    time_counter = 0
    sum = 0
    indices = []
    for num in d_i:
        if (time_counter == time_alloted):
            print('yes')
            print("swap " + str(indices[0]) + " " +  str(indices[1]))
            return ['yes', "swap " + str(indices[0]) + " " +  str(indices[1])]
        sum = num + d_i[counter + 1]
        if sum < num + d_i[counter + 2]:
            counter += 1
            time_counter += 1
            continue
        else:
            if chances == 1:
                return
            else:
                swap(d_i[counter + 1],d_i[counter + 2])
                indices = [(counter + 1), (counter + 2)]
                chances += 1
                time_counter += 1


# check_default()
check_swap()
# print(check_default())
