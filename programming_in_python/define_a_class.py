class House:
    '''
    THis is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house

apt = House()
print(apt.num_rooms)
print(House.num_rooms)

apt.num_rooms = 7
print(apt.num_rooms)
print(House.num_rooms)