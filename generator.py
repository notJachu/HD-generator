from os import supports_effective_ids
from traceback import print_tb

from faker import Faker
from EntityClasses import *
import random
import uuid

class DataGenerator:
    def __init__(self, clientNum : int = 10, bikeNum : int = 10, transactionNum : int = 10, employeeNum : int = 10, save_ids : bool = False):
        self.clientNum = clientNum
        self.bikeNum = bikeNum
        self.transactionNum = transactionNum
        self.employeeNum = employeeNum
        self.faker = Faker('en_US')
        self.clientOutput = "clients.csv"
        self.bikeOutput = "bikes.csv"
        self.transactionOutput = "transactions.csv"
        self.employeeOutput = "employees.csv"
        self.employee_id_list = []
        self.client_id_list = []
        self.bike_id_list = []
        self.save_ids = save_ids




    def generate_clients(self):
        print(f"Generating {self.clientNum} clients to {self.clientOutput}")
        if self.save_ids:
            print("Saving client IDs to client_id_list")
        with open(self.clientOutput, 'w') as f:
            f.write("client_id,first_name,last_name,email_address,phone_number\n")
            for _ in range(1, self.clientNum + 1):
                client_id = str(uuid.uuid4())
                first_name = self.faker.first_name()
                last_name = self.faker.last_name()
                phone_number = self.faker.phone_number()
                email_address = f"{first_name.lower()}.{last_name.lower()}@example.com"
                f.write(f"{client_id},{first_name},{last_name},{email_address},{phone_number}\n")
                if self.save_ids:
                    self.client_id_list.append(client_id)

        print("Client generation completed.")

    def __generate_PESEL(self, birth_date, is_male: bool):
        birth_year = birth_date.year  % 100
        birth_month = birth_date.month
        if birth_date.year >= 2000:
            birth_month += 20
        birth_day = birth_date.day

        random_id = random.randint(0, 999)
        if is_male:
            gender_digit = random.choice([1,3,5,7,9])
        else:
            gender_digit = random.choice([0,2,4,6,8])

        checksum = (birth_year // 10 * 1 + birth_year % 10 * 3 +
                    birth_month // 10 * 7 + birth_month % 10 * 9 +
                    birth_day // 10 * 1 + birth_day % 10 * 3 +
                    (random_id // 100) * 7 + (random_id // 10 % 10) * 9 +
                    (random_id % 10) * 1 + gender_digit * 3) % 10
        if checksum != 0:
            checksum = 10 - checksum

        pesel = f"{birth_year:02d}{birth_month:02d}{birth_day:02d}{random_id:03d}{gender_digit}{checksum}"
        return pesel


    def generate_employees(self):
        print(f"Generating {self.employeeNum} employees to {self.employeeOutput}")
        if self.save_ids:
            print("Saving employee IDs to employee_id_list")
        with open(self.employeeOutput, 'w') as f:
            f.write("empleyee_id,PESEL,enroll_date,birth_date,position,hour_wage\n")
            for _ in range(1, self.employeeNum + 1):
                employee_id = str(uuid.uuid4())
                is_male = random.choice([True, False])
                if is_male:
                    first_name = self.faker.first_name_male()
                    last_name = self.faker.last_name_male()
                else:
                    first_name = self.faker.first_name_female()
                    last_name = self.faker.last_name_female()

                birth_date = self.faker.date_of_birth(minimum_age=18, maximum_age=65)
                enroll_date = self.faker.date_between(start_date=birth_date.replace(year=birth_date.year + 18), end_date='today')
                position = random.choice(['Manager', 'Salesperson', 'Mechanic', 'Cashier'])
                hour_wage = round(random.uniform(15.0, 50.0), 2)
                pesel = self.__generate_PESEL(birth_date, is_male)
                f.write(f"{employee_id},{pesel},{enroll_date},{birth_date},{position},{hour_wage}\n")
                if self.save_ids:
                    self.employee_id_list.append(employee_id)

        print("Employee generation completed.")


    def generate_bikes(self, premium_num : int = 10, two_person_num : int = 10, multi_person_num : int = 10, generate_types: bool = False):

        print(f"Type generation is set to {generate_types}")
        if not generate_types:
            print(f"Generating {self.bikeNum} base bikes to {self.bikeOutput}")
        else:
            print(f"Generating {multi_person_num + premium_num + two_person_num} bikes")

        if self.save_ids:
            print("Saving bike IDs to bike_id_list")
        # Reset base bike file to enable appending types later
        f = open(self.bikeOutput, 'r+')
        f.truncate(0)
        f.close()

        # TODO: clean up commented code so it is executed when generate_types is False
        # Generate base bikes
        # if not generate_types:
        #     with open(self.bikeOutput, 'w') as f:
        #         f.write("bike_id,seats_num,is_functional,hourly_rate\n")
        #         for _ in range(1, self.bikeNum + 1):
        #             bike = Bike.random_bike()
        #             f.write(f"{bike.bike_id},{bike.seats_num},{bike.is_functional},{bike.hourly_rate}\n")
        #     print("Base bike generation completed.")

        # Generate bike types
        # else:

        # TODO: add variable for files not hardcode
        base_file = open(self.bikeOutput, 'a')
        multi_person_file = open('multi_person_bikes.csv', 'w')
        premium_bike_file = open('premium_bikes.csv', 'w')
        two_person_file = open('two_person_bikes.csv', 'w')

        # Headers
        base_file.write("bike_id,seats_num,is_functional,hourly_rate\n")
        multi_person_file.write("bike_id,seat_config,has_stash,has_roof,rowing_seats_num\n")
        premium_bike_file.write("bike_id,has_assist,has_audio,has_lights,battery_life\n")
        two_person_file.write("bike_id,pedal_type\n")

        print(f"Generating {multi_person_num} multi-person bikes to multi_person_bikes.csv and base bikes to {self.bikeOutput}")
        for _ in range(1, multi_person_num + 1):
            bike = MultiPersonBike.random_multi_person_bike()
            multi_person_file.write(f"{bike.bike_id},{bike.seat_config},{bike.has_stash},{bike.has_roof},{bike.rowing_seats_num}\n")
            base_file.write(f"{bike.bike_id},{bike.seat_num},{bike.is_functional},{bike.hourly_rate}\n")
            if self.save_ids:
                self.bike_id_list.append(bike.bike_id)

        print("Multi-person bike generation completed.")

        print(f"Generating {premium_num} premium bikes to premium_bikes.csv and base bikes to {self.bikeOutput}")
        for _ in range(1, premium_num + 1):
            bike = PremiumBike.random_premium_bike()
            premium_bike_file.write(f"{bike.bike_id},{bike.has_assist},{bike.has_audio},{bike.has_lights},{bike.battery_life}\n")
            base_file.write(f"{bike.bike_id},{bike.seat_num},{bike.is_functional},{bike.hourly_rate}\n")
            if self.save_ids:
                self.bike_id_list.append(bike.bike_id)

        print("Premium bike generation completed.")

        print(f"Generating {two_person_num} two-person bikes to two_person_bikes.csv and base bikes to {self.bikeOutput}")
        for _ in range(1, two_person_num + 1):
            bike = TwoPersonBike.random_two_person_bike()
            two_person_file.write(f"{bike.bike_id},{bike.pedal_type}\n")
            base_file.write(f"{bike.bike_id},{bike.seat_num},{bike.is_functional},{bike.hourly_rate}\n")
            if self.save_ids:
                self.bike_id_list.append(bike.bike_id)

        print("Two-person bike generation completed.")

        base_file.close()
        multi_person_file.close()
        premium_bike_file.close()
        two_person_file.close()

        print("Bike generation completed.")

    def generate_transactions(self, date_start, date_end):
        print(f"Generating {self.transactionNum} transactions to {self.transactionOutput}")
        if not self.client_id_list or not self.bike_id_list or not self.employee_id_list:
            print("Error: Client, Bike, and Employee ID lists must be populated to generate transactions.")
            return

        with open(self.transactionOutput, 'w') as f:
            f.write("transaction_id,client_id,bike_id,employee_id,booking_id,transaction_date,transaction_hour,planned_time,real_time,recipe_type,group_size\n")
            for _ in range(1, self.transactionNum + 1):
                date = self.faker.date_between(start_date=date_start, end_date=date_end)
                transaction = Transaction.random_transaction(date, self.client_id_list, self.bike_id_list, self.employee_id_list, None)
                f.write(f"{transaction.transaction_id},{transaction.client_id},{transaction.bike_id},"
                        f"{transaction.employee_id},{transaction.booking_id},{transaction.transaction_date},"
                        f"{transaction.transaction_hour},{transaction.planned_time},{transaction.real_time},{transaction.recipe_type},{transaction.group_size}\n")

        print("Transaction generation completed.")

