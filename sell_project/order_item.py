class OrderItem:
    def __init__(self , id , product , order_item_list , date_time):
        self.id = id
        self.product = product
        self.quantity = quantity
        self.price = price



    def __repr__(self):
        return f"{self.__dict__}"