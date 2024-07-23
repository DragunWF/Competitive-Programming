# https://www.codewars.com/kata/5881460c780e0dd207000084/train/python

def spot_diff(s1, s2):
    return [i for i in range(len(s1)) if s1[i] != s2[i]]
