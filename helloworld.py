import math
#a=10
#b=20
#print(a+b)

"""a="Rakkesh"
print(type(a))
print(len(a))
"""
"""a=25
b=4
print(a/b)
print(a%b)"""

"""a=pow(2,5,2)
print(a)"""
"""
a=[1,2,3,4,5]
b=("rakkesh",10,20,"sai")
d={"rakkesh",10,5}
print(a)
print(b)
print(d)

s='rakkesh'
print(list(s))
print(tuple(s))
print(set(s))
"""

"""a="rak ,kes     5,67"
b=a.split(",")
print(b)"""

"""r=['r','kkesh ']
b='a'.join(r)
print(b)"""

"""a="Rakkesh"
b=a[4::-2]
print(b)"""
"""a=[1,2,3,4]
b=a[3:0:-1]
c=a
print(b)
print(c)"""

"""m=
n=5
m=str(m)
a=m*n
print(list(a))"""

"""a=["200"]
b=4
c=a*b
print(c)"""

"""a=input()
b=input()
print(a==b)
c=a[0:3]
d=b[0:3]
print(c==d)"""

"""x=list(input())
y=list(input())
print(x==y)
f=x[0]
r=y[-1]
if f<r :
    print(True)
else:
    print(False)"""

"""m=p=c=int(input())
if m>=70 and p>=60 and c>=60 :
    print(True)
    d=m+p+c
    if d>=180:
        print(True)
#if m>=70 and p>=60 or c>=60 :"""

"""b="RaKkeSh "
a=b.strip(" ,")
print(a)"""

"""b="rakkesh"
a=b.isupper()
print(a)"""

"""Sai= "Python@12"
for i in Sai:
    x=i.isupper()
    print(x)
    y=i.islower()
    z=i.isdigit()
    if i=="@" :
        a=True"""

"""n=int(input())
a=n//365
print(a)
b=n%365
print(b)
c=b//7
print(c)
d=b%7
print(d)"""

"""
list=[10,20,30,40]
sum=0
for i in list:
    sum+=i
print(sum)"""
"""
Number=list(map(int,input()))
sum=1
for i in (Number):
    sum*=i
print(sum)
print(Number)"""


"""Line=int(input())
for i in range(1,Line):
    for j in range(1,Line):
        print("*",end="")
    print()"""

"""import unittest
class TestStringMethods(unittest.TestCase):
    #def __init__(self,x,y):
        #self.x=x
        # self.y=y
    #def add_numbers(self):
         #c=self.x+self.y
         #return c
    def test_string(self):
        self.assertEqual(2*15,30)
    
#raki_1=TestStringMethods()
#raki_1.add_numbers()
#raki_1.test_string(10"""
import calculation
import unittest

class String_methods(unittest.TestCase):

    def test_add(self):
        result_1=calculation.add(10,20)
        self.assertEqual(result_1,30)
    def test_sub(self):
        result_2=calculation.sub(20,10)
        self.assertEqual(result_2,10)
    def test_fact(self):
        result_3=calculation.factorial(6)
        self.assertAlmostEqual(result_3,720)
    def test_reverse(self):
        result_4=calculation.reverse_number(12345)
        self.assertEqual(result_4,54321)
    def test_list_2(self):#it is for only string elements
        b_1ist="rake"
        result_6="rakkesh"
        #result_6=calculation.list_1()
        self.assertNotIn(b_1ist,result_6)
    def test_even(self):
        result_7=calculation.even_number(10)
        self.assertEqual(result_7,[2,4,6,8,10])
    def test_list_4(self):
        li_1=[1,2,3,4]#to compare the two list are equal are not
        li_2=[1,2,3,4]
        self.assertListEqual(li_1,li_2)

if __name__=='__main__':
    unittest.main()
