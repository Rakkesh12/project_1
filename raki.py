class products:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
        self.actual_price=price
    def display_details(self):
        return "{},{},{},{}".format(self.name,self.price,self.deal_price,self.rating)
    def save_money(self):
        self.actual_price=self.price-self.deal_price
class electronic_items(products):
    def __init__(self,name,price,deal_price,rating,warranty):
        super().__init__(name,price,deal_price,rating)
        self.warranty=warranty
    def Rakkesh(self):
        return super().display_details(),'{}'.format(self.warranty)
class Grocery_items(electronic_items):
    def __init__(self,name,price,deal_price,rating,warranty,manufacture_date,expiary_date):
        super().__init__(name,price,deal_price,rating,warranty)
        self.manufacture_date=manufacture_date
        self.expiary_date=expiary_date
    def varma(self):
        return super().Rakkesh(), "{} {}".format(self.manufacture_date,self.expiary_date)
class order:
    def __init__(self,order_type,order_address):
        self.order_type=order_type
        self.order_address=order_address
        self.items_cart=[]
    def add_items(self,product,quality):
        self.items_cart.append((product,quality))
        #return self.items_cart
    def display_items(self):
        for product,quality in self.items_cart:
            return product.display_details(),("{}{}".format(self.order_type,self.order_address))
    def total_price(self):
        for product,quality in self.items_cart:
            total_bill=0
            price= product.price* quality
            total_bill+=price
            return (total_bill)


raki_1=electronic_items("milk",30,20,4,6)
siva_1=order("online","Thungapalem")
siva_1.add_items(raki_1,2)
siva_1.total_price()
a=siva_1.display_items()
print(a)
"""raki_2=Grocery_items("i-phone",10000,8000,4,5,2022,2026)
b=raki_2.Rakkesh()
c=raki_2.display_details()
d=raki_2.varma()
print(d)
print(c)
print(b)
a=raki_1.Rakkesh()
print(a)"""

