# https://www.codewars.com/kata/56f3f6a82010832b02000f38

# Solution required less than 145 characters

s="You're a(n) "
describe_age=lambda n:s+"kid"if n<13 else s+"teenager"if n<18 else s+"adult"if n<65 else s+"elderly"
