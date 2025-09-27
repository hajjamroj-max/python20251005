from elctrical import Electrical


class Laptop(Electrical):
    def __init__(self , name , price ,voltage , cpu , ram):
        super().__init__(name,price , voltage)
        self.cpu = cpu
        self.ram = ram