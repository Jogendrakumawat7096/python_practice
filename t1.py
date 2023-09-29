for i in range(0,10):
    print(" "*(10-i),"*"*i)

for i in range(0,10):
    print(" "*i,"*"*i)

number = [25,21,10,5]

sum = 0

for n in number:
    sum +=n

print(sum)
n=51

for i in range(n):
    if i%5==0:
        print(i)