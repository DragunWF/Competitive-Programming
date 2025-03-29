# https://www.codewars.com/kata/569b5cec755dd3534d00000f/train/java

def new_avg(arr, newavg):
    required_donation = newavg * (len(arr) + 1) - sum(arr)
    if required_donation <= 0:
        raise Exception()
    return required_donation.__ceil__()
