import streamlit as st
import json
from datetime import datetime
from utils.theming import apply_chatgpt_theme
from utils.data_manager import save_user_data
from utils.ai_validation import validate_content
from utils.translations import get_translations

st.set_page_config(page_title="Language Learning", page_icon="📚", layout="wide")

# Apply theming
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = 'light'
apply_chatgpt_theme(st.session_state.theme_mode)

# Get translations
selected_language = st.session_state.get('selected_language', 'English')
translations = get_translations(selected_language)

st.title("📚 Indian Language Learning Hub")
st.markdown("### Learn and Contribute to India's Linguistic Diversity")

# Indian languages with their scripts and regions
indian_languages = {
    "Hindi": {
        "script": "Devanagari",
        "speakers": "600+ million",
        "regions": ["North India", "Central India"],
        "sample_text": "नमस्ते, आप कैसे हैं?",
        "meaning": "Hello, how are you?"
    },
    "Bengali": {
        "script": "Bengali",
        "speakers": "300+ million",
        "regions": ["West Bengal", "Bangladesh"],
        "sample_text": "নমস্কার, আপনি কেমন আছেন?",
        "meaning": "Hello, how are you?"
    },
    "Telugu": {
        "script": "Telugu",
        "speakers": "95+ million",
        "regions": ["Andhra Pradesh", "Telangana"],
        "sample_text": "నమస్కారం, మీరు ఎలా ఉన్నారు?",
        "meaning": "Hello, how are you?"
    },
    "Marathi": {
        "script": "Devanagari",
        "speakers": "83+ million",
        "regions": ["Maharashtra"],
        "sample_text": "नमस्कार, तुम्ही कसे आहात?",
        "meaning": "Hello, how are you?"
    },
    "Tamil": {
        "script": "Tamil",
        "speakers": "78+ million",
        "regions": ["Tamil Nadu", "Sri Lanka"],
        "sample_text": "வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?",
        "meaning": "Hello, how are you?"
    },
    "Gujarati": {
        "script": "Gujarati",
        "speakers": "56+ million",
        "regions": ["Gujarat"],
        "sample_text": "નમસ્તે, તમે કેમ છો?",
        "meaning": "Hello, how are you?"
    },
    "Kannada": {
        "script": "Kannada",
        "speakers": "44+ million",
        "regions": ["Karnataka"],
        "sample_text": "ನಮಸ್ಕಾರ, ನೀವು ಹೇಗಿದ್ದೀರಿ?",
        "meaning": "Hello, how are you?"
    },
    "Malayalam": {
        "script": "Malayalam",
        "speakers": "38+ million",
        "regions": ["Kerala"],
        "sample_text": "നമസ്കാരം, നിങ്ങൾ എങ്ങനെയിരിക്കുന്നു?",
        "meaning": "Hello, how are you?"
    },
    "Punjabi": {
        "script": "Gurmukhi",
        "speakers": "33+ million",
        "regions": ["Punjab"],
        "sample_text": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ, ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ?",
        "meaning": "Hello, how are you?"
    },
    "Odia": {
        "script": "Odia",
        "speakers": "38+ million",
        "regions": ["Odisha"],
        "sample_text": "ନମସ୍କାର, ଆପଣ କେମିତି ଅଛନ୍ତି?",
        "meaning": "Hello, how are you?"
    }
}

# Language selection
st.subheader("🗣️ Select a Language to Explore")
selected_lang = st.selectbox(
    "Choose an Indian language:",
    list(indian_languages.keys())
)

lang_data = indian_languages[selected_lang]

# Display language information
event_bg_color = st.session_state.get('event_color', '#E3F2FD')

