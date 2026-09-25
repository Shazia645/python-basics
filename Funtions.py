#FUNCTION AND RECURSIONS
# funtions are block of code that perfoe
# rm a spacific statment
def calc_sum(a,b):# idr a ur b ko parameters kaha ga
    sum=a+b
    print(sum)
    return sum
#ap fuction ko bana ka bat usko call kaca krta hai
calc_sum(2,3)# idr a ur b ke value yani 2,3 ko arguments kaha ga
calc_sum(23,33)

calc_sum(22,35)
calc_sum(25,36)
print(sum)

# asa function jo average  calculate kary ga
def calcu_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
calcu_avg(2,5,7)

cities=['karachi','haiderabad','gilit','islamabad','lahore']
heroes=['thor','iron man','hatim','doctor brain','brusle']
def print_len(list):
    print(len(list))
    return len
print_len(cities)
print_len(heroes)

def print_list(list):# ya function simply hamary puri list ka elements ko single line mai print kr daga 
    for item in list:
        print(item, end ="  ")
print_list(heroes)
print_list(cities)






def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")



converter(100)

def input_num(a):
    num=a
    if num==a/2:
     print("ypu enter even num :",a)
    else:
        print("you enter odd num:",a)
    return num

input_num(34)
input_num(33)



# NEW topic recursion oops ur recursion inter related hai jo kam loops sa kia jaskta hai wo recursion sa b kia jaskta hai ur jo kam recursion sa kia ja skta hai wo looops sa b hota hai but recursion some cases mai used  hota hi ur loops sa thorda deficult hai
def show(n):
    if (n==0):
        return# return ka sat kuch b ni likh ka khali return likhta hai to wo control wala return hoga koi valu return ni kary ga
    print(n)
    show(n-1)
show(6)







def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)
print(fact(4))






def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum (n-1) +n



sum=calc_sum(90)
print(sum)
