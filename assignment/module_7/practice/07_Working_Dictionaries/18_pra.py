<<<<<<< HEAD
str =  input("Enter the string:")

count = {}

for i in str:
    if i in count:
        count[i] += 1
    else:
        count[i] =1

print("character count")
for key,value in count.items():
=======
str =  input("Enter the string:")

count = {}

for i in str:
    if i in count:
        count[i] += 1
    else:
        count[i] =1

print("character count")
for key,value in count.items():
>>>>>>> 1a7c192261d8cb08888d1c0830130fba219b7b99
    print(key, ":" , value)