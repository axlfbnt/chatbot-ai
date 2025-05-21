import streamlit as st
import requests

# Konfigurasi API
OPENROUTER_API_KEY = st.secrets["openrouter"]["api_key"]
MODEL = "deepseek/deepseek-chat-v3-0324"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "http://localhost:8501",
    "X-Title": "AI Chatbot Streamlit"
}
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Tampilan halaman
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🧠 AI Chatbot Bubble Style")
st.markdown(f"Powered by `{MODEL}` via OpenRouter 🤖")
st.markdown("<p style='text-align: center; font-size: 0.9em;'>Explored & curated by <b>Axel</b></p>", unsafe_allow_html=True)

# Tombol New Chat
if st.button("🔄 New Chat"):
    st.session_state.chat_history = []  # Hapus histori
    st.markdown("💬 Hello! How can I assist you today? 😊")


# Inisialisasi histori percakapan
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Tampilkan histori percakapan
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Input pengguna
user_input = st.chat_input("Tulis pesan di sini...")

# Jika ada input dari user
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Tampilkan spinner saat proses
    with st.spinner("Mengetik..."):
        payload = {
            "model": MODEL,
            "messages": [{"role": "system", "content": "You are a helpful assistant."}] +
                       [{"role": chat["role"], "content": chat["content"]} for chat in st.session_state.chat_history]
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)

    # Tangani response
    if response.status_code == 200:
        bot_reply = response.json()['choices'][0]['message']['content']
    else:
        bot_reply = "⚠️ Maaf, gagal mengambil respons dari OpenRouter."

    # Tampilkan balasan bot
    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})