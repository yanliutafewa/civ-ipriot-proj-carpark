import json


class ConfigParser:
    def __init__(self, config_file_path):
        self.file_path = config_file_path
        self.config_data = None

        try:
            with open(self.file_path, 'r') as file:
                self.config_data = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in '{self.file_path}': {e}")

    def get_config_data(self):
        return self.config_data

    def get_car_parks_center_name(self):
        center_name = None
        if self.config_data:
            center_name = self.config_data["CarParksCenter"][0]['name']
        return center_name
