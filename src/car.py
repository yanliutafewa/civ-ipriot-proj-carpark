import tkinter as tk
from car_park import CarPark
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
import datetime
from publisher import Publisher


class Car:

    DISPLAY_INIT = '– – –'

    def __init__(self, license_plate, car_model, entry_time, exit_time):
        self.publisher = Publisher("CarAct")
        self.license_plate = license_plate
        self.car_model = car_model
        self.entry_time = entry_time

        car_park_1 = CarPark("1", "Wilson Parking", "102 Wilson Street",
                             self.DISPLAY_INIT, self.DISPLAY_INIT, self.DISPLAY_INIT)
        car_park_2 = CarPark("2", "QV1 Car Park", "51 Murry Street",
                             self.DISPLAY_INIT, self.DISPLAY_INIT, self.DISPLAY_INIT)
        car_park_3 = CarPark("3", "CPP Car Park", "87-89 Pier Str",
                             self.DISPLAY_INIT, self.DISPLAY_INIT, self.DISPLAY_INIT)

        displayer = tk.Tk()
        displayer.geometry('1200x550')
        displayer.title(f"Car: {self.license_plate}")

        l_title = tk.Label(displayer, text='CAR🚘',font=('Arial', 28))
        l_title.grid(row=0, column=0, columnspan=6, pady=(20,5))

        l_plate = tk.Label(displayer, text="license_plate :", font=('Arial', 18))
        l_plate_value = tk.Label(displayer, text=f"{self.license_plate}", font=('Arial', 18))
        l_model = tk.Label(displayer, text="car_model :", font=('Arial', 18))
        l_model_value = tk.Label(displayer, text=f"{self.car_model}", font=('Arial', 18))
        l_plate.grid(row=1, column=0, sticky="W", pady=(20,5), padx=(50, 5))
        l_plate_value.grid(row=1, column=1, sticky="W", pady=(20,5), padx=(50, 5))
        l_model.grid(row=1, column=2, sticky="W", pady=(20,5), padx=(50, 5))
        l_model_value.grid(row=1, column=3, sticky="W", pady=(20,5), padx=(50, 5))

        l_entry_time = tk.Label(displayer, text="entry_time :", font=('Arial', 18))
        l_entry_time_value = tk.Label(displayer, text=f"{self.entry_time}", font=('Arial', 18))
        l_entry_time.grid(row=2, column=0, sticky="W", pady=(20,5), padx=(50, 5))
        l_entry_time_value.grid(row=2, column=1, sticky="W", pady=(20,5), padx=(50, 5))

        l_car_park = tk.Label(displayer, text="Car Park :", font=('Arial', 18))
        l_car_park.grid(row=3, column=0, sticky="W", pady=(20,5), padx=(50, 5))
###########
        # create a combobox #####
        selected_number = tk.StringVar()
        cap_park_cb = ttk.Combobox(displayer, textvariable=selected_number)
        cap_park_cb.grid(row=3, column=1, sticky="W", pady=(20, 5), padx=(50, 5))

        # get first 3 letters of every month name
        cap_park_cb['values'] = [1,2,3]

        # prevent typing a value
        cap_park_cb['state'] = 'readonly'

        # bind the selected value changes
        def car_park_changed(event):

            showinfo(
                title='Result',
                message=f'You selected {selected_number.get()}!'
            )

        cap_park_cb.bind('<<ComboboxSelected>>', car_park_changed)
###########

