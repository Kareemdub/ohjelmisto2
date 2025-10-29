#tehtävä 2
from operator import index


class Building:
    def __init__(self, elevators, bot_floor = 1, top_floor = 8):
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(elevators):
            self.elevators.append(Elevator(i + 1,bot_floor))

    def use_elevator(self, elevator, floor):
        self.elevators[elevator].move_to(floor)

    def tulosta_hissit(self):
        for elevator in self.elevators:
            print(elevator.name)
    def alarm(self):
        for elevator in self.elevators:
            print(f"Palohälytys! Hissi {elevator.name} palaa alimpaan kerrokseen")
            elevator.move_to(self.bot_floor)

class Elevator:
    def __init__(self, name, current_floor = 1, bot_floor = 1, top_floor = 8):
        self.name = name
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.current_floor = current_floor


    def move_to(self, floor):
        while self.current_floor < floor:
            self.move_up()
            print(f"Hissi {self.name} on kerroksesssa {self.current_floor}")

        while self.current_floor > floor:
            self.move_down()
            print(f"Hissi {self.name} on kerroksessa {self.current_floor}")

    def move_up(self):
        self.current_floor = self.current_floor + 1


    def move_down(self):
        self.current_floor = self.current_floor - 1

building1 = Building(2, 1)

#elevator1.move_to(5)
#elevator1.move_to(1)


building1.use_elevator(1,  3)
building1.use_elevator(0, 6)

building1.tulosta_hissit()

building1.alarm()