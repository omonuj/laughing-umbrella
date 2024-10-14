class Television:
    def __init__(self):
        self._volume = 7
        self._channel = 4
        self.is_on = False

    @property
    def volume(self):
        return self._volume

    @property
    def channel(self):
        return self._channel

    def get_state(self):
        if self.is_on:
            return True
        else:
            return False

    def increase_volume(self):
        if self._volume < 10:
            self._volume += 1
        else:
            raise ValueError("Volume cannot exceed 10")

    def decrease_volume(self):
        if self._volume > 1:
            self._volume -= 1
        else:
            raise ValueError("Volume cannot go bellow 1")
    def set_channel(self, channel):
        if 1 <= channel <= 100:
            self._channel = channel
        else:
            raise ValueError("Channel must be between 1 and 100")

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_volume(self, volume):
        self._volume = volume

    def get_volume(self):
        return self._volume

    def get_channel(self):
        return self._channel

    def increase_channel(self):
        if self._channel < 100:
            self._channel += 1
        else:
            raise ValueError("Channel cannot exceed 100")

    def decrease_channel(self):
       if self._channel > 1:
           self._channel -= 1
       else:
           raise ValueError("Channel cannot decrease below 1")

    def reset_channel(self):
        self._channel = 1

    def reset_volume(self):
        self._volume = 1