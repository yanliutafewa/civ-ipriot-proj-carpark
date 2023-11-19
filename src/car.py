import tkinter as tk
from car_park import CarParkInfo
from tkinter import ttk
from tkinter import messagebox
import datetime
from publisher import Publisher
import paho.mqtt.client as mqtt


class Car:

    DISPLAY_INIT = '– – –'

    def __init__(self, car_plate, car_model):

        self.car_park_list = list()
        self.car_plate = car_plate
        self.car_model = car_model
        self.entry_time = self.DISPLAY_INIT
        self.entry_car_park_name = self.DISPLAY_INIT
        self.entry_car_park_id = self.DISPLAY_INIT

        self.displayer = tk.Tk()
        self.displayer.geometry('1320x550')
        self.displayer.title(f"Car: {self.car_plate}")

        l_title = tk.Label(self.displayer, text='CAR🚘', font=('Arial', 28))
        l_title.grid(row=0, column=0, columnspan=6, pady=(20, 5))

        l_plate = tk.Label(self.displayer, text="license_plate :", font=('Arial', 16))
        l_plate_value = tk.Label(self.displayer, text=f"{self.car_plate}", font=('Arial', 16))
        l_model = tk.Label(self.displayer, text="car_model :", font=('Arial', 16))
        l_model_value = tk.Label(self.displayer, text=f"{self.car_model}", font=('Arial', 16))
        l_plate.grid(row=1, column=0, sticky="W", pady=(20, 5), padx=(50, 5))
        l_plate_value.grid(row=1, column=1, columnspan=2, sticky="W", pady=(20, 5))
        l_model.grid(row=1, column=2, sticky="W", pady=(20, 5), padx=(50, 5))
        l_model_value.grid(row=1, column=3, sticky="W", pady=(20, 5))

        l_entry_time = tk.Label(self.displayer, text="entry_time :", font=('Arial', 16))
        l_entry_time_value = tk.Label(self.displayer, text=f"{self.entry_time}", font=('Arial', 16))
        l_entry_car_park = tk.Label(self.displayer, text="entry_car_park :", font=('Arial', 16))
        l_entry_car_park_name = tk.Label(self.displayer, text=f"{self.entry_car_park_name}", font=('Arial', 16))

        l_entry_time.grid(row=2, column=0, sticky="W", pady=(20, 5), padx=(50, 5))
        l_entry_time_value.grid(row=2, column=1, columnspan=2, sticky="W", pady=(20, 5))
        l_entry_car_park.grid(row=2, column=2, sticky="W", pady=(20, 5), padx=(50, 5))
        l_entry_car_park_name.grid(row=2, column=3, sticky="W", pady=(20, 5))

        l_car_park = tk.Label(self.displayer, text="Car Park :", font=('Arial', 16))
        l_car_park.grid(row=3, column=0, sticky="W", pady=(20, 5), padx=(50, 5))

        # combobox for select car park
        selected_number = tk.StringVar()
        cap_park_cb = ttk.Combobox(self.displayer, textvariable=selected_number, font=('Arial', 16), width=10)
        cap_park_cb.grid(row=3, column=1, sticky="W", pady=(20, 5))

        # todo: fix the problem
        # cap_park_cb['values'] = [car_park_1.car_park_id, car_park_2.car_park_id, car_park_3.car_park_id]
        cap_park_cb['values'] = [1, 2, 3]

        # prevent typing a value
        cap_park_cb['state'] = 'readonly'

        # add publisher
        self.publisher = Publisher("CarAct")

        # 'entry' button
        def entry_car_park():
            self.publisher.publish_msg(f"in,{selected_number.get()}")
            # todo: fix the problem
            """ 
            if selected_number.get() == car_park_1.car_park_id:
                self.entry_car_park_name = car_park_1.car_park_name
                self.entry_car_park_id = car_park_1.car_park_id
            if selected_number.get() == car_park_2.car_park_id:
                self.entry_car_park_name = car_park_2.car_park_name
                self.entry_car_park_id = car_park_2.car_park_id
            if selected_number.get() == car_park_3.car_park_id:
                self.entry_car_park_name = car_park_3.car_park_name
                self.entry_car_park_id = car_park_3.car_park_id
            """

            l_entry_time_value.config(text=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            l_entry_car_park_name.config(text=self.entry_car_park_name)
            messagebox.showinfo("Message", f"Welcome to [{self.entry_car_park_name}].")

        b_entry = tk.Button(self.displayer, text="Entry", command=entry_car_park, font=('Arial', 16))
        b_entry.grid(row=3, column=2, sticky="W", pady=(20, 5), padx=(50, 5))

        # 'exit' button
        def exit_car_park():
            self.publisher.publish_msg(f"out,{self.entry_car_park_id}")
            l_entry_time_value.config(text=self.DISPLAY_INIT)
            l_entry_car_park_name.config(text=self.DISPLAY_INIT)
            messagebox.showinfo("Message", f"Thank you for using [{self.entry_car_park_name}].")

        b_exit = tk.Button(self.displayer, text="Exit", command=exit_car_park, font=('Arial', 16))
        b_exit.grid(row=3, column=3, sticky="W", pady=(20, 5), padx=(50, 5))

        # set for car_park_1 display
        l_11 = tk.Label(self.displayer, text="car_park_id :", font=('Arial', 14))
        l_12 = tk.Label(self.displayer, text="car_park_name :", font=('Arial', 14))
        l_13 = tk.Label(self.displayer, text="car_park_address :", font=('Arial', 14))
        l_14 = tk.Label(self.displayer, text="temperature :", font=('Arial', 14))
        l_15 = tk.Label(self.displayer, text="available :", font=('Arial', 14))

        l_11.grid(row=4, column=0, sticky="W", pady=(20, 5), padx=(50, 5))
        l_12.grid(row=5, column=0, sticky="W", pady=5, padx=(50, 5))
        l_13.grid(row=6, column=0, sticky="W", pady=5, padx=(50, 5))
        l_14.grid(row=7, column=0, sticky="W", pady=5, padx=(50, 5))
        l_15.grid(row=8, column=0, sticky="W", pady=5, padx=(50, 5))

        # set values
        l_1_car_park_id = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))
        l_1_car_park_name = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))
        l_1_car_park_address = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))
        l_1_temperature = tk.Label(self.displayer, text=f"{self.DISPLAY_INIT}℃", font=('Arial', 14))
        l_1_available = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))

        # this will arrange entry widgets
        l_1_car_park_id.grid(row=4, column=1, sticky="W", pady=(20, 5))
        l_1_car_park_name.grid(row=5, column=1, sticky="W", pady=5)
        l_1_car_park_address.grid(row=6, column=1, sticky="W", pady=5)
        l_1_temperature.grid(row=7, column=1, sticky="W", pady=5)
        l_1_available.grid(row=8, column=1, sticky="W", pady=5)

        # set for car_park_2 display
        l_31 = tk.Label(self.displayer, text="car_park_id :", font=('Arial', 14))
        l_32 = tk.Label(self.displayer, text="car_park_name :", font=('Arial', 14))
        l_33 = tk.Label(self.displayer, text="car_park_address :", font=('Arial', 14))
        l_34 = tk.Label(self.displayer, text="temperature :", font=('Arial', 14))
        l_35 = tk.Label(self.displayer, text="available :", font=('Arial', 14))

        l_31.grid(row=4, column=2, sticky="W", pady=(20, 5), padx=(60, 5))
        l_32.grid(row=5, column=2, sticky="W", pady=5, padx=(60, 5))
        l_33.grid(row=6, column=2, sticky="W", pady=5, padx=(60, 5))
        l_34.grid(row=7, column=2, sticky="W", pady=5, padx=(60, 5))
        l_35.grid(row=8, column=2, sticky="W", pady=5, padx=(60, 5))

        # set values
        l_2_car_park_id = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))
        l_2_car_park_name = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))
        l_2_car_park_address = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))
        l_2_temperature = tk.Label(self.displayer, text=f"{self.DISPLAY_INIT}℃", font=('Arial', 14))
        l_2_available = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))

        # this will arrange entry widgets
        l_2_car_park_id.grid(row=4, column=3, sticky="W", pady=(20, 5))
        l_2_car_park_name.grid(row=5, column=3, sticky="W", pady=5)
        l_2_car_park_address.grid(row=6, column=3, sticky="W", pady=5)
        l_2_temperature.grid(row=7, column=3, sticky="W", pady=5)
        l_2_available.grid(row=8, column=3, sticky="W", pady=5)

        # set for car_park_3 display
        l_51 = tk.Label(self.displayer, text="car_park_id :", font=('Arial', 14))
        l_52 = tk.Label(self.displayer, text="car_park_name :", font=('Arial', 14))
        l_53 = tk.Label(self.displayer, text="car_park_address :", font=('Arial', 14))
        l_54 = tk.Label(self.displayer, text="temperature :", font=('Arial', 14))
        l_55 = tk.Label(self.displayer, text="available :", font=('Arial', 14))

        l_51.grid(row=4, column=4, sticky="W", pady=(20, 5), padx=(60, 5))
        l_52.grid(row=5, column=4, sticky="W", pady=5, padx=(60, 5))
        l_53.grid(row=6, column=4, sticky="W", pady=5, padx=(60, 5))
        l_54.grid(row=7, column=4, sticky="W", pady=5, padx=(60, 5))
        l_55.grid(row=8, column=4, sticky="W", pady=5, padx=(60, 5))

        # set values
        l_3_car_park_id = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))
        l_3_car_park_name = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))
        l_3_car_park_address = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))
        l_3_temperature = tk.Label(self.displayer, text=f"{self.DISPLAY_INIT}℃", font=('Arial', 14))
        l_3_available = tk.Label(self.displayer, text=self.DISPLAY_INIT, font=('Arial', 14))

        # this will arrange entry widgets
        l_3_car_park_id.grid(row=4, column=5, sticky="W", pady=(20, 5))
        l_3_car_park_name.grid(row=5, column=5, sticky="W", pady=5)
        l_3_car_park_address.grid(row=6, column=5, sticky="W", pady=5)
        l_3_temperature.grid(row=7, column=5, sticky="W", pady=5)
        l_3_available.grid(row=8, column=5, sticky="W", pady=5)

        # add MQTT subscriber for receiving car park info
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        # Connect to MQTT broker
        self.client.connect("localhost", 1883, 600)
        # Start MQTT loop in a non-blocking way
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribe to a topic upon successful connection
        client.subscribe("CarParkInfo")

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        print("Received message: " + message)

        # get effective info
        car_park_id = str(message).split(",")[0]
        car_park_name = str(message).split(",")[1]
        car_park_address = str(message).split(",")[2]
        temperature = str(message).split(",")[3]
        parking_bays = str(message).split(",")[4]
        occupied = str(message).split(",")[5]
        available = int(parking_bays) - int(occupied)

        exist = False
        for each_car_park in self.car_park_list:
            if car_park_id == each_car_park.car_park_id:
                exist = True
        if not exist:
            car_park_info = CarParkInfo(car_park_id, car_park_name, car_park_address,
                                        temperature, parking_bays, occupied)
            self.car_park_list.append(car_park_info)

        # todo: set info to the corresponding position for the final item of self.car_park_list

    def run(self):
        self.displayer.mainloop()


if __name__ == '__main__':

    app = Car('JYQ-4567', car_model='COUPE')
    app.run()
