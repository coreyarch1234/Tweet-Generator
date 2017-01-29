# https://www.hackerrank.com/challenges/plus-minus

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

def find_all(arr):
    num_positive, num_negative, num_zero = 0.0, 0.0, 0.0
    num_array = []
    for num in arr:
        if num > 0:
            num_positive += 1.0
        elif num < 0:
            num_negative += 1.0
        else:
            num_zero += 1.0
    return [num_positive, num_negative, num_zero]


def calc_fraction(pos, neg, zero):
    sum = len(arr)
    print((pos)/sum)
    print((neg)/sum)
    print((zero)/sum)



if __name__ == '__main__':
    a,b,c = find_all(arr)[0], find_all(arr)[1], find_all(arr)[2]
    calc_fraction(a,b,c)
