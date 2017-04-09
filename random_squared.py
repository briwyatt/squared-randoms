#Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.
from random import randrange

random_numbers =[]
for i in range (20):  
    random_numbers.append(randrange(0,49,1))
print ("random_numbers:", random_numbers)

#use a list comprehension to build a new list that contains each number squared.
squared_list = []

for n in random_numbers: 
    squared_list.append(n*n)
print("squared list of previous list:", squared_list)
