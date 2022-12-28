""""#import varma
import pytest
@pytest.mark.parametrize("a,b,c",[("rakkesh","modiboyina","rakkeshmodiboyina"),("aditya","varma","adityavarma")])
def test_raki(a,b,c):
    assert a+b==c

"""
"""def rakkesh_1(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact
#rakkesh_1(5)

def test_raki():
    assert rakkesh_1(5) == 120 """
"""with open("calculation.py",'r') as x:
    for line in x:
        print(line)"""