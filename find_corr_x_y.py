# Spring 2018 - Adam Ross Nelson - Adding as companion to coorhandPy.py
# - See also: https:github.com/adamrossnelson/crossreg/blob/master/corrhandStata.do
# Maintained at: https:github.com/adamrossnelson/crossreg

# After executing hand calcuation of correlation in Stata (fall 2015) and then
# also in Python (Fall 2017) I found this version (Spring 2018) in Saha's (2015)
# book Doing Math With Mython. No Starch Press: San Francisco, CA.
# See pages 77-78.

# This version requires fewer dependencies than my versions discussed above.

def find_corr_x_y(x,y):
    n = len(x)
    
    # Find the sum of the products.
    prod = []
    for xi,yi in zip(x,y):
        prod.append(xi*yi)
        
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2
    
    x_squared = []
    for xi in x:
        x_squared.append(xi**2)
    
    # Find the sum
    x_square_sum = sum(x_squared)
    
    y_square = []
    for yi in y:
        y_square.append(yi**2)
    # Find thes um
    y_square_sum = sum(y_square)
    
    # Use forumla to calculate correlation
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = denominator_term1*denominator_term2**.5
    correlation=numerator/denominator
    
    return correlation

simple_list1 = [1, 2, 3]
simple_list2 = [4, 5, 6]

print(find_corr_x_y(simple_list1, simple_list2))
