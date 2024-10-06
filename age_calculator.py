#for current time
cyear=int(input("the current year: "))
cmonth=int(input("the current month: "))
cday=int(input("the current day: "))
print("year :",cyear,"\nmonth : ",cmonth,"\nday : ",cday)

#for birth time
byear=int(input("the birth year: "))
bmonth=int(input("the birth month: "))
bday=int(input("the birth day: "))
print("year :",byear,"\nmonth : ",bmonth,"\nday : ",bday)

#main logic
year=cyear-byear
month=cmonth-bmonth
day=cday-bday

if day<0 :
    month-=1
    day+=30
if month<0 :
    year-=1
    month+=12

print(year,month,day)



