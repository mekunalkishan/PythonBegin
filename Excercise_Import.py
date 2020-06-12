import random
ex_gallon = random.randint(10,25)
ex_range = random.randint(200,400)

print(ex_gallon)
print(ex_range)

# miles per gallon (MPG) = miles driven/gallons used
print( ex_range % ex_gallon )
print( ex_range // ex_gallon )
print( ex_range / ex_gallon )


