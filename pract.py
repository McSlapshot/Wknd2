Tickets = [1,2,3,4,5]
taken_ticket = Tickets.pop(-1)
print('your ticket #: ' + str(taken_ticket))
print('tickets left: ' + str(Tickets))

def __init__(self, spots_available, Pay_for_Parking, add_car, remove_car):
        self.spots_available = spots_available
        self.Pay_for_Parking = Pay_for_Parking
        self.add_car = add_car
        self.remove_car = remove_car
