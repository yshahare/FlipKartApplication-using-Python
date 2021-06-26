from parent import Parent
class Product(Parent):
    list_prod=[]
    def __init__(self,pid, pname, cat,price, qty):
        self.Productpid=pid
        self.Productpname=pname
        self.Productcat=cat
        self.Productprice=price
        self.Productqty=qty
    def Show_Product_Details(self):
        return f"""
        Product id is:-{self.pid}
        Product name is:-{self.pname} 
        Product category is:-{self.cat}
        Product Price  is:-{self.price}
        Product Quantity is:-{self.qty}"""   

if __name__ == '__main__':

  prod_obj1 = Product(pid=101, pname="mobile", cat="electronics",price=12000, qty=10)
  prod_obj2 = Product(pid=102, pname="chair", cat="plastic",price=2000, qty=15)
#   Product.list_prod.extend([prod_obj1,prod_obj2])
#   print(prod_obj1, "\n", prod_obj2)  
# res = prod_obj1.Show_Product_Details()
# print(res)
# print(Product.list_prod)