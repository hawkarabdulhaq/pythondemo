import streamlit as st
import os
import importlib
import json

# Directory where all translation modules are stored
TRANSLATION_DIR = "translations"

# Function to load translations from a module
def load_translation_module(module_name):
    module = importlib.import_module(f"{TRANSLATION_DIR}.{module_name}")
    return getattr(module, module_name.replace(".py", "").replace("_translation", "_translations"))

# Function to save updated translations back to the module file
def save_translation_file(file_path, translations):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"{json.dumps({'translations': translations}, ensure_ascii=False, indent=4)}\n")

# Load all translation files dynamically
translation_files = [f for f in os.listdir(TRANSLATION_DIR) if f.endswith("_translation.py")]
translations_data = {}
for file in translation_files:
    module_name = file.replace(".py", "")
    translations_data[module_name] = load_translation_module(module_name)

# App UI
st.title("Translation Management Tool")
st.sidebar.header("Select Translation File")

# Dropdown to select a translation file
selected_file = st.sidebar.selectbox("Select a file to edit:", translation_files)

if selected_file:
    # Display and edit translations for the selected file
    st.header(f"Editing Translations: {selected_file}")
    module_name = selected_file.replace(".py", "")
    translations = translations_data[module_name]

    # Display translations in a two-column table
    updated_translations = {}
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
        st.success(f"Translations for {selected_file} have been updated!")