st.markdown(f"""
<div style="background-color: {event_bg_color}; padding: 20px; border-radius: 10px; margin: 10px 0;">
    <h3>{selected_lang}</h3>
    <p><strong>Script:</strong> {lang_data['script']}</p>
    <p><strong>Speakers:</strong> {lang_data['speakers']}</p>
    <p><strong>Primary Regions:</strong> {', '.join(lang_data['regions'])}</p>
    <div style="font-size: 24px; margin: 10px 0;">
        <strong>Sample:</strong> {lang_data['sample_text']}
    </div>
    <p><em>Meaning:</em> {lang_data['meaning']}</p>
</div>
""", unsafe_allow_html=True)

# Interactive learning sections
st.markdown("---")
tabs = st.tabs([
    "📝 Contribute Vocabulary", 
    "📖 Share Phrases", 
    "🎵 Songs & Poetry", 
    "📚 Proverbs & Sayings",
    "🗣️ Dialects & Variations"
])

with tabs[0]:
    st.subheader(f"📝 Contribute {selected_lang} Vocabulary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        word_original = st.text_input(
            f"Word in {selected_lang}:",
            placeholder=f"Enter word in {selected_lang}..."
        )
        word_english = st.text_input(
            "English translation:",
            placeholder="Enter English meaning..."
        )
        word_category = st.selectbox(
            "Category:",
            ["Common Words", "Food & Cuisine", "Family Relations", "Colors", "Numbers", 
             "Nature", "Emotions", "Body Parts", "Clothing", "Transportation", "Other"]
        )
    
    with col2:
        word_pronunciation = st.text_input(
            "Pronunciation (optional):",
            placeholder="How to pronounce in English..."
        )
        word_context = st.text_area(
            "Usage context or example sentence:",
            placeholder="Provide an example of how this word is used...",
            height=100
        )
    
    if st.button("Submit Vocabulary") and word_original and word_english:
        user_data = {
            'type': 'vocabulary',
            'language': selected_lang,
            'original_word': word_original,
            'english_translation': word_english,
            'pronunciation': word_pronunciation,
            'category': word_category,
            'context': word_context,
            'user_language': selected_language,
            'timestamp': datetime.now().isoformat()
        }
        save_user_data(user_data)
        st.success(f"✅ Thank you for contributing to {selected_lang} vocabulary!")

with tabs[1]:
    st.subheader(f"📖 Share {selected_lang} Phrases")
    
    phrase_original = st.text_area(
        f"Phrase in {selected_lang}:",
        placeholder=f"Enter phrase in {selected_lang}...",
        height=80
    )
    phrase_english = st.text_area(
        "English translation:",
        placeholder="Enter English translation...",
        height=80
    )
    phrase_type = st.selectbox(
        "Phrase type:",
        ["Greetings", "Common Expressions", "Polite Phrases", "Questions", 
         "Exclamations", "Idioms", "Religious/Spiritual", "Other"]
    )
    phrase_situation = st.text_input(
        "When is this phrase used?",
        placeholder="Describe the situation or context..."
    )
    
    if st.button("Submit Phrase") and phrase_original and phrase_english:
        user_data = {
            'type': 'phrase',
            'language': selected_lang,
            'original_phrase': phrase_original,
            'english_translation': phrase_english,
            'phrase_type': phrase_type,
            'usage_situation': phrase_situation,
            'user_language': selected_language,
            'timestamp': datetime.now().isoformat()
        }
        save_user_data(user_data)
        st.success(f"✅ Phrase contributed successfully to {selected_lang}!")

with tabs[2]:
    st.subheader(f"🎵 {selected_lang} Songs & Poetry")
    
    content_type = st.radio(
        "Type of content:",
        ["Folk Song", "Religious Hymn", "Classical Poetry", "Children's Rhyme", "Modern Song"]
    )
    
    title = st.text_input("Title:")
    content_original = st.text_area(
        f"Content in {selected_lang}:",
        placeholder=f"Enter the song/poem in {selected_lang}...",
        height=150
    )
    content_translation = st.text_area(
        "English translation/summary:",
        placeholder="Translate or summarize in English...",
        height=100
    )
    cultural_significance = st.text_area(
        "Cultural significance or background:",
        placeholder="Explain the cultural importance, origin, or context...",
        height=80
    )
    
    if st.button("Submit Song/Poetry") and title and content_original:
        user_data = {
            'type': 'song_poetry',
            'language': selected_lang,
            'content_type': content_type,
            'title': title,
            'original_content': content_original,
            'english_translation': content_translation,
            'cultural_significance': cultural_significance,
            'user_language': selected_language,
            'timestamp': datetime.now().isoformat()
        }
        save_user_data(user_data)
        st.success(f"✅ {content_type} contributed successfully!")

