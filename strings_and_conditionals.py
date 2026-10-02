# strings class 2
str1="this is apna gao.\ni am living here for three years.\nsorry i am kiding" 
str2='this is apna gao'
str3='''this is apna gao'''
print(str1)
print(str2)
print(str3)
# string concatination
print(str1 +" " +str2)
len=len(str2)
print(len)
print(str2[1])
print(str2[1:5])
# string funtions
print(str3.endswith ("ao"))
print(str3.endswith ("oo"))
print(str1.capitalize())
# print(str1.replace("i","k"))
print(str1.replace("gao","masjid"))
print(str1.find("o"))
print(str1.count("r"))
name=input("please enter yourfirst user name:")
print("this is lenth of your string ", len(name))


# conditional statments
age=66
if(age>18):
    print("can vote anad apply for lisence")
elif(age<17):
    print("can not vote")
elif(age==18):
    print("eligible")
else:
    print("no more")

    light="green"
if(light=="red"):
        print("stop") 
elif(light=="yellow"):
        print("look")
elif(light=="green"):
             print("go") 
else:
         print("light is broken")
         print("end of code")

marks=int(input("enter your marks:",))
if(marks>=90):
       grate="A"
elif(marks<90 and marks>=80):
       grate="b"
elif(marks>=70 and marks<80):
       grate="c"
elif(marks>=60 and marks<70):
       grate="d"
else:
       grate="e"
       print("grate of students->:",grate)

