# https://www.codewars.com/kata/5590961e6620c0825000008f/train/python

def swap(string):
    return "".join(list(map(lambda x: x.lower() if x == x.upper() else x.upper(), string)))

# Not good for production but it's fun to solve these katas with a one liner hehe
