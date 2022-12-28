class Employee:
    salary_bouns=10000
    total_detalis=""
    def __init__(self,name,last,salary):
        self.name=name
        self.last=last
        self.salary=salary
        self.total_salary=salary
    def dispaly_details(self):
        return "{} {}".format(self.name,self.last)
    def mail_id(self):
        return "{}.{}@hcl.com".format(self.name,self.last)
    def salary_structure(self):
       self.total_salary=int(self.salary*(self.salary_bouns)//100)
        #return total_salary
    def marks_1(self,middle_name):
        self.total_detalis=self.mail_id()+self.dispaly_details()+middle_name
        return self.total_detalis
obj_1= Employee("Modiboyina","Rakkesh",520000)
#b=obj_1.mail_id()
#print(b)
#c=obj_1.dispaly_details()
#print(c)
a_1=obj_1.marks_1(" VARMA")
print(a_1)

