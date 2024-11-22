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

# Centralized translate function
def translate(key, language):
    """Retrieve a translated string for the given key and language."""
    return translations.get(key, {}).get(language, key)
