from mobile import Mobile


class Iphone(Mobile):
    def __init__(self , name , price ,voltage , screen_size , serial):
        super().__init__(name,price , voltage , screen_size)
        self.serial = serial