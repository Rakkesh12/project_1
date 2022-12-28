"""def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact
#a=factorial(5)
#print(a)

def reverse_number(n):
    sum=0
    while n>0:
        r=n%10
        sum=sum*10+r
        n=n//10
    return sum
#reverse_number(1234)

def list_1():
    a_list=[]
    a_list.append("r")#to append the multiple elements we can the extend keyword
    a_list.append("a")
    return a_list
list_1()"""

def even_number(n):
    for i in range(1,n+1):
        li=[]
        if i%2==0:
            li.append(i)
            print(list(li))
        #else:
            #return "false"
even_number(10)
#b_1=even_number(1)
#print(b_1)



