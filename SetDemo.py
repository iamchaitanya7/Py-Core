Set1 = {10, "Hello", 67.90, True} #hetrogenous
print(Set1) 

#print(Set1[2])

Set2 = {11, 78, 90, 11, 78}
print(Set2)

#Set2[1] = 69     Not Possible Data Duplication
#print(Set2)

for val in Set1:     # Only For each loop is avaible 
    print(val)

#for i in range(len(Set1)):   Not Possible range
#    print(Set1[i])

Set2.add(101)
print(Set2)

Set2.discard(101)
print(Set2)

Set2.remove(11)
print(Set2)

n = int(input("Enter a Value to search in set: "))      #to find unique value in the set
for val in Set2:
    if (n == val):
        print("Element Found")
        break