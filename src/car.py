import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from publisher import Publisher
import paho.mqtt.client as mqtt


class Car:

    DISPLAY_INIT = '– – –'

    def __init__(self, displayer, car_plate, car_model):

        self.car_plate = car_plate
        self.car_model = car_model
        self.entry_time = self.DISPLAY_INIT
        self.entry_car_park_id = self.DISPLAY_INIT
        self.entry_car_park_name = self.DISPLAY_INIT

        displayer.geometry('1200x550')
        displayer.title(f"Car: {self.car_plate}")

        # Configure 3 columns with different weights and minimum sizes
        for i in range(4):
            displayer.grid_columnconfigure(i, weight=1, minsize=300)

        l_title = tk.Label(displayer, text='CAR🚘', font=('Arial', 28))
        l_title.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(20, 5), padx=(20, 5))

        l_plate = tk.Label(displayer, text="license_plate :", font=('Arial', 16))
        l_plate_value = tk.Label(displayer, text=f"{self.car_plate}", font=('Arial', 16))
        l_model = tk.Label(displayer, text="car_model :", font=('Arial', 16))
        l_model_value = tk.Label(displayer, text=f"{self.car_model}", font=('Arial', 16))
        l_plate.grid(row=1, column=0, sticky="W", pady=(20, 5), padx=(50, 5))
        l_plate_value.grid(row=1, column=1, columnspan=2, sticky="W", pady=(20, 5))
        l_model.grid(row=1, column=2, sticky="W", pady=(20, 5), padx=(50, 5))
        l_model_value.grid(row=1, column=3, sticky="W", pady=(20, 5))

        l_entry_time = tk.Label(displayer, text="entry_time :", font=('Arial', 16))
        l_entry_time_value = tk.Label(displayer, text=f"{self.entry_time}", font=('Arial', 16))
        l_entry_car_park = tk.Label(displayer, text="entry_car_park :", font=('Arial', 16))
        l_entry_car_park_name = tk.Label(displayer, text=f"{self.entry_car_park_name}", font=('Arial', 16))

        l_entry_time.grid(row=2, column=0, sticky="W", pady=(20, 5), padx=(50, 5))
        l_entry_time_value.grid(row=2, column=1, columnspan=2, sticky="W", pady=(20, 5))
        l_entry_car_park.grid(row=2, column=2, sticky="W", pady=(20, 5), padx=(50, 5))
        l_entry_car_park_name.grid(row=2, column=3, sticky="W", pady=(20, 5))

        l_car_park = tk.Label(displayer, text="Car Park :", font=('Arial', 16))
        l_car_park.grid(row=3, column=0, sticky="W", pady=(20, 5), padx=(50, 5))

        # combobox for select car park
        selected_number = tk.StringVar()
        self.cap_park_cb = ttk.Combobox(displayer, textvariable=selected_number, font=('Arial', 16), width=10)
        self.cap_park_cb.grid(row=3, column=1, sticky="W", pady=(20, 5))

        # prevent typing a value
        self.cap_park_cb['state'] = 'readonly'

        # add publisher
        self.publisher = Publisher("CarAct")

        # 'entry' button
        def entry_car_park():
            self.publisher.publish_msg(f"{selected_number.get()},in")
            self.entry_car_park_id = selected_number.get()

            for line in self.tv_car_parks.get_children():
                if self.tv_car_parks.item(line)['values'][0] == int(selected_number.get()):
                    # get car_park_name from tree item.
                    self.entry_car_park_name = self.tv_car_parks.item(line)['values'][1]
                    # set entry_time and car_park_name on screen
                    l_entry_time_value.config(text=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
                    l_entry_car_park_name.config(text=self.entry_car_park_name)
                    messagebox.showinfo("Message", f"Welcome to [{self.entry_car_park_name}].")

        b_entry = tk.Button(displayer, text="Entry", command=entry_car_park, font=('Arial', 16))
        b_entry.grid(row=3, column=2, sticky="W", pady=(20, 5), padx=(50, 5))

        # 'exit' button
        def exit_car_park():
            self.publisher.publish_msg(f"{self.entry_car_park_id},out")
            l_entry_time_value.config(text=self.DISPLAY_INIT)
            l_entry_car_park_name.config(text=self.DISPLAY_INIT)
            messagebox.showinfo("Message", f"Thank you for using [{self.entry_car_park_name}].")
            self.entry_car_park_id = self.DISPLAY_INIT
            self.entry_car_park_name = self.DISPLAY_INIT
        b_exit = tk.Button(displayer, text="Exit", command=exit_car_park, font=('Arial', 16))
        b_exit.grid(row=3, column=3, sticky="W", pady=(20, 5), padx=(50, 5))

        l_title = tk.Label(displayer, text='Nearby CarParks', font=('Arial', 20))
        l_title.grid(row=4, column=0, columnspan=4, sticky="nsew", pady=(50, 5), padx=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Calibri', 14, 'bold'))
        style.configure("Treeview", font=('Calibri', 12))

        # Create Treeview widget
        self.tv_car_parks = ttk.Treeview(displayer)
        self.tv_car_parks["columns"] = ("car park id", "car park name", "address", "temperature", "parking bays",
                                        "occupied")
        self.tv_car_parks.column("car park id", width=50, anchor=tk.CENTER)
        self.tv_car_parks.column("car park name", width=50, anchor=tk.CENTER)
        self.tv_car_parks.column("address", width=50, anchor=tk.CENTER)
        self.tv_car_parks.column("temperature", width=50, anchor=tk.CENTER)
        self.tv_car_parks.column("parking bays", width=50, anchor=tk.CENTER)
        self.tv_car_parks.column("occupied", width=50, anchor=tk.CENTER)
        self.tv_car_parks.heading("car park id", text="car park id")
        self.tv_car_parks.heading("car park name", text="car park name")
        self.tv_car_parks.heading("address", text="address")
        self.tv_car_parks.heading("temperature", text="temperature")
        self.tv_car_parks.heading("parking bays", text="parking bays")
        self.tv_car_parks.heading("occupied", text="occupied")
        self.tv_car_parks.grid(row=5, column=0, columnspan=4, sticky="nsew", pady=(20, 5), padx=(20, 20))
        self.tv_car_parks['show'] = 'headings'

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
        # Subscribe to topics upon successful connection
        client.subscribe("UpdateTemperature")
        client.subscribe("CarParkInfo")

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        topic = msg.topic
        print("topic:" + topic + ",Received message: " + message)
        # get car_park_id from message
        car_park_id = str(message).split(",")[0]

        if topic == 'CarParkInfo':
            for line in self.tv_car_parks.get_children():
                if self.tv_car_parks.item(line)['values'][0] == int(car_park_id):
                    self.tv_car_parks.item(line, values=(self.tv_car_parks.item(line)['values'][0],
                                                         self.tv_car_parks.item(line)['values'][1],
                                                         self.tv_car_parks.item(line)['values'][2],
                                                         str(message).split(",")[3] + "℃",
                                                         self.tv_car_parks.item(line)['values'][4],
                                                         str(message).split(",")[5]))
                    return
            # if not existed in treeview tv_car_parks, insert
            self.tv_car_parks.insert("", "end",
                                     values=(str(message).split(",")[0], str(message).split(",")[1],
                                             str(message).split(",")[2], str(message).split(",")[3] + "℃",
                                             str(message).split(",")[4], str(message).split(",")[5]))
            self.cap_park_cb['values'] = self.get_car_park_ids()
            return

    def get_car_park_ids(self):
        car_park_id_list = list()
        for line in self.tv_car_parks.get_children():
            car_park_id_list.append(self.tv_car_parks.item(line)['values'][0])
        return car_park_id_list


def main():
    displayer = tk.Tk()
    Car(displayer, 'JYQ-4567', car_model='COUPE')
    displayer.mainloop()


if __name__ == '__main__':
    main()
