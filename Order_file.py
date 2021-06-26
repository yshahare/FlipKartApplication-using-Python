from parent import Parent
class Order(Parent):
    All_Order=[]
    def __init__(self,transactionid,cust,amount):
        self.OrderTransactionID=transactionid
        self.OrderCust=cust
        self.OrderAmount=amount

