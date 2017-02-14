# https://www.hackerrank.com/challenges/plus-minus

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

def find_all(arr):
    num_positive, num_negative, num_zero = 0.0, 0.0, 0.0
    for num in arr:
        if num > 0:
            num_positive += 1
        elif num < 0:
            num_negative += 1
        else:
            num_zero += 1
    return [num_positive, num_negative, num_zero]


def calc_fraction(pos, neg, zero):
    print((pos)/n)
    print((neg)/n)
    print((zero)/n)



if __name__ == '__main__':
    a,b,c = find_all(arr)[0], find_all(arr)[1], find_all(arr)[2]
    calc_fraction(a,b,c)
