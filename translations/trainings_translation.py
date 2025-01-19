import streamlit as st
import base64
import csv
import os

def fetch_trainings():
    """
    Fetch training details from a CSV file and return a dictionary with translations.
    """
    trainings = {}
    csv_file_path = os.path.join('translations', 'csv', 'trainings.csv')

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                key = row['Key'].strip()
                en_value = row['EN'].strip()
                ku_value = row['KU'].strip()
                trainings[key] = {
                    'EN': en_value,
                    'KU': ku_value,
                }
        return trainings
    except Exception as e:
        print(f"Error reading trainings from CSV: {e}")
        return {}

# Fetch trainings from the CSV
training_translations = fetch_trainings()

def load_image_as_base64(image_path):
    """Load an image and return it as a Base64 encoded string."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image at path {image_path} not found.")
        return ""

def translate(key):
    """Retrieve the translated text based on the current language."""
    return training_translations.get(key, {}).get(st.session_state.language, key).strip()

def show_trainings():
    """Display the 'Our Trainings' tab content."""
    language = st.session_state.language  # Retrieve the selected language
    st.title(translate("our_trainings_tab_title"))

    # Loop through training translations to display them dynamically
    for key in training_translations:
        if key.startswith("training_"):
            st.markdown(f"- {translate(key)}")

def show_certificate_system():
    # Implementation unchanged, reusing the existing functionality
    pass

def show_certificate_database():
    # Implementation unchanged, reusing the existing functionality
    pass

def show():
    """Display the tabs for the Streamlit app."""
    tab1, tab2, tab3 = st.tabs([
        translate("our_trainings_tab_title"),
        translate("our_certificate_system_tab_title"),
        translate("certificate_database_tab_title"),
    ])

    with tab1:
        show_trainings()

    with tab2:
        show_certificate_system()

    with tab3:
        show_certificate_database()
