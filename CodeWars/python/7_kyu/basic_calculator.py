# https://www.codewars.com/kata/5296455e4fe0cdf2e000059f/train/python

def calculate(num1, operation, num2): 
    try:
        return eval(f"{num1}{operation}{num2}")
    except:
        return None