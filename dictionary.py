# dictionary.py

import streamlit as st

# Import translations from various modules
from translations.app_translation import app_translations
from translations.home_translation import home_translations
from translations.fit_translation import fit_translations
from translations.learning_platform_translation import learning_platform_translations
from translations.enrollment_translation import enrollment_translations
from translations.price_translation import price_translations
from translations.discount_translation import discount_translations
from translations.certificate_translation import certificate_translations
from translations.about_translation import about_translations  # Import about translations

# Combine all translations into a single dictionary
translations = {}

# List of all translation dictionaries
translation_dicts = [
    app_translations,
    home_translations,
    fit_translations,
    learning_platform_translations,
    enrollment_translations,
    price_translations,
    discount_translations,
    certificate_translations,
    about_translations,
]

# Update the main translations dictionary with each translation dictionary
for t_dict in translation_dicts:
    for key, value in t_dict.items():
        if key in translations:
            st.warning(f"Duplicate translation key detected: '{key}'. Overwriting previous value.")
        translations[key] = value

def translate(key):
    """
    Retrieve a translated string for the given key based on the current language.

    Args:
        key (str): The translation key.

    Returns:
        str: The translated string if found; otherwise, returns a placeholder indicating a missing translation.
    """
    language = st.session_state.get('language', 'EN')  # Default to English if not set
    return translations.get(key, {}).get(language, f"[Missing translation for '{key}']").strip()
