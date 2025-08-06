import streamlit as st
import json
import os
from datetime import datetime
from utils.theming import apply_chatgpt_theme, toggle_theme
from utils.data_manager import save_user_data, load_corpus_data
from utils.translations import get_translations, SUPPORTED_LANGUAGES
from utils.ai_validation import validate_content

# Page config
st.set_page_config(
    page_title="भारतीय संस्कृति - Indian Culture Explorer",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = 'light'
if 'selected_language' not in st.session_state:
    st.session_state.selected_language = 'English'
if 'user_contributions' not in st.session_state:
    st.session_state.user_contributions = []

# Apply ChatGPT-style theming
apply_chatgpt_theme(st.session_state.theme_mode)

# Sidebar configuration
with st.sidebar:
    st.title("🇮🇳 भारतीय संस्कृति")
    st.markdown("*Discover the Rich Heritage of India*")
    
    # Language selection
    st.subheader("🌐 Language / भाषा")
    selected_lang = st.selectbox(
        "Choose your language:",
        options=list(SUPPORTED_LANGUAGES.keys()),
        index=list(SUPPORTED_LANGUAGES.keys()).index(st.session_state.selected_language),
        key="lang_selector"
    )
    st.session_state.selected_language = selected_lang
    
    # Theme toggle
    st.subheader("🎨 Theme")
    if st.button("🌓 Toggle Light/Dark Mode"):
        toggle_theme()
        st.rerun()
    
    # Event color customization
    st.subheader("🎨 Event Colors")
    event_bg_color = st.color_picker(
        "Choose event background color:",
        value="#E3F2FD",
        key="event_color"
    )
    
    # User stats
    st.subheader("📊 Your Contributions")
    st.metric("Total Submissions", len(st.session_state.user_contributions))

# Get translations for selected language
translations = get_translations(st.session_state.selected_language)

# Main content
st.title(f"🇮🇳 {translations['title']}")
st.markdown(f"### {translations['subtitle']}")

# Welcome section with contribution opportunity
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    <div style="background-color: {event_bg_color}; padding: 20px; border-radius: 10px; margin: 10px 0;">
        <h3>🙏 {translations['welcome_title']}</h3>
        <p>{translations['welcome_message']}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### 🌟 Quick Contribute")
    with st.expander("Share a Cultural Fact"):
        cultural_fact = st.text_area(
            "Share an interesting fact about Indian culture:",
            placeholder="e.g., Did you know that yoga originated in India over 5,000 years ago?",
            key="quick_fact"
        )
        fact_category = st.selectbox(
            "Category:",
            ["History", "Religion", "Art", "Music", "Dance", "Food", "Language", "Tradition"]
        )
        
        if st.button("Submit Fact") and cultural_fact:
            # Validate content with AI
            validation_result = validate_content(cultural_fact, fact_category)
            
            if validation_result['is_valid']:
                # Save to corpus
                user_data = {
                    'type': 'cultural_fact',
                    'content': cultural_fact,
                    'category': fact_category,
                    'language': st.session_state.selected_language,
                    'timestamp': datetime.now().isoformat(),
                    'quality_score': validation_result['quality_score']
                }
                
                save_user_data(user_data)
                st.session_state.user_contributions.append(user_data)
                st.success("✅ Thank you for your contribution!")
                st.balloons()
            else:
                st.warning("⚠️ Please provide more detailed information.")

# Featured sections
st.markdown("---")
st.markdown("### 🚀 Explore Indian Culture")

# Create feature cards
feature_cols = st.columns(4)

with feature_cols[0]:
    if st.button("🏛️ Historical Timeline", use_container_width=True):
        st.switch_page("pages/1_🏛️_Historical_Timeline.py")
    st.caption("Explore major events in Indian history")

with feature_cols[1]:
    if st.button("📚 Language Learning", use_container_width=True):
        st.switch_page("pages/2_📚_Language_Learning.py")
    st.caption("Learn Indian languages and scripts")

with feature_cols[2]:
    if st.button("🎭 Cultural Stories", use_container_width=True):
        st.switch_page("pages/3_🎭_Cultural_Stories.py")
    st.caption("Share and read cultural narratives")

with feature_cols[3]:
    if st.button("🧠 Cultural Quiz", use_container_width=True):
        st.switch_page("pages/4_🧠_Cultural_Quiz.py")
    st.caption("Test your knowledge")

# Recent contributions display
st.markdown("---")
st.markdown("### 📝 Recent Community Contributions")

# Load and display recent corpus data
corpus_data = load_corpus_data()
if corpus_data:
    recent_contributions = sorted(corpus_data, key=lambda x: x.get('timestamp', ''), reverse=True)[:5]
    
    for contrib in recent_contributions:
        with st.expander(f"{contrib.get('category', 'General')} - {contrib.get('type', 'Contribution')}"):
            st.write(contrib.get('content', ''))
            st.caption(f"Language: {contrib.get('language', 'Unknown')} | Quality Score: {contrib.get('quality_score', 'N/A')}")
else:
    st.info("🌟 Be the first to contribute to our cultural knowledge base!")

# Footer with corpus collection hints
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; padding: 20px; border-radius: 10px; background-color: {'#2d3748' if st.session_state.theme_mode == 'dark' else '#f7fafc'};">
    <h4>🤝 {translations['community_title']}</h4>
    <p>{translations['community_message']}</p>
    <small>{translations['data_usage_note']}</small>
</div>
""", unsafe_allow_html=True)
