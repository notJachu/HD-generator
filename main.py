from datetime import datetime

from generator import DataGenerator

def main():

    generator = DataGenerator(clientNum=10, bikeNum=50, transactionNum=200, save_ids=True)
    generator.generate_clients()
    generator.generate_employees()
    generator.generate_bikes(generate_types=True)
    generator.generate_transactions(date_start = datetime(2015,1, 1), date_end = datetime(2020,12,31))
    generator.generate_faults(faultNum=10)
    generator.generate_next_interval(date_start=(datetime(2021,1,1)), date_end=(datetime(2024,6,1)))
if __name__ == "__main__":
    main()