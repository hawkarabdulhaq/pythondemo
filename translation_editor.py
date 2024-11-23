import streamlit as st
import os
import importlib
import json
import shutil

# Directory where all translation modules are stored
TRANSLATION_DIR = "translations"

# Function to load translations from a module
def load_translation_module(module_name):
    """Load translations from the given module."""
    try:
        module = importlib.import_module(f"{TRANSLATION_DIR}.{module_name}")
        return getattr(module, module_name.replace(".py", "").replace("_translation", "_translations"))
    except AttributeError:
        st.error(f"Error: Module '{module_name}' does not contain the expected translations attribute.")
        return {}
    except Exception as e:
        st.error(f"Error loading module '{module_name}': {e}")
        return {}

# Function to validate translation structure
def validate_translations(module_name, translations):
    """Ensure translations are in the correct format before saving."""
    expected_variable = module_name.replace(".py", "_translations")
    if not isinstance(translations, dict):
        raise ValueError(f"Translations for {module_name} must be a dictionary.")
    return expected_variable

# Function to save updated translations back to the module file
def save_translation_file(file_path, translations):
    """Save translations to the module file."""
    try:
        # Validate translations structure
        module_name = os.path.basename(file_path)
        variable_name = validate_translations(module_name, translations)

        # Create a backup of the file
        backup_path = f"{file_path}.backup"
        shutil.copy(file_path, backup_path)

        # Save updated translations
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"{variable_name} = {json.dumps(translations, ensure_ascii=False, indent=4)}\n")
        
        st.success(f"Translations for {os.path.basename(file_path)} have been saved successfully!")
    except Exception as e:
        st.error(f"Failed to save translations: {e}")

# Load all translation files dynamically
translation_files = [f for f in os.listdir(TRANSLATION_DIR) if f.endswith("_translation.py")]
translations_data = {}
for file in translation_files:
    module_name = file.replace(".py", "")
    translations_data[module_name] = load_translation_module(module_name)

# Initialize App State
if "selected_file" not in st.session_state:
    st.session_state.selected_file = None

# Sidebar Navigation with Buttons
st.sidebar.title("Translation Management")
st.sidebar.markdown("### Select a file to edit:")

for file in translation_files:
    if st.sidebar.button(file):
        st.session_state.selected_file = file  # Set the selected file

# Main Content
if st.session_state.selected_file:
    selected_file = st.session_state.selected_file
    st.title(f"Editing Translations: {selected_file}")
    module_name = selected_file.replace(".py", "")
    translations = translations_data.get(module_name, {})

    if translations:
        # Display translations in a two-column table
        updated_translations = {}
        st.markdown("### Translation Table")
        for key, langs in translations.items():
            st.write(f"**{key}**")
            col1, col2 = st.columns([1, 1])
            col1.text_input("English", value=langs.get("EN", ""), disabled=True, key=f"{key}_EN")
            new_kurdish = col2.text_input("Kurdish", value=langs.get("KU", ""), key=f"{key}_KU")
            updated_translations[key] = {"EN": langs.get("EN", ""), "KU": new_kurdish}

        # Save button
        if st.button("Save Changes"):
            file_path = os.path.join(TRANSLATION_DIR, selected_file)
            save_translation_file(file_path, updated_translations)
    else:
        st.error(f"No translations found for the selected file: {selected_file}")
else:
    st.title("Welcome to the Translation Management Tool")
    st.markdown("""
    This tool allows you to manage translations for your app.
    - Select a translation file from the sidebar to start editing.
    - Edit Kurdish translations and save your changes.
    """)
