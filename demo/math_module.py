def sub(b,a=0):   # here 0 is the default value of the function          
    '''
    This function is for subtracting two number
    
    arguments:
       a = default=0,int
       b = int
    
    example: 
    >>> sum (a=3,b=1)
        c=3-1
    ... a,b,c=3,1,2
    
    
    
    '''
    c=a-b
    return a,b,c

def tax (price,tax_per):
    tax_amount=price+((price/100)*tax_per)
    return tax_amount

def total_price (a,price):
    total=a*price
    return total

def discount(price,dis_price):
    discount_price=price-((price/100)*dis_price)
    return discount_price