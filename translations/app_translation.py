import csv
import os

def fetch_translations(module_key_prefix):
    """
    Fetch translations for a specific module key prefix from the master CSV file.

    :param module_key_prefix: Prefix of keys for the desired module, e.g., "app_".
    :return: Dictionary containing translations for the specified module.
    """
    translations = {}
    csv_file_path = os.path.join('translations', 'csv', 'master_translation.csv')

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                key = row['Key'].strip()
                if key.startswith(module_key_prefix):  # Filter keys by the prefix
                    en_value = row['EN'].strip()
                    ku_value = row['KU'].strip()
                    translations[key] = {
                        'EN': en_value,
                        'KU': ku_value,
                    }
        return translations
    except Exception as e:
        print(f"Error reading translations from master CSV: {e}")
        return {}

# Fetch translations specific to the "app" module and assign to the variable
app_translations = fetch_translations("app_")
