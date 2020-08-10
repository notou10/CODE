ham = 2000
cola = 2000

for i in range(3):
    temp = int((input)())
    
    if(temp<ham):
        ham = temp

for j in range(2):
    temp = int((input)())
    
    if(temp<cola):
        cola = temp - 50

print(ham+cola)