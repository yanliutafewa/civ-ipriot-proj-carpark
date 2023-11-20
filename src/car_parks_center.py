import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt
from car_park import CarParkInfo


class CarParksCenter:

    car_park_list = list()

    def __init__(self, displayer):

        displayer.geometry('1200x400')
        displayer.title("Moondalup CarPark Management Center")

        l_title = tk.Label(displayer, text='Moondalup CarPark Management Center Monitor',
                           font=('Arial', 28))
        l_title.pack()

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Calibri', 14,'bold'))
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
        self.tv_car_parks.pack(expand=True, fill=tk.BOTH)
        self.tv_car_parks['show'] = 'headings'

        # Populate the table
        # populate_table(self.tv_car_parks)

        # Initialize MQTT subscriber
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        # Connect to MQTT broker
        self.client.connect("127.0.0.1", 1883, 600)
        # Start MQTT loop in a non-blocking way
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribe to two topics
        client.subscribe("CarAct")
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
                    return
                # if not existed in treeview tv_car_parks, insert
            self.tv_car_parks.insert("", "end",
                                     values=(str(message).split(",")[0], str(message).split(",")[1],
                                             str(message).split(",")[2], str(message).split(",")[3] + "℃",
                                             str(message).split(",")[4], str(message).split(",")[5]))
            return

        for line in self.tv_car_parks.get_children():
            if self.tv_car_parks.item(line)['values'][0] == int(car_park_id):
                if topic == 'CarAct':
                    # get action 'in/out' from message
                    act = str(message).split(",")[1]
                    # get parking_bays and occupied from tree item.
                    parking_bays = self.tv_car_parks.item(line)['values'][4]
                    occupied = self.tv_car_parks.item(line)['values'][5]
                    if act == 'in' and occupied < parking_bays:
                        self.tv_car_parks.item(line, values=(self.tv_car_parks.item(line)['values'][0],
                                               self.tv_car_parks.item(line)['values'][1],
                                               self.tv_car_parks.item(line)['values'][2],
                                               self.tv_car_parks.item(line)['values'][3] + "℃",
                                               parking_bays,
                                               occupied+1))
                    if act == 'out' and occupied > 0:
                        self.tv_car_parks.item(line, values=(self.tv_car_parks.item(line)['values'][0],
                                               self.tv_car_parks.item(line)['values'][1],
                                               self.tv_car_parks.item(line)['values'][2],
                                               self.tv_car_parks.item(line)['values'][3] + "℃",
                                               parking_bays,
                                               occupied-1))

                if topic == 'UpdateTemperature':
                    # get new temperature from message
                    new_temperature = str(message).split(",")[1]
                    self.tv_car_parks.item(line, values=(self.tv_car_parks.item(line)['values'][0],
                                                         self.tv_car_parks.item(line)['values'][1],
                                                         self.tv_car_parks.item(line)['values'][2],
                                                         new_temperature + "℃",
                                                         self.tv_car_parks.item(line)['values'][4],
                                                         self.tv_car_parks.item(line)['values'][5]))


def populate_table(tree):
    # Inserting data into the table
    data = list()
    car_park_1 = CarParkInfo("1", "Wilson Parking",
                             "102 Wilson Street", 25,
                             20, 10)
    car_park_2 = CarParkInfo("2", "QV1 Car Park",
                             "51 Murry Street", 20,
                             28, 2)
    car_park_3 = CarParkInfo("3", "CPP Car Park",
                             "87-89 Pier Str", 21,
                             35, 30)
    data.append(car_park_1)
    data.append(car_park_2)
    data.append(car_park_3)
    for record in data:
        tree.insert("", "end", values=(record.car_park_id, record.car_park_name,
                                       record.car_park_address, record.temperature,
                                       record.parking_bays, record.occupied))


def main():
    displayer = tk.Tk()
    CarParksCenter(displayer)
    displayer.mainloop()


if __name__ == "__main__":
    main()
