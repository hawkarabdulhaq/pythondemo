# dictionary.py

# Import translations from various modules
from dictionary.app_translation import app_translations

# Combine all translations into a single dictionary
translations = {
    **app_translations,
    # Add other translation modules here, e.g., home_translations, sidebar_translations
}
