# loops in python
# first loop is while loop  meaans jab tak ya condition sach hoge while loop chala ga 
count=1
while count<= 5:
    print("hello")
    count += 1
    print(count)
i=1
while i<=100:
    print(i)
    i+=1
   
    print("loop is ended")
t=100
while t>=1:
    print(t)
    t-=1
i=1
while i<=10:
    print(5*i)
    i+=1
n=int(input("enter a number  which you want to see in table form:"))
i=1
while i<=10:
    print(n*i)
    i+=1
nums=[1,2,4,9,16,25,36,49,89]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1
x=36
nums=(1,2,4,9,16,25,36,49,89)
idx=0#initialization
while idx<len(nums):
    if(nums[idx]==x):
        print ("found at index :",idx)
    else:
        print("Finding....")
    idx+=1
    # break and continues key words
i=1
while i<= 5:
     print(i)
     
     if(i==3):
          break
     i += 1
     
i=1
while i<= 5:
    
     
     if(i==3):
          continue# continue means break
     i += 1
     print(i)
# FOR LOOP IN PYTHON
list=["tomatoes","brinjal","onion"]
for val in list:
     print(val)

nums=[1,2,3,4,5,6]
for val in nums:
     print(val)

#Range() funtion range is an important function
for i in range(10):
    print(i)
    for i in range(2,100,2):
        print(i)
    