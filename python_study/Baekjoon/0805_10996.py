N = int(input())

if(N==1):
    print("*")

elif (N>=2):
    for j in range(N):
        for i in range(1,N+1):
            if(i%2==1):
                print("* ", end="")
        print()
        
        for k in range(1,N+1):
            if(k%2==0):
                print(" *", end="")
        print()
        
        



