# dictionary.py

# Import translations from various modules
from translations.app_translation import app_translations
from translations.home_translation import home_translations

# Combine all translations into a single dictionary
translations = {
    **app_translations,
    **home_translations,
    # Add other translation modules here as needed
}
