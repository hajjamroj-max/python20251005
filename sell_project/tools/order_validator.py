import re

def customer_validator(customer):
    if not type(customer)==str and re.match(r"^[a-zA-Z]$", customer):
        raise ValueError("Invalid customer")

    else:
        return customer

def empolyee_validator(empolyee):
    if not type(empolyee)==str and re.match(r"^[a-zA-Z]$", empolyee):
        raise ValueError("Invalid empolyee")

    else:
        return empolyee


def order_item_list_validator(order_item_list):
    if not type(order_item_list)==str and re.match(r"^[a-zA-Z]$", order_item_list):
        raise ValueError("Invalid order_item_list")

    else:
        return order_item_list

def date_time_validator(date_time):
    if not type(date_time)==str and re.match(r"^[a-zA-Z]$", date_time):
        raise ValueError("Invalid date_time")
    else:
        return date_time

def product_validator(product):
    if not type(product)==str and re.match(r"^[a-zA-Z]$", product):
        raise ValueError("Invalid product")
    else:
        return product


def quantity_validator(quantity):
    if not type(quantity)==str and re.match(r"^[a-zA-Z]$", quantity):
        raise ValueError("Invalid quantity")

    else:
        return quantity


def price_validator(price):
    if not type(price)==int and re.match(r"^[/d]$", price):
        raise ValueError("Invalid price")
    else:
        return price




