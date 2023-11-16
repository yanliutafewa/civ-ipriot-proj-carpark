from car_park import CarPark
from car_park_displayer import CarParkDisplayer


class CarParkManageCenter:

    def __init__(self):
        self.car_park_list = list()
        self.car_park_displayer = CarParkDisplayer()
        # unfinished.


    def init_car_park_list(self):
        car_park = CarPark("1", "Wilson Parking", "102 Wilson Street", 25, 20, 10)
        self.car_park_list.append(car_park)
        car_park = CarPark("2", "QV1 Car Park", "51 Murry Street", 20, 28, 2)
        self.car_park_list.append(car_park)
        car_park = CarPark("3", "CPP Car Park", "87-89 Pier Str", 21, 35, 30)
        self.car_park_list.append(car_park)



if __name__ == '__main__':
    """
    TODO: 
    Run each of this classes in a separate terminal. You should see the CarParkDisplay update 
    when you click the buttons in the CarDetector.
    """
    CarParkManageCenter()