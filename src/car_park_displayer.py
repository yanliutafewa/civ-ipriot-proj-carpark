import random
from window_displayer import WindowDisplayer
from car_park import CarPark
import threading
import time


class CarParkDisplayer:
    """
    Provides a simple display of the car park status. This is a skeleton only.
    The class is designed to be customizable without requiring and understanding of tkinter or threading.
    """
    # determines what fields appear in the UI
    fields = ['CarPark No.', 'CarPark Name', 'CarPark Address', 'Temperature', 'Available bays', 'At']

    def __init__(self):
        self.window = WindowDisplayer(
            'Moondalup CarPark Management Center', CarParkDisplayer.fields)
        updater = threading.Thread(target=self.check_updates)
        updater.daemon = True
        updater.start()
        self.window.show()

    def check_updates(self, car_park: CarPark):
        # TODO: This is where you should manage the MQTT subscription
        while True:
            # NOTE: Dictionary keys *must* be the same as the class fields
            field_values = dict(zip(CarParkDisplayer.fields, [
                f'{car_park.car_park_id}',
                f'{car_park.car_park_name}',
                f'{car_park.car_park_address}',
                f'{car_park.temperature:02d}℃',
                f'{car_park.parking_bays - car_park.occupied:03d}',
                time.strftime("%H:%M:%S")]))
            # Pretending to wait on updates from MQTT
            time.sleep(3)
            # When you get an update, refresh the display.
            self.window.update(field_values)


if __name__ == '__main__':
    """
    TODO: 
    Run each of this classes in a separate terminal. You should see the CarParkDisplay update 
    when you click the buttons in the CarDetector.
    """
    CarParkDisplayer()
