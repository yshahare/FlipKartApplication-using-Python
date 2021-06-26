from parent import Parent
from address import Address
from account import Account
import random
class Customer(Parent):
    def __init__(self,name,address,account,contact_no,email,isplusmember=False):
        self.id=random.randint(145, 689)
        self.name=name
        self.address=address
        self.account=account
        str_mobile=str(contact_no)
        if str_mobile[:2]== "91" and len(str_mobile[2:])== 10:
            self.contact_no=contact_no
        else:
            raise ValueError("mobile no should be +91 code and length is 10")    
         
        if "@" not in email:
            raise ValueError("email must be @ and . symbol")
        self.email=email
        self.ProdOrder =[]
        self.IsPlusMember=isplusmember

    def Customer_details(self):
        return f"""
        Customer id is:-{self.id}
        Customer name is:-{self.name}
        Customer address is:-{self.address}
        Customer account is:-{self.account}
        Customer contact no is:-{self.contact_no}
        Customer email is:-{self.email}"""    
                
if __name__ == '__main__':
    add_obj = Address(house_no=404,building_name="instakart",pin=410206,city="panvel",state="MH")
    acc_obj=Account(actype="saving",bal=8000)
    cust_obj=Customer(name="ABC",address=add_obj,account=acc_obj,contact_no= +918080707217,email="yog@gmail.com")
    # print(cust_obj)
    res = cust_obj.Customer_details()
    print(res)        