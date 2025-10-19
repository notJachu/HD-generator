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
    def __init__(self, bike_id, seat_config, is_functional, hourly_rate, has_stash, has_roof, rowing_seats_num, seat_num):
        super().__init__(bike_id, seat_num, is_functional, hourly_rate)
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
        return cls(bike_id, seat_config, is_functional, hourly_rate, has_stash, has_roof, rowing_seats_num, seats_num)

class PremiumBike(Bike):
    def __init__(self, bike_id, has_assist, has_audio, has_lights, battery_life, seat_num, is_functional, hourly_rate):
        super().__init__(bike_id, seat_num, is_functional, hourly_rate)
        self.has_assist = has_assist
        self.has_audio = has_audio
        self.has_lights = has_lights
        self.battery_life = battery_life

    @classmethod
    def random_premium_bike(cls):
        bike_id = str(uuid.uuid4())
        seat_num = 1
        is_functional = random.choice([True, True, True, False])
        hourly_rate = round(random.uniform(15.0, 40.0), 2)
        has_assist = random.choice([True, False])
        has_audio = random.choice([True, False])
        has_lights = random.choice([True, False])
        battery_life = random.randint(2, 8)  # in hours
        return cls(bike_id, has_assist, has_audio, has_lights, battery_life, seat_num, is_functional, hourly_rate)

class TwoPersonBike(Bike):
    def __init__(self, bike_id, is_functional, hourly_rate, pedal_type, seat_num=2):
        super().__init__(bike_id, seat_num, is_functional, hourly_rate)
        self.pedal_type = pedal_type

    @classmethod
    def random_two_person_bike(cls):
        bike_id = str(uuid.uuid4())
        is_functional = random.choice([True, True, True, False])
        hourly_rate = round(random.uniform(7.0, 25.0), 2)
        pedal_type = random.choice(['standard', 'fancy', 'small'])
        return cls(bike_id, is_functional, hourly_rate, pedal_type)