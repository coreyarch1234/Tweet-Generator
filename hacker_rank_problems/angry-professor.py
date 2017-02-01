import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

def find_number_cancelled():
    num_on_time = 0
    for time in a:
        if time < 0:
            num_on_time += 1
    return num_on_time

def calculate(num):
    if num < k:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
        number = find_number_cancelled
        calculate(number)
