import csv

class CSVWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_csv(self, data):
        try:
            with open(self.file_path, mode='w', newline='') as file:
                csv_writer = csv.writer(file)
                for row in data:
                    csv_writer.writerow(row)
            print(f"Data has been written to '{self.file_path}'")
        except IOError as e:
            print(f"Error writing to '{self.file_path}': {e}")

    def append_to_csv(self, data):
        try:
            with open(self.file_path, mode='a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(data)
            print(f"Data has been appended to '{self.file_path}'")
        except IOError as e:
            print(f"Error appending to '{self.file_path}': {e}")
