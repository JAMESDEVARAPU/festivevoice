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
    # Language selection at top
    selected_lang = st.selectbox(
        "Language",
        options=list(SUPPORTED_LANGUAGES.keys()),
        index=list(SUPPORTED_LANGUAGES.keys()).index(st.session_state.selected_language),
        key="lang_selector",
        label_visibility="collapsed"
    )
    st.session_state.selected_language = selected_lang
    
    # User Profile Section
    st.markdown("### 👤 User Profile")
    
    # Initialize session state for user profile
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = {
            'username': '',
            'email': '',
            'region': 'North India'
        }
    
    username = st.text_input(
        "Username / उपयोगकर्ता नाम:",
        value=st.session_state.user_profile['username'],
        placeholder="Enter your username"
    )
    st.session_state.user_profile['username'] = username
    
    email = st.text_input(
        "Email:",
        value=st.session_state.user_profile['email'],
        placeholder="Enter your email"
    )
    st.session_state.user_profile['email'] = email
    
    region = st.selectbox(
        "Region / क्षेत्र:",
        options=["North India", "South India", "East India", "West India", "Central India", "Northeast India"],
        index=["North India", "South India", "East India", "West India", "Central India", "Northeast India"].index(st.session_state.user_profile['region'])
    )
    st.session_state.user_profile['region'] = region
    
    if st.button("Join Community / समुदाय में शामिल हों", use_container_width=True):
        if username and email:
            st.success("Welcome to the community!")
        else:
            st.warning("Please fill all fields")
    
    st.markdown("---")
    
    # Theme toggle
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

# Get translations for selected language
translations = get_translations(st.session_state.selected_language)

# Main content - Orange banner with Viswam.ai branding
st.markdown("""
<div style="
    background: linear-gradient(135deg, #FF7F50 0%, #FF6B35 100%);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
">
    <div style="
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        display: inline-block;
        margin-bottom: 1rem;
    ">
        <span style="color: white; font-size: 2rem; margin-right: 0.5rem;">🕉️</span>
        <span style="color: white; font-size: 1.5rem; font-weight: bold;">
            Viswam.ai - भारतीय सांस्कृतिक संग्रह
        </span>
    </div>
    <h2 style="
        color: white;
        margin: 1rem 0;
        font-size: 1.2rem;
        font-weight: normal;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    ">
        Preserving India's Rich Cultural Heritage Through Community Contributions
    </h2>
    <p style="
        color: white;
        margin: 0.5rem 0 0 0;
        font-size: 1rem;
        opacity: 0.9;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    ">
        समुदायिक योगदान के माध्यम से भारत की समृद्ध सांस्कृतिक विरासत का संरक्षण
    </p>
</div>
""", unsafe_allow_html=True)

# Login message (similar to screenshot)
if not st.session_state.user_profile.get('username'):
    st.markdown("""
    <div style="
        background-color: #FFF3CD;
        border: 1px solid #FFEAA7;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        margin-bottom: 1.5rem;
    ">
        <span style="color: #856404;">
            Please login from the sidebar to start contributing! / कृपया योगदान शुरू करने के लिए साइडबार से लॉगिन करें।
        </span>
    </div>
    """, unsafe_allow_html=True)

# Statistics section (matching screenshot design)
col1, col2, col3 = st.columns(3)
data = load_corpus_data()

with col1:
    story_count = len([item for item in data if item.get('type') == 'story'])
    st.markdown(f"""
    <div style="
        background-color: #F8F9FA;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #E9ECEF;
        margin-bottom: 1rem;
    ">
        <h3 style="margin: 0; color: #6C757D; font-size: 0.9rem; font-weight: normal;">Total Stories</h3>
        <h1 style="margin: 0.5rem 0 0 0; color: #495057; font-size: 2.5rem; font-weight: bold;">{story_count}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    cultural_count = len([item for item in data if item.get('type') == 'cultural'])
    st.markdown(f"""
    <div style="
        background-color: #F8F9FA;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #E9ECEF;
        margin-bottom: 1rem;
    ">
        <h3 style="margin: 0; color: #6C757D; font-size: 0.9rem; font-weight: normal;">Cultural Practices</h3>
        <h1 style="margin: 0.5rem 0 0 0; color: #495057; font-size: 2.5rem; font-weight: bold;">{cultural_count}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    event_count = len([item for item in data if item.get('category') in ['Festivals', 'Religious Events', 'Cultural Celebrations']])
    st.markdown(f"""
    <div style="
        background-color: #F8F9FA;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #E9ECEF;
        margin-bottom: 1rem;
    ">
        <h3 style="margin: 0; color: #6C757D; font-size: 0.9rem; font-weight: normal;">Festival Events</h3>
        <h1 style="margin: 0.5rem 0 0 0; color: #495057; font-size: 2.5rem; font-weight: bold;">{event_count}</h1>
    </div>
    """, unsafe_allow_html=True)

# How to Contribute section (matching screenshot)
st.markdown("""
<div style="
    text-align: center;
    margin: 2rem 0;
">
    <h2 style="
        color: #FF6B35;
        margin-bottom: 1rem;
        display: inline-block;
    ">
        🎯 How to Contribute / कैसे योगदान करें
    </h2>
</div>
""", unsafe_allow_html=True)

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
            "Share details about festivals or cultural events:",
            placeholder="e.g., Diwali is celebrated for 5 days and signifies the victory of light over darkness...",
            key="quick_fact"
        )
        fact_category = st.selectbox(
            "Category:",
            ["Festivals", "Religious Events", "Cultural Celebrations", "Historical Events", "Traditional Practices", "Food Culture", "Art & Music", "Language & Literature", "Regional Customs"]
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
    if st.button("🎊 Festivals & Events", use_container_width=True):
        st.switch_page("pages/6_🎊_Festivals_Events.py")
    st.caption("Explore Indian festivals")

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
