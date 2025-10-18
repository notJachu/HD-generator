from generator import DataGenerator

def main():

    generator = DataGenerator(clientNum=10, bikeNum=50, transactionNum=200)
    generator.generate_clients()
    generator.generate_employees()
    generator.generate_bikes(generate_types=True)

if __name__ == "__main__":
    main()