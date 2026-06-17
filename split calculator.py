#ask the user to input the expenses of food,bill, rent

rent= int(input("enter rent amount : "))
food= int(input("enter food amount : "))
electricity_unit= int(input("enter electricity unit : "))
electricity_unitcharge= int(input("enter electricity per unit charge ; "))
other= int(input("enter other expenses amount, if there is no other expenses enter 0 : ")) #if there is any other expenses so user can enter it here
electricbill= electricity_unit*electricity_unitcharge
totalbill= rent+food+electricbill+other

print(totalbill)
