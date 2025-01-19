import csv
import os

def fetch_trainings():
    """
    Fetch training details from a CSV file and return a dictionary with translations.
    """
    trainings = {}
    csv_file_path = os.path.join('translations', 'csv', 'trainings.csv')

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                key = row['Key'].strip()
                en_value = row['EN'].strip()
                ku_value = row['KU'].strip()
                trainings[key] = {
                    'EN': en_value,
                    'KU': ku_value,
                }
        return trainings
    except Exception as e:
        print(f"Error reading trainings from CSV: {e}")
        return {}

# Fetch trainings from the CSV
trainings_translations = fetch_trainings()  # Renamed to match the expected import name
