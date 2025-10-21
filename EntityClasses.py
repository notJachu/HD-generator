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


class Transaction:
    def __init__(self, transaction_id, client_id, bike_id, employee_id, booking_id,
                 transaction_date, transaction_hour, planned_time, real_time, recipe_type, group_size):
        self.transaction_id = transaction_id
        self.client_id = client_id
        self.bike_id = bike_id
        self.employee_id = employee_id
        self.booking_id = booking_id
        self.transaction_date = transaction_date
        self.transaction_hour = transaction_hour
        self.planned_time = planned_time
        self.real_time = real_time
        self.recipe_type = recipe_type
        self.group_size = group_size

    @classmethod
    def random_transaction(cls, date, client_ids, bike_id, employee_ids, booking_id):
        transaction_id = str(uuid.uuid4())
        client_id = random.choice(client_ids)
        employee_id = random.choice(employee_ids)
        transaction_date = date
        if booking_id is None:
            booking_id = 0
        transaction_hour = random.randint(8, 20)  # Assuming transactions happen between 8 AM and 8 PM
        planned_time = random.randint(1, 8)  # Planned time between 1 to 8 hours
        real_time = planned_time + random.choice([-1, 0, 1])  # Real time can be planned time +/- 1 hour
        recipe_type = random.choice(['standard', 'premium', 'family'])

        # TODO: make group size make sense with bike type
        group_size = random.randint(1, 6)  # Group size between 1 to 6

        return cls(transaction_id, client_id, bike_id, employee_id, booking_id,
                   transaction_date, transaction_hour, planned_time, real_time, recipe_type, group_size)


class FaultReport:
    def __init__(self, bike_id, last_lease_date, report_date, client_contact, repair_cost, insurance_claimed, fault_description):
        self.bike_id = bike_id
        self.last_lease_date = last_lease_date
        self.report_date = report_date
        self.client_contact = client_contact
        self.repair_cost = repair_cost
        self.insurance_claimed = insurance_claimed
        self.fault_description = fault_description

    @classmethod
    def random_fault_report(cls, bike_id, last_lease_date, report_date, client_contact):
        repair_cost = round(random.uniform(20.0, 500.0), 2)
        insurance_claimed = round(random.uniform(0.0, repair_cost), 2)
        fault_description = "lorem ipsum dolor sit amet"
        return cls(bike_id, last_lease_date, report_date, client_contact, repair_cost, insurance_claimed, fault_description)