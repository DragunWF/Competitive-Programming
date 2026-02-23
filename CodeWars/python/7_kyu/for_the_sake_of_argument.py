# https://www.codewars.com/kata/5258b272e6925db09900386a

def numbers(*nums) -> bool:
    return all(type(num) is int or type(num) is float for num in nums)
