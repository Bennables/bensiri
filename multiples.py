# --------------------------------------------------
# Challenge 1 - First Three Multiples
# --------------------------------------------------

# Write a function named first_three_multiples() that has one parameter named num.

# This function should print the first three multiples of num. Then, it should return the third multiple.

# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

# Write your first_three_multiples function here

# Uncomment these function calls to test your first_three_multiples function:
#first_three_multiples(10)
# should print 10, 20, 30, and return 30
#first_three_multiples(0)
# should print 0, 0, 0, and return 0
def first_three_multiples(num):
    x = num
    y = num * 2
    z = num * 3
    print(x)
    print(y)
    return z

# --------------------------------------------------
# Challenge 2 - Tip
# --------------------------------------------------

# Create a function called tip() that has two parameters named total and percentage.

# This function should return the amount you should tip given a total and the percentage you want to tip.

# Write your tip function here:
  
# Uncomment these function calls to test your tip function:
#print(tip(10, 25))
# should print 2.5
#print(tip(0, 100))
# should print 0.0 ]

def tip(total, percentage):
    tib = total*(percentage*.01)
    return tib

# --------------------------------------------------
# Challenge 4 - Dog Years
# --------------------------------------------------

# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.

# The function should compute the age in dog years and return the following string:

# "{name}, you are {age} years old in dog years"
# Test this function with your name and your age!

# Write your dog_years function here:

# Uncomment these function calls to test your dog_years function:
#print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
#print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years" 

def dog_years(name,age):
    return (f'{name}, you are {age*7} years old in dog years')

# --------------------------------------------------
# Challenge 1 - In Range
# --------------------------------------------------

# Create a function named in_range() that has three parameters named num, lower, and upper.

# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

# Write your in_range function here:

# Uncomment these function calls to test your in_range function:
#print(in_range(10, 10, 10))
# should print True
#print(in_range(5, 10, 20))
# should print False 

def in_range(num, lower, upper):
    if num>=lower and num<=upper:
        return True
    else:
        return False

# --------------------------------------------------
# Challenge 4 - Movie Review
# --------------------------------------------------

# Create a function named movie_review() that has one parameter named rating.

# If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"

# Write your movie_review function here:

# Uncomment these function calls to test your movie_review function:
#print(movie_review(9))
# should print "Outstanding!"
#print(movie_review(4))
# should print "Avoid at all costs!"
#print(movie_review(6))
# should print "This one was fun." 

def movie_review(rating):
    if rating <=5:
        return "noooo watch"
    elif 5<rating<9:
        return "This one OK"
    elif rating>9:
        return "Outstanding!"
    else:
        return "Not Valid"

# --------------------------------------------------
# Challenge 5 - All Operations
# --------------------------------------------------

# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.

# First, print the sum of a and b.

# Second, print d subtracted from c.

# Third, print the first number printed, multiplied by the second number printed.

# Finally, return the third number printed mod a.

# Write your lots_of_math function here:

# Uncomment these function calls to test your lots_of_math function:
#print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
#print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

def lots_of_math(a,b,c,d):
    print(a+b)
    print(d-c)
    print(a,",", a*b)
    return c%a
    

def main():
    print(first_three_multiples(5))
    print(f'Tip is {tip(5,10)}')
    print(dog_years("lola",16))
    print(in_range(5,10,20))
    print(movie_review(7))
    print (lots_of_math(2,3,5,5))
main()





