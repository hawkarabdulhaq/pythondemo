import csv
import os

def fetch_translations():
    translations = {}
    csv_file_path = os.path.join('translations', 'csv', 'about_translation.csv')

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                key = row['Key'].strip()
                en_value = row['EN'].strip()
                ku_value = row['KU'].strip()
                translations[key] = {
                    'EN': en_value,
                    'KU': ku_value,
                }
        return translations
    except Exception as e:
        print(f"Error reading translations from CSV: {e}")
        return {}

# Fetch translations and assign to the variable without changing its name
about_translations = fetch_translations()
