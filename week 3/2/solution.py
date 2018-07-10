import csv
import os


class BaseCar:
    """Base class for cars"""

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        (root, ext) = os.path.splitext(self.photo_file_name)
        return ext if ext != "" else root

    def __repr__(self):
        return self.__str__()


class Car(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    def __str__(self):
        return f"Car {self.brand} photo={self.photo_file_name} carrying={self.carrying} passenger_seats_count=" \
               f"{self.passenger_seats_count}"


class Truck(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, body_whl_str):
        super().__init__(brand, photo_file_name, carrying)
        body_whl = body_whl_str.split("x")
        if len(body_whl) < 3:
            body_whl = [0, 0, 0]

        for i in range(0, len(body_whl)):
            body_whl[i] = float(body_whl[i])

        self.body_width = float(body_whl[0])
        self.body_height = float(body_whl[1])
        self.body_length = float(body_whl[2])

    def get_body_value(self):
        return self.body_width * self.body_height * self.body_length

    def __str__(self):
        return f"Car {self.brand} photo={self.photo_file_name} carrying={self.carrying} body_value=" \
               f"{self.get_body_value()}"


class SpecMachine(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    def __str__(self):
        return f"Car {self.brand} photo={self.photo_file_name} carrying={self.carrying} extra={self.extra}"


def get_car_list(cars_strings):
    """
    Create list of cars
    :param cars_strings:
    :return:
    """

    car_list = []

    for car_str in cars_strings:
        brand = car_str["brand"]
        photo_file_name = car_str["photo_file_name"]
        carrying = car_str["carrying"]
        passenger_seats_count = car_str["passenger_seats_count"]
        body_whl = car_str["body_whl"]
        extra = car_str["extra"]
        car_type = car_str["car_type"]

        try:
            if car_type == "car":
                car = Car(brand, photo_file_name, carrying, passenger_seats_count)
            elif car_type == "truck":
                car = Truck(brand, photo_file_name, carrying, body_whl)
            elif car_type == "spec_machine":
                car = SpecMachine(brand, photo_file_name, carrying, extra)
            else:
                continue
        except ValueError:
            continue

        car_list.append(car)

    return car_list


def main():
    with open("3-2.csv", newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        cars = get_car_list(reader)
        print(cars)


if __name__ == "__main__":
    main()
