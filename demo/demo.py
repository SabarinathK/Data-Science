from math_module import tax,total_price,discount

tax_price=tax(300,18)
print(tax_price)
price=total_price(3,tax_price)
print(price)
total=discount(price,20)
print(total)