class AirConditioner:

    def __init__(self):
        self.is_on = False
        self.temperature = 24

    def turn_on(self):
        self.is_on = True