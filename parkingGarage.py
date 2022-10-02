# Start Your Code here
class Parking_Garage():
    def __init__(Self, Take_Ticket, Pay_for_Parking, Variable, Leave_Garage, Parking_Spaces):
        self.Take_Ticket = Take_Ticket
        self.Pay_for_Parking = Pay_for_Parking
        self.Variable = Variable
        self.Leave_Garage = Leave_Garage
        self.Parking_Spaces = Parking_Spaces

def Take_Ticket():
    for i in Tickets():
        print(i)
        taken_ticket = Tickets.pop(-1)
        print('your ticket #: ' + str(taken_ticket))
        print('tickets left: ' + str(Tickets))

        Parking_spot = Parking_Spaces.pop(-1)
        print('your parking spot is #: ' + str(Parking_spot))
        print('spaces left: ' + str(Parking_Spaces))

def Pay_for_Parking():
    
    pass

def Variable():
    print("Your ticket has been paid. You have 15 minutes to leave the garage. Have a great day! ")
    

def Leave_Garage():
    pass

#-----------------------------------------------------------------------------------
#--------------------------------MAIN PART OF CODE----------------------------------
Current_Ticket = {}
Tickets = [1,2,3,4,5,6,7,8,9]
Parking_Spaces = [1,2,3,4,5,6,7,8,9]

def Garage():

    while True:
    
        Welcome = input("Welcome to DS's Parking Garage! If you would like to park please press yes to take a ticket.")

        if Welcome == "yes":
            Take_Ticket()