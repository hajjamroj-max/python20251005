from laptop import Laptop


class Asus(Laptop):
    def __init__(self , name , price ,voltage , cpu , ram , serial_1 ):
        super().__init__(name,price , voltage,cpu , ram ,)
        self.serial_1 = serial_1