#for loop is used to iterate station no of times
# name=input("enter a string")
# for i in name:
#     print(i)
#wap to create a table
# number=int(input("enter a number for table"))
# for i in range(1,11):
#     print(number*i)
'''for i in range(2,21,2):
    print(i)
    '''
# for i in range(1,21):
#     if i%2==0:
#        print(i)
#wap to print 1 4 7 10 13
# for i in range(1,14,3):
#     print(i)

#wap tp print 1 3 7 11 13 15 using for loop
for i in range(1,16,2):
    if i==5 or i==9:
        continue
    else:
        print(i)
        