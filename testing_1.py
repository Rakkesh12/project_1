import unittest
from raki import products
from raki import electronic_items
from raki import Grocery_items
from raki import order
class raki_1(unittest.TestCase):
    def setUp(self):
        print("ok")
        self.varma_1=products("rakkesh",40,20,4)
        self.varma_2=electronic_items("varma",60,30,3,5)
        self.govind_3=Grocery_items("govind",80,50,5,8,2022,2026)
        self.total=order("online","Thungapalem")
        #self.total.add_items(self.govind_3,2)
    def testProd(self):
        self.assertEqual(self.varma_1.display_details(),"rakkesh,40,20,4")
        self.assertEqual(self.varma_1.actual_price,40)
        self.varma_1.save_money()
        self.assertEqual(self.varma_1.actual_price,20)
    def test_electronic(self):
        self.assertEqual(self.varma_2.actual_price,60)
        #self.varma_2.save_money()
        #self.assertEqual(self.varma_2.actual_price,30)
        result=self.varma_2.Rakkesh()
        self.assertEqual(result,('varma,60,30,3', '5'))
        #self.assertEqual(self.varma_2.Rakkesh(),'5')
    def test_Grocery_items(self):
        #self.assertEqual(self.varma_2.Rakkesh(),('varma,60,30,3', '5'))
        #self.assertEqual(self.govind_3.varma(),('varma,60,30,3', '5'))
        self.assertEqual(self.govind_3.price,80)
    def test_total(self):
        self.assertEqual(self.total.items_cart,[])
        self.total.add_items(self.govind_3, 2)
        #self.assertEqual(self.total.items_cart,["govind",80,50,5,8,2022,2026,2)
        #self.assertEqual(self.total.display_items(),'80,onlineThungapalem')
        self.assertEqual(self.total.total_price(),160)
        #self.assertEqual(self.total.display_items(),"govind",80,50,5,6)

if __name__=='__main__':
    unittest.main()






"""class rakkesh_methods(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.obj_1 = Employee("Modiboyina", "Rakkesh", 520000)
    def test_salary(self):
        #obj_1 = Employee("Modiboyina", "Rakkesh", 520000)
        obj_2= Employee ("varma","aditya",75000)
        #here were are not updated the salary after calling the salary_structure method the salary will
        #will update the salary
        self.assertEqual(obj_2.total_salary,75000)
        obj_2.salary_structure()
        self.assertEqual(obj_2.total_salary,7500000)
        #self.assertEqual(self.obj_1.salary_structure(),52000000)
    def test_varma(self):
        #obj_1 = Employee("Modiboyina", "Rakkesh", 520000)
        self.assertEqual(self.obj_1.dispaly_details(),"Modiboyina Rakkesh")
        self.assertEqual(self.obj_1.mail_id(),"Modiboyina.Rakkesh@hcl.com")
       # with self.assertRaises(TypeError,1+"aa"):
           # print("Exception")
    def test_bhuv(self):
        self.assertEqual(self.obj_1.total_detalis,"")
        self.obj_1.marks_1("rakki bhai")
        self.assertEqual(self.obj_1.total_detalis,"Modiboyina.Rakkesh@hcl.comModiboyina Rakkeshrakki bhai")"""
