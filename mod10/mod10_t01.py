#tehtävä 1

class Hissi:
    def __init__(self, bot_floor = 1, top_floor = 8, current_floor = 1):
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.current_floor = current_floor



    def move_to(self, floor):
        while self.current_floor < floor:
            Hissi.move_up(self)
            print(f"Hissi on kerroksessa {self.current_floor}")
            if self.current_floor == floor:
                print(f"Hissi on päämäärässään kerroksessa {self.current_floor}")
        while self.current_floor > floor:
            Hissi.move_down(hissi1)
            print(f"Hissi on kerroksessa {self.current_floor}")
            if self.current_floor == floor:
                print(f"Hissi on päämäärässään kerroksessa {self.current_floor}")
    def move_up(self):
        self.current_floor = self.current_floor + 1

    def move_down(self):
        self.current_floor = self.current_floor - 1


hissi1 = Hissi()
hissi1.move_to(5)
hissi1.move_to(1)