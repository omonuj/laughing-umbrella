class AirConditioner:

    def __init__(self):
        self.is_on = False
        self.temperature = 24
        self.cooling_level = 10

    def toggle_power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def get_status(self):
        return "ON" if self.is_on else "OFF"

    def get_temperature(self):
        return self.temperature

    def get_cooling_level(self):
        return self.cooling_level

    def increase_temperature(self):
        if self.is_on and self.temperature < 30:
            self.temperature += 1
            self.cooling_level -= 1

    def decrease_temperature(self):
        if self.is_on and self.temperature > 16:
            self.temperature -= 1
            self.cooling_level += 1

    def set_temperature(self, temperature):
       self.temperature = temperature
       ...

    def set_cooling_level(self, level):
        self.cooling_level = level
    ...



