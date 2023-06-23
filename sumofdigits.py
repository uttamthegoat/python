n=int(input("Enter the number = "))
sum=0;
c=n
while c!=0:
    sum+=c%10
    c=int(c/10)
    if c!=0:
        sum*=10

print(sum)
