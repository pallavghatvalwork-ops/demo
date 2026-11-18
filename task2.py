r=(int(input("Enter a number: ")))

try:
    if(r%2==0):
        raise ValueError("Number must be an odd number.")
    else:
        mid=r//2
        for i in range(1,mid+2):
            for j in range(mid-i+1):
                print(" ",end="")
            k=2*i-1
            for j in range(k):
                if j==0 or j==k-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#demo  
        for i in range(mid,0,-1):
            for j in range(mid-i+1): #adding new feature
                print(" ",end="")
            k=2*i-1
            for j in range(k):
                if j==0 or j==k-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
             
except ValueError as e:
    print("Error:",e)
