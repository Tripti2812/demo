choice=int(input("1.dollar to ruppees\n2.ruppees to dollar\nenter your choice in number :"))
if choice==1 :
    amount=int(input("enter the amount to convert :"))
    amount*=84.03
    print("the amount in ruppees =",amount,"rs")
elif choice==2 :
    amount=int(input("enter the amount to convert in dollar : "))
    amount/=84.03
    print("the amount in dollar =$",amount)
else :
    print("invalid choice")