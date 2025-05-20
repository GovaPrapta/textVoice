import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="Text to Speech Multibahasa", page_icon="🗣️")

st.title("🌍 Konversi Teks ke Suara - Multibahasa")
st.write("Masukkan teks dan pilih bahasa untuk menghasilkan file suara (.mp3).")

languages = {
    "Indonesia": "id",
    "Inggris": "en",
    "Arab": "ar",
    "Jepang": "ja",
    "Korea": "ko",
    "Mandarin (Cina)": "zh-CN",
    "Prancis": "fr",
    "Jerman": "de",
    "Spanyol": "es"
}

text_input = st.text_area("📝 Masukkan Teks:", height=200)
selected_lang = st.selectbox("🌐 Pilih Bahasa:", options=list(languages.keys()))

if st.button("🔊 Ubah ke Suara"):
    if text_input.strip() == "":
        st.warning("Teks tidak boleh kosong.")
    else:
        lang_code = languages[selected_lang]
        tts = gTTS(text=text_input, lang=lang_code)
        filename = "output.mp3"
        tts.save(filename)

        with open(filename, 'rb') as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button("⬇️ Download Suara", data=audio_bytes, file_name="hasil_suara.mp3", mime='audio/mp3')

        os.remove(filename)
