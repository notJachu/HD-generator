from faker import Faker
import random
import uuid

class DataGenerator:
    def __init__(self, clientNum : int = 10, bikeNum : int = 10, transactionNum : int = 10, employeeNum : int = 10):
        self.clientNum = clientNum
        self.bikeNum = bikeNum
        self.transactionNum = transactionNum
        self.employeeNum = employeeNum
        self.faker = Faker('en_US')
        self.clientOutput = "clients.csv"
        self.bikeOutput = "bikes.csv"
        self.transactionOutput = "transactions.csv"
        self.employeeOutput = "employees.csv"

    def generate_clients(self):
        print(f"Generating {self.clientNum} clients to {self.clientOutput}")
        with open(self.clientOutput, 'w') as f:
            f.write("client_id,first_name,last_name,email_address,phone_number\n")
            for _ in range(1, self.clientNum + 1):
                client_id = str(uuid.uuid4())
                first_name = self.faker.first_name()
                last_name = self.faker.last_name()
                phone_number = self.faker.phone_number()
                email_address = f"{first_name.lower()}.{last_name.lower()}@example.com"
                f.write(f"{client_id},{first_name},{last_name},{email_address},{phone_number}\n")

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

        print("Employee generation completed.")


    def generate_bikes(self, premium_num : int = 10, two_person_num : int = 10, multi_person_num : int = 10):
        print(f"Generating {self.bikeNum} base bikes to {self.bikeOutput}")
        with open(self.bikeOutput, 'w') as f:
            f.write("bike_id,seats_num,is_functional,hourly_rate\n")
            for _ in range(1, self.bikeNum + 1):
                bike_id = str(uuid.uuid4())
                seats_num = 1
                is_functional = random.choice([True, True, True, False])  # 75% chance to be functional
                hourly_rate = round(random.uniform(5.0, 15.0), 2)
                f.write(f"{bike_id},{seats_num},{is_functional},{hourly_rate}\n")
        print("Base bike generation completed.")