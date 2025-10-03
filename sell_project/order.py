class Order:
    def __init__(self , id , customer , order_item_list , date_time):
        self.id = id
        self.customer = customer
        self.empolyee = empolyee
        self.order_item_list = order_item_list
        self.date_time = date_time


    def __repr__(self):
        return f"{self.__dict__}"