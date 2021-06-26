from parent import Parent

class Address(Parent):
    def __init__(self,house_no,building_name,pin,city,state):
        self.house_no = house_no
        self.building_name = building_name
        self.pin = pin
        self.city = city
        self.state = state
    def Show_Address(self):
       return f"""
       House no is:-{self.house_no}
       Building name is:-{self.building_name} 
       Pin no is:-{self.pin}
       City is:-{self.city}
       State is:-{self.state}"""     

if __name__ == '__main__':
    add_obj = Address(house_no=102,building_name="deccan",pin=410206,city="panvel",state="MH")
    # print(add_obj) 
    # res = add_obj.Show_Address()
    # print(res)      




