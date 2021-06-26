from parent import Parent
from product import Product
from copy import deepcopy
from Order_file import Order
import random
class Flipkart(Parent):
    def __init__(self, headq, no_warehouse, prod,acc):
        self.name="FLIPKARTS"
        self.headq=headq
        self.no_warehouse=no_warehouse
        self.prod=prod
        self.acc=acc
        self.prod_name=list(map(lambda x:x.Productpname,self.prod))
        # print(self.prod_name)

    def Product_purchase(self,productname,cust,qty):
        if productname in self.prod_name:
            for i in self.prod:
                if productname==i.Productpname:
                    if qty <=i.Productqty:
                        total_price=qty*i.Productprice
                        print(f"total_price is:-{total_price}")
                        if cust.account.bal>=total_price: 
                            print(i,"####Flipkart Stock before purchase product####")
                            if cust.IsPlusMember ==True:
                                total_price=total_price-total_price*(5/100)
                                print(f"total price after discount:-{total_price}")
                            cust.account.bal=cust.account.bal-total_price
                            self.acc.bal+=total_price
                                           
                            actual_qty=i.Productqty  #  25
                            i.Productqty=qty
                            cust.ProdOrder.append(deepcopy(i)) # 1
                            i.Productqty=actual_qty-qty
                            trans_id =random.randint(1111111,9999999)
                            order_obj=Order(transactionid=trans_id,cust=cust,amount=total_price)
                            Order.All_Order.append(order_obj)
                            print(f"thank you for purchasing the product,tarnsaction id is:-{trans_id}")
                            print(i,"*****Flipkart stock Ater purchase product*******")
                        else:
                            print("insifficient amount")
                            return

                    else: 
                        print("quantity is more")
                        return
                      
        else:
            print(f"Given product is not available in the list {self.prod_name}") 

    def return_product(self,cust,productname,qty):
        if productname in self.prod_name:
            for i in self.prod:
                # print(i,"@@@@@@@@@@")
                if productname==i.Productpname:
                    if qty<=i.Productqty:
                        total_price=qty*i.Productprice
                        print(total_price,"........")
                        self.acc.bal-=total_price
                        print(f"deducted the flipkart balance, and current balance is:-{self.acc.bal}")
                        cust.account.bal=cust.account.bal+total_price
                        print(f"your order is successfully return, and return your amount on your account:-{cust.account.bal}",)
                        # return_qty=qty+i.Productqty
                        # print(return_qty)
                        actual_qty=i.Productqty  #  25
                        i.Productqty=qty
                        cust.ProdOrder.append(deepcopy(i)) # 1
                        i.Productqty=actual_qty+qty
                        trans_id =random.randint(1234567,9879679)
                        order_obj=Order(transactionid=trans_id,cust=cust,amount=total_price)
                        Order.All_Order.append(order_obj)
                        print(f" flipkart account transaction id is:- {trans_id}")
                        print(i,".....product is return with quantity, and added with qty............")
                        
                  
        else:
            print("this produc is not available")
            return

      
                



if __name__ == '__main__':
    prod_obj1 = Product(pid=10, pname="mobile", cat="electronics",price=12000, qty=10)
    prod_obj2 = Product(pid=10, pname="chair", cat="plastic",price=2000, qty=10)
    # flip_obj= Flipkart(headq="pune", no_warehouse=10, prod=[prod_obj1,prod_obj2],)
    # print(flip_obj)
    