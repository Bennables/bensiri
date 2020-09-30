def quadratic(a,b,c):
    discrim = (b**2-(4*a*c))**.5
    x1= (-b+discrim)/2*a
    return x1
def main():
    print (quadratic(1,2,3))

main()