#TEHÄTÄVÄ 1

class Car:
    def __init__(self, plate, top_speed, speed = 0, trip = 0):
        self.plate = plate
        self.speed = speed
        self.trip = trip
        self.top_speed = top_speed
    #def accelerate(self):
    #    self.speed =+ 1


car1 = Car("ABC-123", 142)

#car1.speed = car1.speed + 10,"km/h"

print(car1.plate, car1.top_speed, car1.speed, car1.trip)