

class Bike:
    def __init__(self, bike_id, seat_num, is_functional, hourly_rate):
        self.bike_id = bike_id
        self.seat_num = seat_num
        self.is_functional = is_functional
        self.hourly_rate = hourly_rate


class MultiPersonBike(Bike):
    def __init__(self, bike_id, seat_config, is_functional, hourly_rate, has_stash, has_roof, rowing_seats_num):
        super().__init__(bike_id, seat_config.count('+') + 1, is_functional, hourly_rate)
        self.seat_config = seat_config
        self.has_stash = has_stash
        self.has_roof = has_roof
        self.rowing_seats_num = rowing_seats_num

