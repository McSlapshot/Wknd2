# Start Your Code here

class Parking_Garage():
    def __init__(self, spots_available, Pay_for_Parking, add_car, remove_car):
        self.spots_available = spots_available
        self.Pay_for_Parking = Pay_for_Parking
        self.add_car = add_car
        self.spots = 9
        self.tickets = 9
        self.remove_car = remove_car

def spots_available(self):       
        return self.spots

def Pay_for_Parking(self):
    Price = input("Please input $5 to pay your ticket")
    if Price == '$5':
        print("Thank you! The ticket has been paid, you have 15 min to leave, come again!") 
    else:
        print("Incorrect payment, try again")    

def add_car(self):
    print("Please take a ticket")
    if self.spots > 0:
        self.spots -=1
        self.tickets -= 1

    else:
        print("We don't have any space available")

def remove_car(self):
    self.spots += 1
    self.tickets +=1

 

#-----------------------------------------------------------------------------------
#--------------------------------MAIN PART OF CODE----------------------------------
Current_Ticket = {}

DS_Garage = Parking_Garage(spots_available, Pay_for_Parking, add_car, remove_car)

def Garage():

    while True:
    
        Welcome = input("Welcome to DS's Parking Garage! If you would like to park please say yes to take a ticket.")

        if Welcome == "yes":
            DS_Garage.add_car()            

        Leaving = input('Enter done when leaving')
        if Leaving == 'done':
            Pay_for_Parking()
            remove_car()     

Garage()