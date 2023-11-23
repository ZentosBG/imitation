class Players:
    def __init__(self,age,height,weight,speed):
        self.age = age
        self.height = height
        self.weight = weight
        self.speed = speed
    def setings(self):
        print(f"{self.age, self.height,self.weight,self.speed }")

class Payer_1(Players):
    pass
class Payers_2(Players):
    def __init___(self,age,height,weight,speed,deference):
        super().__init__(age,height,weight,speed)
        self.deference = deference
        print("heloo")
        
    def setings(self):
        print(f"{self.age, self.height,self.weight,self.speed,self.deference }")
    

p1 = Payer_1("15", "170", "70", "20")
p2 = Payers_2("15", "15", "170", "70", "20")
p1.setings()
p2.setings()