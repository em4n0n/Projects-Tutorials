class Beach:

    def __init__(self, location, water_color, temperature) -> None: #added location as a different parameter. passed into the initializaiton function
        self.location = location #to locate this attribute, we need to call self. we call this instance later. these are instance variables
        self.water_color = water_color
        self.temperature = temperature
        self.heat_rating = 'hot' if temperature > 80 else 'cool'

    def add_part(self, part):
        self.part.append(part)

cape_cod_beach = Beach('Cape Cod', 'dark blue', 70)
cancun_beach = Beach('Cancun', 'crystal blue', 90)
print(cape_cod_beach.part)
cape_cod_beach.add_part('rock')
print(cape_cod_beach)
