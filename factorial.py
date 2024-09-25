#factorial program
count=1
n=int(input("enter the number for the factorial : "))
fact=1
while count<n+1 :
    fact*=count
    count+=1
print("factorial : ",fact)
