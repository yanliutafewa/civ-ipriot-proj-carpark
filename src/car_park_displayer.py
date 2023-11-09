import random
from window_displayer import WindowDisplayer
import threading
import time


class CarParkDisplayer:
    """
    Provides a simple display of the car park status. This is a skeleton only.
    The class is designed to be customizable without requiring and understanding of tkinter or threading.
    """
    # determines what fields appear in the UI
    fields = ['Available bays', 'Temperature', 'At']

    def __init__(self):
        self.window = WindowDisplayer(
            'Moondalup', CarParkDisplayer.fields)
        updater = threading.Thread(target=self.check_updates)
        updater.daemon = True
        updater.start()
        self.window.show()

    def check_updates(self):
        # TODO: This is where you should manage the MQTT subscription
        while True:
            # NOTE: Dictionary keys *must* be the same as the class fields
            field_values = dict(zip(CarParkDisplayer.fields, [
                f'{random.randint(0, 150):03d}',
                f'{random.randint(0, 45):02d}℃',
                time.strftime("%H:%M:%S")]))
            # Pretending to wait on updates from MQTT
            time.sleep(random.randint(1, 10))
            # When you get an update, refresh the display.
            self.window.update(field_values)


if __name__ == '__main__':
    """
    TODO: 
    Run each of this classes in a separate terminal. You should see the CarParkDisplay update 
    when you click the buttons in the CarDetector.
    """
    CarParkDisplayer()
