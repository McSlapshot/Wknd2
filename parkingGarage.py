# Start Your Code here

from re import T


class Parking_Garage():

    def add_car(tickets, spots):
        if len(tickets) == 0:
            print("We don't have any space available")
        else:
            print("Here is your ticket " + str(tickets.pop()) + " and your parking spot is " + str(spots.pop()))


    def Pay_for_Parking(tickets, spots):
        Price = input("Please input $5 to pay your ticket")
        if Price == '$5':
            Parking_Garage.remove_car(tickets, spots)
            print("Thank you! The ticket has been paid, you have 15 min to leave, come again!") 
        else:
            print("Incorrect payment, try again")
            return    


    def remove_car(tickets, spots):
        paid = input('Do you want to pay your ticket? y/n')
        if len(tickets) == 9:
            print("ticket paid for, have a great day!")
        elif paid.lower() == 'y':
            tickets.append(tickets[-1]+1)
            spots.append(spots[-1]+1)
            print("You have paid your ticket, have a great day!")
        else:
            paid.lower() == 'n'
            print("Please come back when you wish to pay your ticket")
            


#-----------------------------------------------------------------------------------
#--------------------------------MAIN PART OF CODE----------------------------------

spots = [1,2,3,4,5,6,7,8,9]
tickets = [1,2,3,4,5,6,7,8,9]


def Garage():
    while True:
        Welcome = input("Welcome to DS's Parking Garage! If you would like to 't' take ticket, 'p' pay for parking or 'l' to leave.")
        if Welcome == "t":
            Parking_Garage.add_car(tickets, spots)            
        elif Welcome == 'p':
            Parking_Garage.Pay_for_Parking(tickets, spots)
        elif Welcome == "l":
            Parking_Garage.remove_car(tickets, spots)
            break
Garage()