from faker import Faker
import uuid

class DataGenerator:
    def __init__(self, clientNum : int, bikeNum : int, transactionNum : int):
        self.clientNum = clientNum
        self.bikeNum = bikeNum
        self.transactionNum = transactionNum
        self.faker = Faker('en_US')
        self.clientOutput = "clients.csv"
        self.bikeOutput = "bikes.csv"
        self.transactionOutput = "transactions.csv"

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