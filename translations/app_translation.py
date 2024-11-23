import csv
import os

def fetch_translations():
    """
    Fetch translations specific to app keys from the master_translation.csv file.
    """
    translations = {}
    csv_file_path = os.path.join('translations', 'csv', 'master_translation.csv')

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                key = row['Key'].strip()  # Use exact key from CSV without prefixing
                en_value = row['EN'].strip()
                ku_value = row['KU'].strip()
                translations[key] = {
                    'EN': en_value,
                    'KU': ku_value,
                }
            print(f"Loaded Translations: {translations}")  # Debug loaded data
        return translations
    except Exception as e:
        print(f"Error reading translations from master CSV: {e}")
        return {}


# Fetch translations and assign to the variable without changing its name
app_translations = fetch_translations()
