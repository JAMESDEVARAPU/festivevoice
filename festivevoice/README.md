#  FestiveVoice – AI-Powered Event Corpus Collector

FestiveVoice is an open-source Streamlit-based application built as part of Viswam.ai's Summer of AI 2025. It collects multilingual data related to Indian **events, festivals, celebrations, and special occasions**, contributing to the development of inclusive LLMs for Indic languages.

---

##  Purpose

To create a crowd-powered engine that allows users to contribute event-related data (text, images, audio) in Indian languages, helping build diverse cultural corpora.

---

##  Features

- Multilingual form-based data submission
- Upload event descriptions, audio recordings, and photos
- Light-weight UI for low-internet areas
- Indic language support for contribution and UI
- Open-source and community-driven

---

##  Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Model/API:** OpenHathi (or any open-source LLM via Hugging Face or Dify.ai)
- **Hosting:** Streamlit Cloud / GitLab Pages (optional)

---

##  Team Members

| Name      | Role                          |
|-----------|-------------------------------|
| James     | Designer                      |
| Meghana   | Project Manager / Coordinator |
| Harshitha| Designer / Collector           |
| Bharath   | API / Content Integrator      |
| Midhula   | Designer / Collector          |

---

##  Run Locally

```bash
git clone https://code.swecha.org/devarapujames/festivevoice.git
cd festivevoice
pip install -r requirements.txt
streamlit run app.py
