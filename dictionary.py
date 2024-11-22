# dictionary.py

from translations.app_translation import app_translations
from translations.home_translation import home_translations
from translations.fit_translation import fit_translations
from translations.learning_platform_translation import learning_platform_translations

translations = {
    **app_translations,
    **home_translations,
    **fit_translations,
    **learning_platform_translations,
}

def translate(key, language):
    return translations.get(key, {}).get(language, key)
