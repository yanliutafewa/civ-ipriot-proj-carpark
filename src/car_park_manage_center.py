from car_park import CarPark
import tkinter as tk


class CarParkManageCenter:

    def __init__(self):
        car_park_1 = CarPark("1", "Wilson Parking", "102 Wilson Street", 25, 20, 10)
        car_park_2 = CarPark("2", "QV1 Car Park", "51 Murry Street", 20, 28, 2)
        car_park_3 = CarPark("3", "CPP Car Park", "87-89 Pier Str", 21, 35, 30)

        displayer = tk.Tk()
        displayer.geometry('1200x400')
        displayer.title("Moondalup CarPark Management Center")

        l_title = tk.Label(displayer, text='Moondalup CarPark Management Center Monitor',font=('Arial', 28))
        l_title.grid(row=0, column=0, columnspan=6, pady=(20,5))

        # set for car_park_1
        # set Properties' name
        l_11 = tk.Label(displayer, text="car_park_id :", font=('Arial', 14))
        l_12 = tk.Label(displayer, text="car_park_name :", font=('Arial', 14))
        l_13 = tk.Label(displayer, text="car_park_address :", font=('Arial', 14))
        l_14 = tk.Label(displayer, text="temperature :", font=('Arial', 14))
        l_15 = tk.Label(displayer, text="parking_bays :", font=('Arial', 14))
        l_16 = tk.Label(displayer, text="occupied :", font=('Arial', 14))

        l_11.grid(row=1, column=0, sticky="W", pady=(20,5), padx=(50, 5))
        l_12.grid(row=2, column=0, sticky="W", pady=5, padx=(50, 5))
        l_13.grid(row=3, column=0, sticky="W", pady=5, padx=(50, 5))
        l_14.grid(row=4, column=0, sticky="W", pady=5, padx=(50, 5))
        l_15.grid(row=5, column=0, sticky="W", pady=5, padx=(50, 5))
        l_16.grid(row=6, column=0, sticky="W", pady=5, padx=(50, 5))

        # set values
        l_21 = tk.Label(displayer, text=f"{car_park_1.car_park_id}", font=('Arial', 14))
        l_22 = tk.Label(displayer, text=f"{car_park_1.car_park_name}", font=('Arial', 14))
        l_23 = tk.Label(displayer, text=f"{car_park_1.car_park_address}", font=('Arial', 14))
        l_24 = tk.Label(displayer, text=f"{car_park_1.temperature}℃", font=('Arial', 14))
        l_25 = tk.Label(displayer, text=f"{car_park_1.parking_bays}", font=('Arial', 14))
        l_26 = tk.Label(displayer, text=f"{car_park_1.occupied}", font=('Arial', 14))

        # this will arrange entry widgets
        l_21.grid(row=1, column=1, sticky="W", pady=(20,5))
        l_22.grid(row=2, column=1, sticky="W", pady=5)
        l_23.grid(row=3, column=1, sticky="W", pady=5)
        l_24.grid(row=4, column=1, sticky="W", pady=5)
        l_25.grid(row=5, column=1, sticky="W", pady=5)
        l_26.grid(row=6, column=1, sticky="W", pady=5)

        # set for car_park_2
        # set Properties' name
        l_31 = tk.Label(displayer, text="car_park_id :", font=('Arial', 14))
        l_32 = tk.Label(displayer, text="car_park_name :", font=('Arial', 14))
        l_33 = tk.Label(displayer, text="car_park_address :", font=('Arial', 14))
        l_34 = tk.Label(displayer, text="temperature :", font=('Arial', 14))
        l_35 = tk.Label(displayer, text="parking_bays :", font=('Arial', 14))
        l_36 = tk.Label(displayer, text="occupied :", font=('Arial', 14))

        l_31.grid(row=1, column=2, sticky="W", pady=(20,5), padx=(60, 5))
        l_32.grid(row=2, column=2, sticky="W", pady=5, padx=(60, 5))
        l_33.grid(row=3, column=2, sticky="W", pady=5, padx=(60, 5))
        l_34.grid(row=4, column=2, sticky="W", pady=5, padx=(60, 5))
        l_35.grid(row=5, column=2, sticky="W", pady=5, padx=(60, 5))
        l_36.grid(row=6, column=2, sticky="W", pady=5, padx=(60, 5))

        # set values
        l_41 = tk.Label(displayer, text=f"{car_park_2.car_park_id}", font=('Arial', 14))
        l_42 = tk.Label(displayer, text=f"{car_park_2.car_park_name}", font=('Arial', 14))
        l_43 = tk.Label(displayer, text=f"{car_park_2.car_park_address}", font=('Arial', 14))
        l_44 = tk.Label(displayer, text=f"{car_park_2.temperature}℃", font=('Arial', 14))
        l_45 = tk.Label(displayer, text=f"{car_park_2.parking_bays}", font=('Arial', 14))
        l_46 = tk.Label(displayer, text=f"{car_park_2.occupied}", font=('Arial', 14))

        # this will arrange entry widgets
        l_41.grid(row=1, column=3, sticky="W", pady=(20,5))
        l_42.grid(row=2, column=3, sticky="W", pady=5)
        l_43.grid(row=3, column=3, sticky="W", pady=5)
        l_44.grid(row=4, column=3, sticky="W", pady=5)
        l_45.grid(row=5, column=3, sticky="W", pady=5)
        l_46.grid(row=6, column=3, sticky="W", pady=5)

        # set for car_park_3
        # set Properties' name
        l_51 = tk.Label(displayer, text="car_park_id :", font=('Arial', 14))
        l_52 = tk.Label(displayer, text="car_park_name :", font=('Arial', 14))
        l_53 = tk.Label(displayer, text="car_park_address :", font=('Arial', 14))
        l_54 = tk.Label(displayer, text="temperature :", font=('Arial', 14))
        l_55 = tk.Label(displayer, text="parking_bays :", font=('Arial', 14))
        l_56 = tk.Label(displayer, text="occupied :", font=('Arial', 14))

        l_51.grid(row=1, column=4, sticky="W", pady=(20,5), padx=(60, 5))
        l_52.grid(row=2, column=4, sticky="W", pady=5, padx=(60, 5))
        l_53.grid(row=3, column=4, sticky="W", pady=5, padx=(60, 5))
        l_54.grid(row=4, column=4, sticky="W", pady=5, padx=(60, 5))
        l_55.grid(row=5, column=4, sticky="W", pady=5, padx=(60, 5))
        l_56.grid(row=6, column=4, sticky="W", pady=5, padx=(60, 5))

        # set values
        l_61 = tk.Label(displayer, text=f"{car_park_3.car_park_id}", font=('Arial', 14))
        l_62 = tk.Label(displayer, text=f"{car_park_3.car_park_name}", font=('Arial', 14))
        l_63 = tk.Label(displayer, text=f"{car_park_3.car_park_address}", font=('Arial', 14))
        l_64 = tk.Label(displayer, text=f"{car_park_3.temperature}℃", font=('Arial', 14))
        l_65 = tk.Label(displayer, text=f"{car_park_3.parking_bays}", font=('Arial', 14))
        l_66 = tk.Label(displayer, text=f"{car_park_3.occupied}", font=('Arial', 14))

        # this will arrange entry widgets
        l_61.grid(row=1, column=5, sticky="W", pady=(20,5))
        l_62.grid(row=2, column=5, sticky="W", pady=5)
        l_63.grid(row=3, column=5, sticky="W", pady=5)
        l_64.grid(row=4, column=5, sticky="W", pady=5)
        l_65.grid(row=5, column=5, sticky="W", pady=5)
        l_66.grid(row=6, column=5, sticky="W", pady=5)

        displayer.mainloop()




if __name__ == '__main__':

    CarParkManageCenter()