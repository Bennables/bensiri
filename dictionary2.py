my_grades = {"english":80,"science":"63"}
your_grades = {"english":80,"science":"63"}
everyones_grade = {
    "mine":my_grades,
    "yours":your_grades
}
print (everyones_grade)

veggies = {"california":"sacramento", "oregon":"salem"}
print (veggies)
caps = []
capis = []
states = []

for cap in veggies.values():
    print(cap)
    caps.append(cap)

#alt way to access value in dictionary
#capi = key
for capi in veggies:
    print(veggies[capi])
    capis.append(capi)

for st in veggies:
    print(st)
    states.append(st)


    
print (caps)
print (capis)
print (states)
print (veggies["california"])

game_scores = {"1":"24", "2":"35"}

average = 0
for user in game_scores:
    average += int(game_scores[user])

average = average/len(game_scores)
print (average)
    

