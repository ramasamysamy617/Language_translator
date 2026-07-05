import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translator")

text = st.text_area("Enter text to translate")

languages = {
    "Tamil": "ta",
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

target_language = st.selectbox("Select Target Language", list(languages.keys()))

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source="auto",
            target=languages[target_language]
        ).translate(text)

        st.success("Translated Text:")
        st.write(translated)
    else:
        st.warning("Please enter some text.")