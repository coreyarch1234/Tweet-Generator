# https://www.hackerrank.com/challenges/symmetric-difference
a_len = raw_input()
a_set = set(list(map(int, raw_input().split())))
b_len = raw_input()
b_set = set(list(map(int, raw_input().split())))


def symm_diff(a_set, b_set):

    x = (a_set.difference(b_set))
    y = (b_set.difference(a_set))
    z = x.union(y)
    return z


ordered = list(sorted(symm_diff(a_set, b_set)))
for i in range(len(ordered)):
    print ordered[i]
