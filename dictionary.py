# dictionary.py

# Import translations from various modules
from translations.app_translation import app_translations
from translations.home_translation import home_translations
from translations.fit_translation import fit_translations
from translations.learning_platform_translation import learning_platform_translations
from translations.enrollment_translation import enrollment_translations
from translations.price_translation import price_translations  # Import price translations

# Combine all translations into a single dictionary
translations = {
    **app_translations,
    **home_translations,
    **fit_translations,
    **learning_platform_translations,
    **enrollment_translations,
    **price_translations,  # Include price translations
}

# Centralized translate function
def translate(key, language):
    """Retrieve a translated string for the given key and language."""
    return translations.get(key, {}).get(language, key)
