import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))


def order(b):
    sort_list = sorted(b)
    return sort_list


def all_factors(set_b_array):
    num_array = []
    distinct_array = []
    for num in set_b_array:
        for i in range(1, num + 1):
            if num % i == 0:
                num_array.append(i)
    least = order(b)[0]
    distinct_array.append(least)
    for num in num_array:
        if num < least:
            distinct_array.append(num)
    return list(set(distinct_array))

def check_multiples(factor_array):
    between_array = []
    sort = order(b)
    delete_array = []
    delete_new_array = []
    for number in factor_array:
        for num in a:
            if is_a_factor(number, num):
                between_array.append(number)
    for number in between_array:
        for sort_num in sort:
            if sort_num % number != 0:
                delete_array.append(number)
    for number in list(set(between_array).difference(delete_array)):
        if number % order(a)[-1] != 0:
            delete_array.append(number)
    for number in (list(set(between_array).difference(delete_array))):
        for num in a:
            if number % num != 0:
                delete_array.append(number)
    return      (list(set(between_array).difference(delete_array)))

def is_a_factor(num1, num2): # tests if num2 is a factor of num1
    if num1 % num2 == 0:
        return True
    return False

if __name__ == '__main__':
    array_factors = all_factors(b)
    count = check_multiples(array_factors)
    print(count)
