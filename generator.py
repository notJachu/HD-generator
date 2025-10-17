from faker import Faker

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
            f.write("client_id,name,email\n")
            for client_id in range(1, self.clientNum + 1):
                name = self.faker.name()
                email = self.faker.email()
                f.write(f"{client_id},{name},{email}\n")
        print("Client generation completed.")