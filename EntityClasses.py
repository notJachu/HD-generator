import uuid
import random

class Bike:
    def __init__(self, bike_id, seat_num, is_functional, hourly_rate):
        self.bike_id = bike_id
        self.seat_num = seat_num
        self.is_functional = is_functional
        self.hourly_rate = hourly_rate

    @classmethod
    def random_bike(cls, seat_num = 2):
        bike_id = str(uuid.uuid4())
        is_functional = random.choice([True, True, True, False])
        hourly_rate = round(random.uniform(5.0, 20.0), 2)
        return cls(bike_id, seat_num, is_functional, hourly_rate)

class MultiPersonBike(Bike):
    def __init__(self, bike_id, seat_config, is_functional, hourly_rate, has_stash, has_roof, rowing_seats_num):
        super().__init__(bike_id, seat_config.count('+') + 1, is_functional, hourly_rate)
        self.seat_config = seat_config
        self.has_stash = has_stash
        self.has_roof = has_roof
        self.rowing_seats_num = rowing_seats_num

    @classmethod
    def random_multi_person_bike(cls):
        bike_id = str(uuid.uuid4())
        seats_num = random.randint(3, 6)
        seat_config = ''
        rowing_seats_num = seats_num - 1
        # TODO: implement seat configuration generation
        # for i in range(seats_num):
        #     if random.choice([True, False]):
        #         seat_config += 'o'
        #     else:
        #         seat_config += '+'
        #         rowing_seats_num += 1
        is_functional = random.choice([True, True, True, False])
        hourly_rate = round(random.uniform(10.0, 30.0), 2)
        has_stash = random.choice([True, False])
        has_roof = random.choice([True, False])
        return cls(bike_id, seat_config, is_functional, hourly_rate, has_stash, has_roof, rowing_seats_num)