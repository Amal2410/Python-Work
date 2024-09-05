class bike:

    name:str

    brand:str

    price:int

    def __init__(self,name,brand,price):

        self.name=name

        self.price=price

        self.brand=brand

    def __str__(self):

        return self.name
    
class showroom:

    name:str

    place:str

    bikes:list

    def __init__(self,name,place):

        self.name=name

        self.place=place

        self.bikes=[]

    def add_vehicle(self,bike):

        self.bikes.append(bike)

    def list_vehicle(self):

        for b in self.bikes:

            print(b)

    
hunter_instances=bike("hunter","re",200000)

activa_instances=bike("activa","honda",200000)

dominar_instances=bike("dominar","bajaj",120000)

himalayan_instances=bike("himalayan","re",220000)

showroon_instance=showroom("popular","kakkanad")

showroon_instance.add_vehicle(hunter_instances)

showroon_instance.add_vehicle(dominar_instances)

showroon_instance.list_vehicle()

showroon_instance2=showroom("tags","thrissur")

showroon_instance2.add_vehicle(hunter_instances)
showroon_instance2.add_vehicle(activa_instances)
showroon_instance2.add_vehicle(dominar_instances)
showroon_instance2.add_vehicle(himalayan_instances)

showroon_instance.list_vehicle()

 