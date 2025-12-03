#  3 : Loop through a dictionary and print each key–value pair. and store it in a list .
#       Example 1:
#       Input : x = {'a' : 34 , 'b' : 32 , 'c' : 39 } 
#       output :  [a,b,c] 
#       [34,32,39]


main = {
    "a" : 10,
    "b" : 20,
    "c" : 30,
    "d" : 40
}

keys = []
values = []


for key in main:
    keys.append(key)

for i in main.values():
    values.append(i)


print(keys)
print(values)