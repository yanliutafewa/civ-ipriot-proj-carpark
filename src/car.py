class Car:
    DISPLAY_INIT = '– – –'

    def __init__(self, car_plate, car_model):
        self.car_plate = car_plate
        self.car_model = car_model
        self.entry_time = self.DISPLAY_INIT
        self.entry_car_park_id = self.DISPLAY_INIT
        self.entry_car_park_name = self.DISPLAY_INIT
