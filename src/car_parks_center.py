import tkinter as tk
import paho.mqtt.client as mqtt
from car_park import CarParkInfo


class CarParksCenter:

    def __init__(self):

        self.car_park_1 = CarParkInfo("1", "Wilson Parking", "102 Wilson Street", 25, 20, 10)
        self.car_park_2 = CarParkInfo("2", "QV1 Car Park", "51 Murry Street", 20, 28, 2)
        self.car_park_3 = CarParkInfo("3", "CPP Car Park", "87-89 Pier Str", 21, 35, 30)

        self.displayer = tk.Tk()
        self.displayer.geometry('1200x400')
        self.displayer.title("Moondalup CarPark Management Center")

        l_title = tk.Label(self.displayer, text='Moondalup CarPark Management Center Monitor',
                           font=('Arial', 28))
        l_title.grid(row=0, column=0, columnspan=6, pady=(20, 5))

        # set for car_park_1
        # set Properties' name
        l_11 = tk.Label(self.displayer, text="car_park_id :", font=('Arial', 14))
        l_12 = tk.Label(self.displayer, text="car_park_name :", font=('Arial', 14))
        l_13 = tk.Label(self.displayer, text="car_park_address :", font=('Arial', 14))
        l_14 = tk.Label(self.displayer, text="temperature :", font=('Arial', 14))
        l_15 = tk.Label(self.displayer, text="parking_bays :", font=('Arial', 14))
        l_16 = tk.Label(self.displayer, text="occupied :", font=('Arial', 14))

        l_11.grid(row=1, column=0, sticky="W", pady=(20, 5), padx=(50, 5))
        l_12.grid(row=2, column=0, sticky="W", pady=5, padx=(50, 5))
        l_13.grid(row=3, column=0, sticky="W", pady=5, padx=(50, 5))
        l_14.grid(row=4, column=0, sticky="W", pady=5, padx=(50, 5))
        l_15.grid(row=5, column=0, sticky="W", pady=5, padx=(50, 5))
        l_16.grid(row=6, column=0, sticky="W", pady=5, padx=(50, 5))

        # set values
        l_21 = tk.Label(self.displayer, text=f"{self.car_park_1.car_park_id}", font=('Arial', 14))
        l_22 = tk.Label(self.displayer, text=f"{self.car_park_1.car_park_name}", font=('Arial', 14))
        l_23 = tk.Label(self.displayer, text=f"{self.car_park_1.car_park_address}", font=('Arial', 14))
        self.l_car_park_1_temperature = tk.Label(self.displayer, text=f"{self.car_park_1.temperature}℃",
                                                 font=('Arial', 14))
        l_25 = tk.Label(self.displayer, text=f"{self.car_park_1.parking_bays}", font=('Arial', 14))
        self.l_car_park_1_occupied = tk.Label(self.displayer, text=f"{self.car_park_1.occupied}", font=('Arial', 14))

        # this will arrange entry widgets
        l_21.grid(row=1, column=1, sticky="W", pady=(20, 5))
        l_22.grid(row=2, column=1, sticky="W", pady=5)
        l_23.grid(row=3, column=1, sticky="W", pady=5)
        self.l_car_park_1_temperature.grid(row=4, column=1, sticky="W", pady=5)
        l_25.grid(row=5, column=1, sticky="W", pady=5)
        self.l_car_park_1_occupied.grid(row=6, column=1, sticky="W", pady=5)

        # set for car_park_2
        # set Properties' name
        l_31 = tk.Label(self.displayer, text="car_park_id :", font=('Arial', 14))
        l_32 = tk.Label(self.displayer, text="car_park_name :", font=('Arial', 14))
        l_33 = tk.Label(self.displayer, text="car_park_address :", font=('Arial', 14))
        l_34 = tk.Label(self.displayer, text="temperature :", font=('Arial', 14))
        l_35 = tk.Label(self.displayer, text="parking_bays :", font=('Arial', 14))
        l_36 = tk.Label(self.displayer, text="occupied :", font=('Arial', 14))

        l_31.grid(row=1, column=2, sticky="W", pady=(20, 5), padx=(60, 5))
        l_32.grid(row=2, column=2, sticky="W", pady=5, padx=(60, 5))
        l_33.grid(row=3, column=2, sticky="W", pady=5, padx=(60, 5))
        l_34.grid(row=4, column=2, sticky="W", pady=5, padx=(60, 5))
        l_35.grid(row=5, column=2, sticky="W", pady=5, padx=(60, 5))
        l_36.grid(row=6, column=2, sticky="W", pady=5, padx=(60, 5))

        # set values
        l_41 = tk.Label(self.displayer, text=f"{self.car_park_2.car_park_id}", font=('Arial', 14))
        l_42 = tk.Label(self.displayer, text=f"{self.car_park_2.car_park_name}", font=('Arial', 14))
        l_43 = tk.Label(self.displayer, text=f"{self.car_park_2.car_park_address}", font=('Arial', 14))
        self.l_car_park_2_temperature = tk.Label(self.displayer, text=f"{self.car_park_2.temperature}℃",
                                                 font=('Arial', 14))
        l_45 = tk.Label(self.displayer, text=f"{self.car_park_2.parking_bays}", font=('Arial', 14))
        self.l_car_park_2_occupied = tk.Label(self.displayer, text=f"{self.car_park_2.occupied}", font=('Arial', 14))

        # this will arrange entry widgets
        l_41.grid(row=1, column=3, sticky="W", pady=(20, 5))
        l_42.grid(row=2, column=3, sticky="W", pady=5)
        l_43.grid(row=3, column=3, sticky="W", pady=5)
        self.l_car_park_2_temperature .grid(row=4, column=3, sticky="W", pady=5)
        l_45.grid(row=5, column=3, sticky="W", pady=5)
        self.l_car_park_2_occupied.grid(row=6, column=3, sticky="W", pady=5)

        # set for car_park_3
        # set Properties' name
        l_51 = tk.Label(self.displayer, text="car_park_id :", font=('Arial', 14))
        l_52 = tk.Label(self.displayer, text="car_park_name :", font=('Arial', 14))
        l_53 = tk.Label(self.displayer, text="car_park_address :", font=('Arial', 14))
        l_54 = tk.Label(self.displayer, text="temperature :", font=('Arial', 14))
        l_55 = tk.Label(self.displayer, text="parking_bays :", font=('Arial', 14))
        l_56 = tk.Label(self.displayer, text="occupied :", font=('Arial', 14))

        l_51.grid(row=1, column=4, sticky="W", pady=(20, 5), padx=(60, 5))
        l_52.grid(row=2, column=4, sticky="W", pady=5, padx=(60, 5))
        l_53.grid(row=3, column=4, sticky="W", pady=5, padx=(60, 5))
        l_54.grid(row=4, column=4, sticky="W", pady=5, padx=(60, 5))
        l_55.grid(row=5, column=4, sticky="W", pady=5, padx=(60, 5))
        l_56.grid(row=6, column=4, sticky="W", pady=5, padx=(60, 5))

        # set values
        l_61 = tk.Label(self.displayer, text=f"{self.car_park_3.car_park_id}", font=('Arial', 14))
        l_62 = tk.Label(self.displayer, text=f"{self.car_park_3.car_park_name}", font=('Arial', 14))
        l_63 = tk.Label(self.displayer, text=f"{self.car_park_3.car_park_address}", font=('Arial', 14))
        self.l_car_park_3_temperature = tk.Label(self.displayer, text=f"{self.car_park_3.temperature}℃",
                                                 font=('Arial', 14))
        l_65 = tk.Label(self.displayer, text=f"{self.car_park_3.parking_bays}", font=('Arial', 14))
        self.l_car_park_3_occupied = tk.Label(self.displayer, text=f"{self.car_park_3.occupied}", font=('Arial', 14))

        # this will arrange entry widgets
        l_61.grid(row=1, column=5, sticky="W", pady=(20, 5))
        l_62.grid(row=2, column=5, sticky="W", pady=5)
        l_63.grid(row=3, column=5, sticky="W", pady=5)
        self.l_car_park_3_temperature .grid(row=4, column=5, sticky="W", pady=5)
        l_65.grid(row=5, column=5, sticky="W", pady=5)
        self.l_car_park_3_occupied.grid(row=6, column=5, sticky="W", pady=5)

        # Initialize MQTT subscriber
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Connect to MQTT broker
        self.client.connect("localhost", 1883, 600)

        # Start MQTT loop in a non-blocking way
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribe to two topics
        client.subscribe("CarAct")
        client.subscribe("UpdateTemperature")

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        topic = msg.topic
        print("topic:" + topic + ",Received message: " + message)

        if topic == 'CarAct':
            # get effective info
            act = str(message).split(",")[0]
            car_park_id = str(message).split(",")[1]

            # update occupied number for corresponding car park
            if act == 'in' and car_park_id == '1':
                self.car_park_1.occupied += 1
                self.l_car_park_1_occupied.config(text=self.car_park_1.occupied)
            if act == 'out' and car_park_id == '1':
                self.car_park_1.occupied -= 1
                self.l_car_park_1_occupied.config(text=self.car_park_1.occupied)

            if act == 'in' and car_park_id == '2':
                self.car_park_2.occupied += 1
                self.l_car_park_2_occupied.config(text=self.car_park_2.occupied)
            if act == 'out' and car_park_id == '2':
                self.car_park_2.occupied -= 1
                self.l_car_park_2_occupied.config(text=self.car_park_2.occupied)

            if act == 'in' and car_park_id == '3':
                self.car_park_3.occupied += 1
                self.l_car_park_3_occupied.config(text=self.car_park_3.occupied)
            if act == 'out' and car_park_id == '3':
                self.car_park_3.occupied -= 1
                self.l_car_park_3_occupied.config(text=self.car_park_3.occupied)

        if topic == 'UpdateTemperature':
            # get effective info
            car_park_id = str(message).split(",")[0]
            temperature = str(message).split(",")[1]
            if car_park_id == '1':
                self.car_park_1.temperature = temperature
                self.l_car_park_1_temperature.config(text=f"{temperature}℃")
            if car_park_id == '2':
                self.car_park_2.temperature = temperature
                self.l_car_park_2_temperature.config(text=f"{temperature}℃")
            if car_park_id == '3':
                self.car_park_3.temperature = temperature
                self.l_car_park_3_temperature.config(text=f"{temperature}℃")

    def run(self):
        self.displayer.mainloop()


if __name__ == "__main__":
    app = CarParksCenter()
    app.run()
