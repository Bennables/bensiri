
def add_seven(num):
    print ("we are in the add 7 function")
    return num + 7
    
def subtract_seven_add_eight(numb):
    print ("we are in the -7 +8 function")
    return numb+1

def large_power(x,y):
    if x*y>50:
        return True
    else:
        return False
    
def twice_as_large(w,z):
    if w>2*z:
        return True
    else:
        return False
    #or 
    #return w>2*z

def wins_losses(wins,losses):
    total=wins+losses
    print (wins/total)
        
def avg(a,b,c,d,e,f):
    return((a+b+c+d+e+f)/6)

    

def main():
    print("we are in main")
    print(add_seven(7))
    print(subtract_seven_add_eight(4))
    print (large_power(7,8))
    print (twice_as_large(3,2))
    print (wins_losses(8,2))
    print (avg(1,2,3,4,5,6))
main()
    


