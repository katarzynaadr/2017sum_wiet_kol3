class PlanePosition(object):
    # Adding necessery requirements ex. formating and statements
    def __init__(self, current_position=0, max_correction=0.3):
        self.current_position = float(current_position)
        self.max_correction = float(max_correction)

    def show_current_position(self):
        self.current_position_string = 'Current position: {}'.format(self.current_position)
        print(self.current_position_string)

    def tilt_correction(self, tilt):
        self.current_position += tilt

    def correction_flight(self):
        if self.max_correction == self.current_position:
            self.current_position = 0
        elif self.current_position > self.max_correction:
            self.current_position -= self.max_correction
        else:
            self.current_position += self.max_correction

