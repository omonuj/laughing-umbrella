class Bike:
    def __init__(self):
        self.is_on = False
        self.speed = 15
        self.gear = 1



    def toggle_power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def turn_on(self):
        self.is_on = True

    def is_on(self):
        return self.is_on

    def turn_off(self):
        self.is_on = False

    def accelerate(self):
        if self.is_on:
            if self.gear == 1:
                self.speed += 1
            elif self.gear == 2:
                self.speed += 2
            elif self.gear == 3:
                self.speed += 3
            elif self.gear == 4:
                self.speed += 4

    def decelerate(self):
        if self.is_on:
            if self.gear == 1:
                self.speed -= 1
            elif self.gear == 2:
                self.speed -= 2
            elif self.gear == 3:
                self.speed -= 3
            elif self.gear == 4:
                self.speed -= 4

    def set_gear(self, gear):
        if 1 <= gear <= 4:
            self.gear = gear

    def get_speed(self):
        return self.speed

    def get_gear(self):
        return self.gear

    def set_speed(self, speed):
        self.speed = speed

    def get_state(self):
        return self.is_on