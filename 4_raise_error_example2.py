class Mobile:
    def __init__(self,name):
        self.name=name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be a object of Mobile class')

oneplus = Mobile('one plus 6')   #1
samsung = 'samsung galaxy s6'   #2
mobostore = MobileStore()      #3
# print(mobostore.mobiles)    #4
mobostore.add_mobile(oneplus) 
mobo_phone = mobostore.mobiles
print(mobo_phone[0].name)
# mobostore.add_mobile(samsung) #5
# print(mobostore.mobiles)

# fisrt i create a mobile object 1
# and a normal string  2 
# aand again create a object of mobilestore  3
# if i print it,this will give an empty list 4
# if i append new_mobile in mobostore this will gives positive result  5
# if i dont want any string i want to append the mobile object in mobilestore 
# otherwise raise the error   
# for that we have to use the isinstance method where we def a append method
# this will raise error what if i append the mobile object(oneplus)
# we have to store it in a variable and write the position[0] and the parameter(name)