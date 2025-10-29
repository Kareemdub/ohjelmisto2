#TEHÄTÄVÄ 2

class Car:
    def __init__(self, plate = 0, top_speed = 0, speed = 0, trip = 0):
        self.plate = plate
        self.speed = speed
        self.trip = trip
        self.top_speed = top_speed
    def accelerate(self, acceleration):
        self.speed = self.speed + acceleration
        if self.speed > self.top_speed:
            self.speed = self.top_speed
        elif self.speed < 0:
            self.speed = 0
    def distance(self, distance):
        self.trip = self.speed * distance

#

cars = [] #autolistan teko matin ohjeistuksella
for i in range(9): #luodaan 9 autoa listaan cars
    cars.append(Car())
cars[0].plate ="ABC123" #ensimmäisen auton rekkari ja vauhtimuutokset
cars[0].top_speed = 142
cars[0].accelerate(30)
print(cars[0].speed)
cars[0].accelerate(70)
print(cars[0].speed)
cars[0].accelerate(50)
print(cars[0].speed)
print(cars[0].trip)
cars[0].distance(20)
for car in cars:
    print(f"auton rekkari: {car.plate}. nopeus: {car.speed}. "
          f"maximinopeus {car.top_speed}. Auto on matkannut {car.trip} kilometriä")




#print(car1.plate, car1.top_speed, car1.speed, car1.trip)