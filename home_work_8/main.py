from furniture import Furniture
from laptop import Laptop
from mobile import Mobile
from lenovo import Lenovo
from asus import Asus
from iphone import Iphone
from samsung import Samsung


furnit_1 = Furniture("raphal", "1200" , "100","2")
print(furnit_1)

mob = Mobile("samsung s25","100","100","10*20")
print(mob)

lap = Laptop("lenovo a1","1200","100", "100","12")
print(lap)

leno = Lenovo("a1", "1200", "100","100","12","1")
print(leno)

as_1 = Asus("d1", '1000',"100","100", "10", "2")
print(as_1)

ipho_1 = Iphone("15", "12500","100","10*30","2")
print(ipho_1)

sam_1 = Samsung("25","100", "100", "10*20","1")
print(sam_1)