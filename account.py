from parent import Parent
import random
class Account(Parent):
    def __init__(self,actype,bal):
        self.accno=random.randint(12345, 78945)
        self.actype=actype
        if bal<2000:
            raise ValueError("your balance should be more")
        self.bal=bal

    def Show_Account(self):
        return f""" 
        Account no is:-{self.accno}
        account type is:-{self.actype}
        your balance is:-{self.bal}"""    
if __name__ == '__main__':
    acc_obj=Account(actype="saving",bal=3000)
    # print(acc_obj)
    # res= acc_obj.Show_Account()
    # print(res)        