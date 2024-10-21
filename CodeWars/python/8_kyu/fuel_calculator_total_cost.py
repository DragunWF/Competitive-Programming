# https://www.codewars.com/kata/57b58827d2a31c57720012e8/train/python

def fuel_price(litres, price_per_litre):
    discount = (litres // 2) * 0.05
    if discount > 0.25:  # Max discount
        discount = 0.25
    return round(litres * price_per_litre - litres * discount, 2)
