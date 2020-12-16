#count


string = "a distinct section of a piece of writing, usually dealing with a single theme and indicated by a new line, indentation, or numbering."
print(string.count("a"))
#amount of a's in the string
print(string.count("i",0,10))
#0 is the first letter, 2 is the is the tenth letter



#lower

string2 = "WrItTen woRkS, espEciALly thoSE cOnsiDered oF superior or laStinG aRtiStic mERit"
print(string2.lower())

#does not effect other characters or numbers
string3 = "!@#$>< 23498  FJDKFJD"
print(string3.lower())



#split

string4 = "a system of labor camps maintained in the Soviet Union from 1930 to 1955 in which many people died"
print(string4.split())

#does not account for spaces in between words
string5 = "a wow system wow of wow labor wow camps wow maintained"
print(string5.split("wow"))