# https://www.codewars.com/kata/6113c2dc3069b1001b8fdd05/train/python

def count_duplicates(name, age, height):
    duplicates = 0
    profiles = []
    for i in range(len(name)):
        profile = {"name": name[i], "age": age[i], "height": height[i]}
        if profile in profiles:
            duplicates += 1
        else:
            profiles.append(profile)
    return duplicates
