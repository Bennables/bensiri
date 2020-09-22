#Income and Expenses

array1=[]
xy=1
for x in range(4):
    
    print(f'Year:{xy}')
    #income
    mincome=int(input("What's your monthly income?"))
    weekincome=mincome/4
    aincome=mincome*12

    #expenses
    util=int(input("What's your utility bill per month? "))
    enter=int(input("How much do you spend on entertainment per month? "))
    food=int(input("How much do you spend onf food every month? "))
    mexpenses=util+enter+food
    #taxes, incomplete
    #((mincome+util+enter+food)*.08)taxes..
    
    #clean income
    cleanmincom=mincome-mexpenses
    cleanaincome=int(aincome-(mexpenses*12))

    #display
    print("Your monthly income is:", mincome, ", your annual income is:", aincome)
    print("Your monthly expenses add up to", mexpenses )
    print("After your expenses, you get", cleanaincome, "per year")
    
    x=+1
    array1.append(cleanaincome)
    

tarray=array1[0]+array1[1]+array1[2]+array1[3]
print(f'After four years, your total income after expenses is {tarray}')

