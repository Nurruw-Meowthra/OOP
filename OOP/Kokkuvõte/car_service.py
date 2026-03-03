"""Car service."""


class Car:
    """Represent car model."""

    def __init__(self, color: str, make: str, engine_size: int):
        """
        Car class constructor.

        :param color: car color
        :param make: car make
        :param engine_size: car engine size
        """
        self.color = color
        self.make = make
        self.engine_size = engine_size


class Service:
    """Represent car service model."""

    def __init__(self, name: str, max_car_num: int):
        """
        Service class constructor.

        Car service should also have a database to keep and track all cars standing in queue for repair.
        :param name: service name
        :param max_car_num: max car number service can take for repair at one time
        """
        self.name = name
        self.max_car_num = max_car_num
        self.cars_in_service = []

    def can_add_to_service_queue(self, car: Car) -> bool:
        """
        Check if it possible to add car to service queue.

        Car can be added if:
        1. after adding new car, total car number in service does not exceed max_car_number (allowed car number in service)
        2. there is no car with the same color and make present in this service (yes, this world works this way).

        If car can be added, return True. Otherwise return False.
        """
        if len(self.cars_in_service) >= self.max_car_num:
            return False
        for c in self.cars_in_service:
            if c.color == car.color and c.make == car.make:
                return False
        return True

    def add_car_to_service_queue(self, car: Car):
        """
        Add car to service if it is possible.

        The function does not return anything.
        """
        if self.can_add_to_service_queue(car):
            self.cars_in_service.append(car)

    def get_service_cars(self) -> list:
        """Get all cars in service."""
        return self.cars_in_service

    def repair(self) -> Car:
        """
        Repair car in service queue.

        Normally, the first car in queue is repaired.
        However, if there is a car in queue which color + make characters length is exactly 13 ->
        this car is chosen and is repaired (might be multiple suitable cars -> choose any).
        After the repair, car is no longer in queue (is removed).
        :return: chosen and repaired car
        """
        if not self.cars_in_service:
            return None
        for car in self.cars_in_service:
            if len(car.color + car.make) == 13:
                self.cars_in_service.remove(car)
                return car
        return self.cars_in_service.pop(0)

    def get_the_car_with_the_biggest_engine(self) -> list:
        """
        Return a list of cars (car) with the biggest engine size.

        :return: car (cars) with the biggest engine size
        """
        if not self.cars_in_service:
            return []
        max_engine_size = max(car.engine_size for car in self.cars_in_service)
        return [car for car in self.cars_in_service if car.engine_size == max_engine_size]