########
        def entry_car_park():
            l_entry_time_value.config(text=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            self.publisher.publish_msg(f"in,{selected_number.get()}")
            msg = messagebox.showinfo("Message", selected_number.get())

        b_entry = tk.Button(displayer, text="Entry", command=entry_car_park)
        b_entry.grid(row=3, column=2, sticky="W", pady=(20, 5), padx=(50, 5))

        def exit_car_park():
            l_entry_time_value.config(text='')

        b_exit = tk.Button(displayer, text="Exit", command=exit_car_park)
        b_exit.grid(row=3, column=3, sticky="W", pady=(20, 5), padx=(50, 5))

########


        # set for car_park_1
        # set Properties' name
        l_11 = tk.Label(displayer, text="car_park_id :", font=('Arial', 14))
        l_12 = tk.Label(displayer, text="car_park_name :", font=('Arial', 14))
        l_13 = tk.Label(displayer, text="car_park_address :", font=('Arial', 14))
        l_14 = tk.Label(displayer, text="temperature :", font=('Arial', 14))
        l_15 = tk.Label(displayer, text="parking_bays :", font=('Arial', 14))
        l_16 = tk.Label(displayer, text="occupied :", font=('Arial', 14))

        l_11.grid(row=4, column=0, sticky="W", pady=(20,5), padx=(50, 5))
        l_12.grid(row=5, column=0, sticky="W", pady=5, padx=(50, 5))
        l_13.grid(row=6, column=0, sticky="W", pady=5, padx=(50, 5))
        l_14.grid(row=7, column=0, sticky="W", pady=5, padx=(50, 5))
        l_15.grid(row=8, column=0, sticky="W", pady=5, padx=(50, 5))
        l_16.grid(row=9, column=0, sticky="W", pady=5, padx=(50, 5))

        # set values
        l_21 = tk.Label(displayer, text=f"{car_park_1.car_park_id}", font=('Arial', 14))
        l_22 = tk.Label(displayer, text=f"{car_park_1.car_park_name}", font=('Arial', 14))
        l_23 = tk.Label(displayer, text=f"{car_park_1.car_park_address}", font=('Arial', 14))
        l_24 = tk.Label(displayer, text=f"{car_park_1.temperature}℃", font=('Arial', 14))
        l_25 = tk.Label(displayer, text=f"{car_park_1.parking_bays}", font=('Arial', 14))
        l_26 = tk.Label(displayer, text=f"{car_park_1.occupied}", font=('Arial', 14))

        # this will arrange entry widgets
        l_21.grid(row=4, column=1, sticky="W", pady=(20,5))
        l_22.grid(row=5, column=1, sticky="W", pady=5)
        l_23.grid(row=6, column=1, sticky="W", pady=5)
        l_24.grid(row=7, column=1, sticky="W", pady=5)
        l_25.grid(row=8, column=1, sticky="W", pady=5)
        l_26.grid(row=9, column=1, sticky="W", pady=5)

        # set for car_park_2
        # set Properties' name
        l_31 = tk.Label(displayer, text="car_park_id :", font=('Arial', 14))
        l_32 = tk.Label(displayer, text="car_park_name :", font=('Arial', 14))
        l_33 = tk.Label(displayer, text="car_park_address :", font=('Arial', 14))
        l_34 = tk.Label(displayer, text="temperature :", font=('Arial', 14))
        l_35 = tk.Label(displayer, text="parking_bays :", font=('Arial', 14))
        l_36 = tk.Label(displayer, text="occupied :", font=('Arial', 14))

        l_31.grid(row=4, column=2, sticky="W", pady=(20,5), padx=(60, 5))
        l_32.grid(row=5, column=2, sticky="W", pady=5, padx=(60, 5))
        l_33.grid(row=6, column=2, sticky="W", pady=5, padx=(60, 5))
        l_34.grid(row=7, column=2, sticky="W", pady=5, padx=(60, 5))
        l_35.grid(row=8, column=2, sticky="W", pady=5, padx=(60, 5))
        l_36.grid(row=9, column=2, sticky="W", pady=5, padx=(60, 5))

        # set values
        l_41 = tk.Label(displayer, text=f"{car_park_2.car_park_id}", font=('Arial', 14))
        l_42 = tk.Label(displayer, text=f"{car_park_2.car_park_name}", font=('Arial', 14))
        l_43 = tk.Label(displayer, text=f"{car_park_2.car_park_address}", font=('Arial', 14))
        l_44 = tk.Label(displayer, text=f"{car_park_2.temperature}℃", font=('Arial', 14))
        l_45 = tk.Label(displayer, text=f"{car_park_2.parking_bays}", font=('Arial', 14))
        l_46 = tk.Label(displayer, text=f"{car_park_2.occupied}", font=('Arial', 14))

        # this will arrange entry widgets
        l_41.grid(row=4, column=3, sticky="W", pady=(20,5))
        l_42.grid(row=5, column=3, sticky="W", pady=5)
        l_43.grid(row=6, column=3, sticky="W", pady=5)
        l_44.grid(row=7, column=3, sticky="W", pady=5)
        l_45.grid(row=8, column=3, sticky="W", pady=5)
        l_46.grid(row=9, column=3, sticky="W", pady=5)

        # set for car_park_3
        # set Properties' name
        l_51 = tk.Label(displayer, text="car_park_id :", font=('Arial', 14))
        l_52 = tk.Label(displayer, text="car_park_name :", font=('Arial', 14))
        l_53 = tk.Label(displayer, text="car_park_address :", font=('Arial', 14))
        l_54 = tk.Label(displayer, text="temperature :", font=('Arial', 14))
        l_55 = tk.Label(displayer, text="parking_bays :", font=('Arial', 14))
        l_56 = tk.Label(displayer, text="occupied :", font=('Arial', 14))

        l_51.grid(row=4, column=4, sticky="W", pady=(20,5), padx=(60, 5))
        l_52.grid(row=5, column=4, sticky="W", pady=5, padx=(60, 5))
        l_53.grid(row=6, column=4, sticky="W", pady=5, padx=(60, 5))
        l_54.grid(row=7, column=4, sticky="W", pady=5, padx=(60, 5))
        l_55.grid(row=8, column=4, sticky="W", pady=5, padx=(60, 5))
        l_56.grid(row=9, column=4, sticky="W", pady=5, padx=(60, 5))

        # set values
        l_61 = tk.Label(displayer, text=f"{car_park_3.car_park_id}", font=('Arial', 14))
        l_62 = tk.Label(displayer, text=f"{car_park_3.car_park_name}", font=('Arial', 14))
        l_63 = tk.Label(displayer, text=f"{car_park_3.car_park_address}", font=('Arial', 14))
        l_64 = tk.Label(displayer, text=f"{car_park_3.temperature}℃", font=('Arial', 14))
        l_65 = tk.Label(displayer, text=f"{car_park_3.parking_bays}", font=('Arial', 14))
        l_66 = tk.Label(displayer, text=f"{car_park_3.occupied}", font=('Arial', 14))

        # this will arrange entry widgets
        l_61.grid(row=4, column=5, sticky="W", pady=(20,5))
        l_62.grid(row=5, column=5, sticky="W", pady=5)
        l_63.grid(row=6, column=5, sticky="W", pady=5)
        l_64.grid(row=7, column=5, sticky="W", pady=5)
        l_65.grid(row=8, column=5, sticky="W", pady=5)
        l_66.grid(row=9, column=5, sticky="W", pady=5)

        displayer.mainloop()



if __name__ == '__main__':

    Car('JYQ-4567',car_model='COUPE', entry_time='', exit_time='')