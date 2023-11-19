import tkinter as tk
from publisher import Publisher
from tkinter import messagebox
import paho.mqtt.client as mqtt
import time


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
    def __init__(self, car_park_id):

        if car_park_id == 1:
            self.car_park = CarParkInfo("1", "Wilson Parking",
                                        "102 Wilson Street", 25,
                                        20, 10)
        elif car_park_id == 2:
            self.car_park = CarParkInfo("2", "QV1 Car Park",
                                        "51 Murry Street", 20,
                                        28, 2)
        elif car_park_id == 3:
            self.car_park = CarParkInfo("3", "CPP Car Park",
                                        "87-89 Pier Str", 21,
                                        35, 30)

        self.displayer = tk.Tk()
        self.displayer.geometry('600x400')
        self.displayer.title(self.car_park.car_park_name)

        # set title
        l_title = tk.Label(self.displayer, text=self.car_park.car_park_name, font=('Arial', 20))
        l_title.grid(row=0, column=0, columnspan=3, pady=(20, 5))

        # set car park info
        # row for car_park_id
        l_11 = tk.Label(self.displayer, text="car_park_id :", font=('Arial', 14))
        l_11.grid(row=1, column=0, sticky="W", pady=(20, 5), padx=(50, 5))
        l_21 = tk.Label(self.displayer, text=f"{self.car_park.car_park_id}", font=('Arial', 14))
        l_21.grid(row=1, column=1, sticky="W", pady=(20, 5))

        # row for car_park_address
        l_12 = tk.Label(self.displayer, text="car_park_address :", font=('Arial', 14))
        l_12.grid(row=2, column=0, sticky="W", pady=5, padx=(50, 5))
        l_22 = tk.Label(self.displayer, text=f"{self.car_park.car_park_address}", font=('Arial', 14))
        l_22.grid(row=2, column=1, sticky="W", pady=5)

        # row for parking_bays
        l_13 = tk.Label(self.displayer, text="parking_bays :", font=('Arial', 14))
        l_13.grid(row=3, column=0, sticky="W", pady=5, padx=(50, 5))
        l_23 = tk.Label(self.displayer, text=f"{self.car_park.parking_bays}", font=('Arial', 14))
        l_23.grid(row=3, column=1, sticky="W", pady=5)

        # row for occupied
        l_14 = tk.Label(self.displayer, text="occupied :", font=('Arial', 14))
        l_14.grid(row=4, column=0, sticky="W", pady=5, padx=(50, 5))
        self.l_occupied = tk.Label(self.displayer, text=f"{self.car_park.occupied}", font=('Arial', 14))
        self.l_occupied.grid(row=4, column=1, sticky="W", pady=5)

        # row for temperature
        l_15 = tk.Label(self.displayer, text="temperature :", font=('Arial', 14))
        l_15.grid(row=5, column=0, sticky="W", pady=5, padx=(50, 5))

        # create a frame to store the entry control and ℃ label
        frame = tk.Frame(self.displayer)
        frame.grid(row=5,  column=1, sticky="W", pady=5)
        e_temperature = tk.Entry(frame, width=5, font=('Arial', 14))
        e_temperature.insert(0, self.car_park.temperature)
        e_temperature.pack(side=tk.LEFT)
        l_25 = tk.Label(frame, text="℃", font=('Arial', 14))
        l_25.pack(side=tk.LEFT)

        # add MQTT publisher for transfer temperature.
        self.publisher_temperature = Publisher("UpdateTemperature")

        # 'update temperature' button
        def update_temperature():
            self.publisher_temperature.publish_msg(f"{self.car_park.car_park_id},{e_temperature.get()}")
            self.car_park.temperature = e_temperature.get()
            messagebox.showinfo("Message",
                                f"Temperature has been set as {self.car_park.temperature}℃ "
                                f"for Car Park {self.car_park.car_park_id}.")
        b_entry = tk.Button(self.displayer, text="Update Temperature", command=update_temperature, font=('Arial', 14))
        b_entry.grid(row=5, column=2, sticky="W", pady=5)

        # add MQTT subscriber for Car-IN Car-OUT
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        # Connect to MQTT broker
        self.client.connect("localhost", 1883, 600)
        # Start MQTT loop in a non-blocking way
        self.client.loop_start()

        # add MQTT publisher for transfer car park info every 10 second.
        self.publisher_car_park = Publisher("CarParkInfo")
        # Publish messages every 10 seconds
        while True:
            # Publish a message to a specific topic
            message = (f"{self.car_park.car_park_id},{self.car_park.car_park_name},{self.car_park.car_park_address},"
                       f"{self.car_park.temperature}, {self.car_park.parking_bays},{self.car_park.occupied}")
            self.publisher_car_park.publish_msg(message)
            print(f"Message published: {message}")
            time.sleep(10)  # Sleep for 10 seconds

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
        if car_park_id == self.car_park.car_park_id:
            if act == 'in':
                self.car_park.occupied += 1
            if act == 'out':
                self.car_park.occupied -= 1
            self.l_occupied.config(text=self.car_park.occupied)

    def run(self):
        self.displayer.mainloop()


if __name__ == "__main__":
    # app = CarPark(1)
    app = CarPark(2)
    # app = CarPark(3)
    app.run()
