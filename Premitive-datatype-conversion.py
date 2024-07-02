# Data Type Conversion with Strings

# A string is a collection of one or more characters (letters, numbers, symbols). 
# You may need to convert strings to numbers or numbers to strings fairly often. 
# Check out how you can do this using the str() function:

price_cake = 15
price_cookie = 6
total = price_cake + price_cookie
print("The total is: " + total  + "$") #TypeError: Can't convert 'int' object to str implicitly
print("The total is: " + str(total)  + "$") # you have to write like this

# -----------------------------------------------------------------------------------

# Real to Complex Data Type Conversion

real = 2
imag = 5
print(complex(real, imag))

# ------------------------------------------------------------------------------------

price_cake = '15'
price_cookie = '6'

# Explicit type conversion to integer
total = int(price_cake) + int(price_cookie)
print("The total is: " + str(total)  + "$")

# String concatenation
total = price_cake + price_cookie
print("The total is: " + total + "$")

#--------------------------------------------------------------------------------------
