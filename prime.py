n=int(input("Enter N :"))

if n%2!=0 :
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n,"is not Prime Number")
            break
    else:
        print(n," Prime Number")

else:
    print(n," is not prime number")


 