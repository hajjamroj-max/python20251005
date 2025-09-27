from mobile import Mobile


class Samsung(Mobile):
    def __init__(self , name , price ,voltage , screen_size , serie):
        super().__init__(name,price , voltage , screen_size)
        self.serie = serie