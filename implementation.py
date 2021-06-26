from customer import Customer, Address, Account
from flipkart_file import Flipkart, Product
from Order_file import Order

prod_obj1 = Product(pid=101, pname="mobile", cat="electronics",price=12000, qty=10)
prod_obj2 = Product(pid=102, pname="chair", cat="plastic",price=2000, qty=10)
prod_obj3 = Product(pid=103, pname="jeans", cat="causual",price=5000, qty=10)
prod_obj4 = Product(pid=104, pname="axe", cat="perfume",price=200, qty=15)
prod_obj5 = Product(pid=105, pname="watch", cat="accessories",price=1500, qty=25)
prod_obj6 = Product(pid=106, pname="Pan", cat="utensils",price=500, qty=20)

Product.list_prod.extend([prod_obj1,prod_obj2,prod_obj3,prod_obj4,prod_obj5,prod_obj6])

flip_acc=Account(actype="current",bal=10000)

flip_obj=Flipkart(headq="pune", no_warehouse=10, prod=Product.list_prod,acc=flip_acc)

# print(flip_obj)

add_obj = Address(house_no=404,building_name="instakart",pin=410206,city="panvel",state="MH")

acc_obj=Account(actype="saving",bal=2000)

cust_obj=Customer(name="ABC",address=add_obj,account=acc_obj,contact_no= +918080707217,email="yog@gmail.com",isplusmember=True)
print(cust_obj)
print("----------------------------------------------")
flip_obj.Product_purchase("Pan",cust_obj,2)
print(flip_obj.prod)
print(cust_obj)
print(flip_obj)
# print(Order.All_Order)
flip_obj.return_product(cust_obj,"Pan",2)
# print(flip_obj.acc.bal)