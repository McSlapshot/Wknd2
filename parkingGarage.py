# Start Your Code here
class Parking_Garage():
    def __init__(self):
        self.spots = [1,2,3,4,5,6,7,8,9]
        self.tickets = [1,2,3,4,5,6,7,8,9]

    def add_car(self):
        if len(self.tickets) == 0:
            print("We don't have any space available")
        else:
            print("Here is your ticket " + str(self.tickets.pop()) + " and your parking spot is " + str(self.spots.pop()))


    def Pay_for_Parking(self):
        Price = input("Please input $5 to pay your ticket")
        if Price == '$5':
            self.remove_car()
            print("Thank you! The ticket has been paid, you have 15 min to leave, come again!") 
        else:
            print("Incorrect payment, try again")
            return    


    def remove_car(self):
        paid = input('Do you want to pay your ticket? y/n')
        if len(self.tickets) == 9:
            print("ticket paid for, have a great day!")
        elif paid.lower() == 'y':
            self.tickets.append(self.tickets[-1]+1)
            self.spots.append(self.spots[-1]+1)
            print("You have paid your ticket, have a great day!")
        else:
            paid.lower() == 'n'
            print("Please come back when you wish to pay your ticket")
            
#-----------------------------------------------------------------------------------
#--------------------------------MAIN PART OF CODE----------------------------------

    def run(self):
        while True:
            Welcome = input("Welcome to DS's Parking Garage! If you would like to 't' take ticket, 'p' pay for parking or 'l' to leave.")
            if Welcome == "t":
                self.add_car()            
            elif Welcome == 'p':
                self.Pay_for_Parking()
            elif Welcome == "l":
                self.remove_car()
                break
g = Parking_Garage()
g.run()