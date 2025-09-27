from non_electrical import  Non_electrical


class Furniture(Non_electrical):
    def __init__(self, name , price ,weight,capacity):
        super().__init__(name , price ,weight)
        self.capacity = capacity