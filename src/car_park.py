import tkinter as tk
from publisher import Publisher
from tkinter import messagebox
import paho.mqtt.client as mqtt
import time
import threading


class CarParkInfo:
    def __init__(self, car_park_id, car_park_name, car_park_address, temperature, parking_bays,
                 occupied):
        self.car_park_id = car_park_id
        self.car_park_name = car_park_name
        self.car_park_address = car_park_address
        self.temperature = temperature
        self.parking_bays = parking_bays
        self.occupied = occupied


class CarPark:
    def __init__(self, displayer, car_park_info):

        self.car_park_info = car_park_info

        displayer.geometry('600x400')
        displayer.title(car_park_info.car_park_name)

        # set title
        l_title = tk.Label(displayer, text=self.car_park_info.car_park_name, font=('Arial', 20))
        l_title.grid(row=0, column=0, columnspan=3, pady=(20, 5))

        # set car park info
        # row for car_park_id
        l_11 = tk.Label(displayer, text="car_park_id :", font=('Arial', 14))
        l_11.grid(row=1, column=0, sticky="W", pady=(20, 5), padx=(50, 5))
        l_21 = tk.Label(displayer, text=f"{self.car_park_info.car_park_id}", font=('Arial', 14))
        l_21.grid(row=1, column=1, sticky="W", pady=(20, 5))

        # row for car_park_address
        l_12 = tk.Label(displayer, text="car_park_address :", font=('Arial', 14))
        l_12.grid(row=2, column=0, sticky="W", pady=5, padx=(50, 5))
        l_22 = tk.Label(displayer, text=f"{self.car_park_info.car_park_address}", font=('Arial', 14))
        l_22.grid(row=2, column=1, sticky="W", pady=5)

        # row for parking_bays
        l_13 = tk.Label(displayer, text="parking_bays :", font=('Arial', 14))
        l_13.grid(row=3, column=0, sticky="W", pady=5, padx=(50, 5))
        l_23 = tk.Label(displayer, text=f"{self.car_park_info.parking_bays}", font=('Arial', 14))
        l_23.grid(row=3, column=1, sticky="W", pady=5)

        # row for occupied
        l_14 = tk.Label(displayer, text="occupied :", font=('Arial', 14))
        l_14.grid(row=4, column=0, sticky="W", pady=5, padx=(50, 5))
        self.l_occupied = tk.Label(displayer, text=f"{self.car_park_info.occupied}", font=('Arial', 14))
        self.l_occupied.grid(row=4, column=1, sticky="W", pady=5)

        # row for temperature
        l_15 = tk.Label(displayer, text="temperature :", font=('Arial', 14))
        l_15.grid(row=5, column=0, sticky="W", pady=5, padx=(50, 5))

        # create a frame to store the entry control and ℃ label
        frame = tk.Frame(displayer)
        frame.grid(row=5,  column=1, sticky="W", pady=5)
        e_temperature = tk.Entry(frame, width=5, font=('Arial', 14))
        e_temperature.insert(0, self.car_park_info.temperature)
        e_temperature.pack(side=tk.LEFT)
        l_25 = tk.Label(frame, text="℃", font=('Arial', 14))
        l_25.pack(side=tk.LEFT)

        # add MQTT publisher for transfer temperature.
        self.publisher_temperature = Publisher("UpdateTemperature")

        # 'update temperature' button
        def update_temperature():
            new_temperature = e_temperature.get()
            # validation
            if not new_temperature.lstrip('-+').isdigit():
                messagebox.showinfo("Error",
                                    f"Please input a digital number for the temperature.")
                return
            self.publisher_temperature.publish_msg(f"{self.car_park_info.car_park_id},{new_temperature}")
            print(f"Topic=UpdateTemperature: {self.car_park_info.car_park_id},{new_temperature}")
            self.car_park_info.temperature = new_temperature
            messagebox.showinfo("Message",
                                f"Temperature has been set as {self.car_park_info.temperature}℃ "
                                f"for Car Park {self.car_park_info.car_park_id}.")
        b_entry = tk.Button(displayer, text="Update Temperature", command=update_temperature, font=('Arial', 14))
        b_entry.grid(row=5, column=2, sticky="W", pady=5)

        # add MQTT publisher for transfer car park info every 3 second.
        self.publisher_car_park_info = Publisher("CarParkInfo")

        # Start the MQTT loop in a separate thread
        mqtt_thread = threading.Thread(target=self.publish_loop)
        mqtt_thread.daemon = True  # Daemonize the thread to stop when the main program exits
        mqtt_thread.start()

        # add MQTT subscriber for Car-IN Car-OUT
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        # Connect to MQTT broker
        self.client.connect("localhost", 1883, 600)
        # Start MQTT loop in a non-blocking way
        self.client.loop_start()

    def publish_loop(self):
        while True:
            # Publish a message to a specific topic
            message = (f"{self.car_park_info.car_park_id},"
                       f"{self.car_park_info.car_park_name},"
                       f"{self.car_park_info.car_park_address},"
                       f"{self.car_park_info.temperature}, "
                       f"{self.car_park_info.parking_bays},"
                       f"{self.car_park_info.occupied}")
            self.publisher_car_park_info.publish_msg(message)
            print(f"Message published: {message}")
            time.sleep(3)  # Sleep for 10 seconds

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribe to a topic upon successful connection
        client.subscribe("CarAct")

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        print("Received message: " + message)

        # get effective info
        act = str(message).split(",")[0]
        car_park_id = str(message).split(",")[1]

        # update occupied number for corresponding car park
        if car_park_id == self.car_park_info.car_park_id:
            if act == 'in':
                self.car_park_info.occupied += 1
            if act == 'out':
                self.car_park_info.occupied -= 1
            self.l_occupied.config(text=self.car_park_info.occupied)


def main():
    car_park_1 = CarParkInfo("1", "Wilson Parking",
                             "102 Wilson Street", 25,
                             20, 10)
    car_park_2 = CarParkInfo("2", "QV1 Car Park",
                             "51 Murry Street", 20,
                             28, 2)
    car_park_3 = CarParkInfo("3", "CPP Car Park",
                             "87-89 Pier Str", 21,
                             35, 30)

    displayer = tk.Tk()
    #CarPark(displayer, car_park_1)
    # CarPark(displayer, car_park_2)
    CarPark(displayer, car_park_3)
    displayer.mainloop()


if __name__ == "__main__":
    main()
