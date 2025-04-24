import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", layout="centered")

st.title("🌍 Language Translator")
st.markdown("Translate text from one language to another designed by ╚══ ≪ °PARASHRAM° ≫ ══╝")

# Get supported languages and add 'auto' for source detection
translator = GoogleTranslator(source='english', target='french')
languages = translator.get_supported_languages(as_dict=True)
lang_names = list(languages.keys())
lang_names.insert(0, 'auto')  # Add 'auto' at the beginning

# Language selection
col1, col2 = st.columns(2)
with col1:
    src = st.selectbox("🔤 Source Language", options=lang_names, index=0)
with col2:
    dest = st.selectbox("🈯 Target Language", options=lang_names, index=lang_names.index("english"))

# Text input
text = st.text_area("✍️ Enter text to translate", height=150)

# Translate
if st.button("🌐 Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(source=src, target=dest).translate(text)
            st.success("✅ Translated Text")
            st.text_area("📝 Output", translated, height=150)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
