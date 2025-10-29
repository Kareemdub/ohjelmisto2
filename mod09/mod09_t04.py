#tehtävä 4
import random
#TEHÄTÄVÄ 2

class Car:
    def __init__(self, plate, top_speed = 0, speed = 0, trip = 0):
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
        self.trip = self.speed * distance + self.trip


cars = [] #autolistan teko matin ohjeistuksella
for i in range(10): #luodaan 10 autoa listaan cars
    plate_number = i
    max = random.randint(100, 200)
    cars.append(Car(f"ABC-{plate_number + 1}", max))

for car in cars:
    print(f"auton rekkari: {car.plate} nopeus: {car.speed}. Huippunopeus on {car.top_speed} "
          f"Auto on matkannut {car.trip} kilometriä")

while car.trip < 10000:

    for car in cars:
        if car.trip < 10000:
            car.accelerate(random.randint(-10, 15))
            car.distance(1)
            print(car.plate, car.trip)
        else:
            break

for car in cars:
    print(f"auton rekkari: {car.plate} nopeus: {car.speed}. Huippunopeus on {car.top_speed} "
          f"Auto on matkannut {car.trip} kilometriä")

#    for car in cars:
##        car.distance(1)
#        random_speed = random.randint(-10, 15)
#        car.accelerate(random_speed)
#        print(car.trip)



#print(car1.plate, car1.top_speed, car1.speed, car1.trip)