import csv

class Csv_reader:

    def read(self, file) -> list : 
        with open(file, "r") as file:
            csv_reader = csv.reader(file)
            return [x for x in csv_reader]