with tabs[3]:
    st.subheader(f"📚 {selected_lang} Proverbs & Sayings")
    
    proverb_original = st.text_area(
        f"Proverb/Saying in {selected_lang}:",
        placeholder=f"Enter the proverb in {selected_lang}...",
        height=80
    )
    proverb_meaning = st.text_area(
        "Literal meaning:",
        placeholder="What does it mean word-for-word?",
        height=60
    )
    proverb_lesson = st.text_area(
        "Life lesson or moral:",
        placeholder="What wisdom does this proverb convey?",
        height=80
    )
    proverb_usage = st.text_input(
        "When is this proverb used?",
        placeholder="In what situations do people use this saying?"
    )
    
    if st.button("Submit Proverb") and proverb_original and proverb_lesson:
        user_data = {
            'type': 'proverb',
            'language': selected_lang,
            'original_proverb': proverb_original,
            'literal_meaning': proverb_meaning,
            'life_lesson': proverb_lesson,
            'usage_context': proverb_usage,
            'user_language': selected_language,
            'timestamp': datetime.now().isoformat()
        }
        save_user_data(user_data)
        st.success("✅ Proverb wisdom shared successfully!")

with tabs[4]:
    st.subheader(f"🗣️ {selected_lang} Dialects & Regional Variations")
    
    dialect_region = st.text_input(
        "Region/Area:",
        placeholder="Which region does this dialect come from?"
    )
    dialect_name = st.text_input(
        "Dialect name (if known):",
        placeholder="Local name for this variation..."
    )
    dialect_differences = st.text_area(
        "How is it different from standard language?",
        placeholder="Describe pronunciation, vocabulary, or grammar differences...",
        height=100
    )
    dialect_examples = st.text_area(
        "Examples of dialect-specific words/phrases:",
        placeholder="Provide examples with translations...",
        height=100
    )
    
    if st.button("Submit Dialect Info") and dialect_region and dialect_differences:
        user_data = {
            'type': 'dialect',
            'language': selected_lang,
            'region': dialect_region,
            'dialect_name': dialect_name,
            'differences': dialect_differences,
            'examples': dialect_examples,
            'user_language': selected_language,
            'timestamp': datetime.now().isoformat()
        }
        save_user_data(user_data)
        st.success("✅ Dialect information contributed successfully!")

# Learning progress gamification
st.markdown("---")
st.subheader("🏆 Your Learning Contributions")

if 'user_contributions' in st.session_state:
    language_contributions = [
        contrib for contrib in st.session_state.user_contributions 
        if contrib.get('type') in ['vocabulary', 'phrase', 'song_poetry', 'proverb', 'dialect']
    ]
    
    if language_contributions:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Words/Phrases", len([c for c in language_contributions if c.get('type') in ['vocabulary', 'phrase']]))
        with col2:
            st.metric("Cultural Content", len([c for c in language_contributions if c.get('type') in ['song_poetry', 'proverb']]))
        with col3:
            st.metric("Dialect Info", len([c for c in language_contributions if c.get('type') == 'dialect']))
    else:
        st.info("Start contributing to see your progress!")

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏛️ ← Historical Timeline"):
        st.switch_page("pages/1_🏛️_Historical_Timeline.py")
with col2:
    if st.button("🏠 Back to Home"):
        st.switch_page("app.py")
with col3:
    if st.button("🎭 Cultural Stories →"):
        st.switch_page("pages/3_🎭_Cultural_Stories.py")
