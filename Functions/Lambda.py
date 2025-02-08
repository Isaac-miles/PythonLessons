# A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression. SYNTAX= lambda arguments : expression

# Add 10 to argument a and return the result
x= lambda a : a+10
print(x(5))

# lambda function can take any number f arguements:
x = lambda a,b: a*b
print(x(5,7))

y= lambda  a,b,c: a+b+c
print(y(4,6,2))

def myFunc(n):
    return lambda a:a*n

multi = myFunc(2)

print(multi(11))