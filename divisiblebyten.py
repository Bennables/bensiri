
#----------------------------------------------------------
# Challenge 1 - Divisible by Ten
#----------------------------------------------------------
# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

# Return the count of how many numbers in the list are divisible by 10.

#Write your function here

def divisible_by_ten(nums):
    a = 0
    for number in nums:
        if number % 10 == 0:
            a = a + 1
    return a



#Uncomment the line below when your function is done

print(divisible_by_ten([20, 25, 30, 35, 40]))

def at_at_beginning():
    b = []
    words = ["@gmail.com", "purchase", "@yahoo.com", "cart", "password", "@aol.com"]
    for num in words:
        if num[0] == "@":
            b.append(num)
    return b

print (at_at_beginning())



#----------------------------------------------------------
# Challenge 2 - Greetings
#----------------------------------------------------------
# Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.

#Write your function here

def add_greetings(names):
    greetings = []
    for name in names:
        c = ("Hello, "+name)
        greetings.append(c)
    
    return greetings



#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#----------------------------------------------------------
# Challenge 9 - Same Values
#----------------------------------------------------------

# Write a function named same_values() that takes two lists of numbers of equal size as parameters.

# The function should return a list of the indices where the values were equal in lst1 and lst2.

# For example, the following code should return [0, 2, 3]

# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

#Write your function here

def same_values(a,b):
    count = []
    for x in range(len(a)):
        if a[x] == b[x]:
            count.append(x)
    return count

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#----------------------------------------------------------
# Challenge 6 - Larger Sum
#----------------------------------------------------------

# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

#Write your function here

def larger_sum(a,b):
    if sum(a)>sum(b):
        return a
    elif sum(b)>sum(a):
        return b
    else:
        print("equal")
    c = 0
    d = 0
    for x in range(len(a)):
        c = c+c[x]
        d = d+d[x]
        if c>d:
            return a
        elif d>c:
            return b
        else:
            print("equal")

    




#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))