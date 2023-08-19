Tuple1 = (11, "Hello", 90.89, False)
print(Tuple1) 

print(Tuple1[3]) #indexing
print(type(Tuple1[0]))
print(type(Tuple1[1]))
print(type(Tuple1[2]))
print(type(Tuple1[3]))

Tuple2 = (11, 78, 90, 11, 78, 56)
print(Tuple2)

#Tuple2[1] = 69
#print(Tuple2)

#Tuple2.append(101)
#print(Tuple2)

#Tuple2.remove(11)
#print(Tuple2)

for val in Tuple2:
    print(val)

for i in range(len(Tuple2)):
    print(Tuple2[i])

