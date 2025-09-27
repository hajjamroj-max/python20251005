from elctrical import Electrical


class Mobile (Electrical):
    def __init__(self , name , price ,voltage , screen_size):
        super().__init__(name,price , voltage)
        self.screen_size = screen_size