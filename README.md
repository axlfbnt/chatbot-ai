# 🤖 AI Chatbot Bubble Style (Streamlit + OpenRouter)

Proyek ini adalah chatbot berbasis web yang dibangun menggunakan **Streamlit** dan model AI dari **OpenRouter**, dengan tampilan percakapan bergaya bubble seperti chat app.

---

## 🚀 Fitur
- Tampilan percakapan ala chat bubble.
- Gunakan model `deepseek/deepseek-chat-v3-0324` dari OpenRouter.
- Dapat reset percakapan dengan tombol **New Chat**.
- Riwayat percakapan disimpan menggunakan `st.session_state`.

---

## 🧰 Requirements

Install dependencies dengan:

```bash
pip install streamlit requests
```

---

## 🔐 Setup API Key

Tambahkan file `.streamlit/secrets.toml` di root direktori project Anda:

```toml
[openrouter]
api_key = "YOUR_OPENROUTER_API_KEY"
```

Ganti `YOUR_OPENROUTER_API_KEY` dengan API key dari [OpenRouter](https://openrouter.ai).

---

## 🏃 Menjalankan Aplikasi

Jalankan dengan perintah:

```bash
streamlit run nama_file.py
```

Contoh:

```bash
streamlit run chatbot.py
```

---

## 📝 Struktur Kode

```python
# 1. Konfigurasi API & Header
# 2. Setup halaman Streamlit (judul, model info, tombol new chat)
# 3. Inisialisasi dan render histori percakapan
# 4. Tangani input user dan kirim ke API OpenRouter
# 5. Tampilkan respons bot ke layar dan simpan ke histori
```

---

## 📌 Catatan
- Pastikan API key aktif dan model tersedia di akun OpenRouter Anda.
- Referer dapat diganti jika Anda deploy ke domain publik.