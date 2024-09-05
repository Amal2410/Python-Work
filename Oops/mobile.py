class mobile:

    name:str

    storage:str

    price:int

    brand:str

# instance variable

    def __init__(self,name,storage,price,brand):
        
        self.name=name

        self.storage=storage

        self.price=price

        self.brand=brand

    def display_details(self):

        print(self.name,self.storage)

# object creation

# __init__()

# 

#  reference_name=className()

mobile_instance=mobile("nord9r","128",567,"oneplus")

mobile_instance.display_details()

