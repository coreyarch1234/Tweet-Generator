# Apple and Orange # Easy
#!/bin/python

#!/bin/python

# https://www.hackerrank.com/challenges/apple-and-orange

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

def check_in_range(position):
    if (s <= position <= t):
        return True
    else:
        return False

def num_apples():
        app_counter = 0
        for app in apple:
            if check_in_range(a + app):
                app_counter += 1
            else:
                continue
        return app_counter

def num_oranges():
        oran_counter = 0
        for oran in orange:
            if check_in_range(b + oran):
                oran_counter += 1
            else:
                continue
        return oran_counter

num_apples()
num_oranges()
print(num_apples())
print(num_oranges())

# I had the right logic, but I did not call the functions (lines 42 and 43), so for each test case, the app_counter and oran_counter were not
# resetting to 0. This caused an error for successive cases.
