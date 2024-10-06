#file handling
#create file to save password 
# mypassword=open("password.txt","w")

# #write the text in that file
# mypassword.write("my macbook password : kpj")

# #take the input from user
# #mypassword.write(input("\n enter the text :"))

# #read the file text
mypassword=open("password.txt","r")
print(mypassword.read())
mydata=mypassword.read()
print("mydata", mydata)

if "macbook" in mydata:
    print("yes")
else:
    print("no")

#create read write delete csv,excel,json,txt

#create csv file
# mycsv=open("myfile.csv","w")
# mycsv.write("shreya","tripti","kajal","dristi")

# myexcel = open("myexcel.xlsx","w")
# myexcel.write("name,jisoo,rose,lisa,jennie")

