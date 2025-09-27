from laptop import Laptop


class Lenovo(Laptop):
    def __init__(self , name , price ,voltage , cpu , ram , serial_2 ):
        super().__init__(name,price , voltage,cpu , ram ,)
        self.serial_2 = serial_2