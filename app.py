import streamlit as st
import json
import os
from datetime import datetime
from utils.theming import apply_chatgpt_theme
from utils.data_manager import save_user_data, load_corpus_data
from utils.translations import get_translations, SUPPORTED_LANGUAGES
from utils.ai_validation import validate_content
from utils.auth import auth_sidebar, is_logged_in, get_current_user, update_user_contributions

# Page config
st.set_page_config(
    page_title="Indian Culture Explorer",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state - fixed light theme
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
    
    st.markdown("---")
    
    # Authentication Section
    auth_sidebar()
    
    st.markdown("---")
    
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
    background: linear-gradient(135deg, rgba(255, 127, 80, 0.95) 0%, rgba(255, 107, 53, 0.95) 100%);
    background-image: 
        radial-gradient(circle at 30% 20%, rgba(255, 215, 0, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 70% 80%, rgba(255, 165, 0, 0.08) 0%, transparent 50%);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
    position: relative;
    overflow: hidden;
">
    <div style="
        position: absolute;
        top: 10px;
        left: 20px;
        right: 20px;
        height: 3px;
        background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.3), transparent);
        border-radius: 2px;
    "></div>
    <div style="
        position: absolute;
        bottom: 10px;
        left: 20px;
        right: 20px;
        height: 3px;
        background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.3), transparent);
        border-radius: 2px;
    "></div>
    
    <div style="
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 200px;
        height: 200px;
        border: 1px solid rgba(255, 215, 0, 0.1);
        border-radius: 50%;
        z-index: 1;
    "></div>
    <div style="
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 150px;
        height: 150px;
        border: 1px solid rgba(255, 215, 0, 0.08);
        border-radius: 50%;
        z-index: 1;
    "></div>
    
    <div style="position: relative; z-index: 2;">
        <div style="
            background: rgba(255, 255, 255, 0.15);
            padding: 0.5rem 1.5rem;
            border-radius: 25px;
            display: inline-block;
            margin-bottom: 1rem;
            border: 1px solid rgba(255, 215, 0, 0.2);
            backdrop-filter: blur(5px);
        ">
            <span style="color: white; font-size: 2rem; margin-right: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">🕉️</span>
            <span style="color: white; font-size: 1.5rem; font-weight: bold; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                Viswam.ai - Indian Cultural Collection
            </span>
        </div>
        <h2 style="
            color: white;
            margin: 1rem 0;
            font-size: 1.2rem;
            font-weight: normal;
            text-shadow: 0 2px 6px rgba(0,0,0,0.4);
            letter-spacing: 0.5px;
        ">
            Preserving India's Rich Cultural Heritage Through Community Contributions
        </h2>
        <p style="
            color: white;
            margin: 0.5rem 0 0 0;
            font-size: 1rem;
            opacity: 0.95;
            text-shadow: 0 1px 3px rgba(0,0,0,0.4);
        ">
            🏛️ Blessed by the divine grace of Lord Venkateswara 🙏
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Login message for non-authenticated users
if not is_logged_in():
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
            Please login from the sidebar to start contributing!
        </span>
    </div>
    """, unsafe_allow_html=True)

# Statistics section (matching screenshot design)
col1, col2, col3 = st.columns(3)
data = load_corpus_data()

with col1:
    voice_count = len([item for item in data if item.get('type') == 'voice_story'])
    st.markdown(f"""
    <div style="
        background-color: #F8F9FA;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #E9ECEF;
        margin-bottom: 1rem;
    ">
        <h3 style="margin: 0; color: #6C757D; font-size: 0.9rem; font-weight: normal;">Voice Stories</h3>
        <h1 style="margin: 0.5rem 0 0 0; color: #495057; font-size: 2.5rem; font-weight: bold;">{voice_count}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    video_count = len([item for item in data if item.get('type') == 'video_tradition'])
    st.markdown(f"""
    <div style="
        background-color: #F8F9FA;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #E9ECEF;
        margin-bottom: 1rem;
    ">
        <h3 style="margin: 0; color: #6C757D; font-size: 0.9rem; font-weight: normal;">Video Traditions</h3>
        <h1 style="margin: 0.5rem 0 0 0; color: #495057; font-size: 2.5rem; font-weight: bold;">{video_count}</h1>
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
        🎯 How to Contribute
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
            if not is_logged_in():
                st.warning("Please login to submit contributions")
            else:
                current_user = get_current_user()
                # Validate content with AI
                validation_result = validate_content(cultural_fact, fact_category)
                
                if validation_result['is_valid']:
                    # Save to corpus
                    username = current_user.get('username', 'unknown') if current_user else 'unknown'
                    user_data = {
                        'type': 'cultural_fact',
                        'content': cultural_fact,
                        'category': fact_category,
                        'language': st.session_state.selected_language,
                        'timestamp': datetime.now().isoformat(),
                        'quality_score': validation_result['quality_score'],
                        'contributor': username
                    }
                    
                    save_user_data(user_data)
                    update_user_contributions(username)
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
    if st.button("🎙️ Voice Stories", use_container_width=True):
        st.switch_page("pages/1_Voice_Stories.py")
    st.caption("Record and share cultural stories")

with feature_cols[1]:
    if st.button("📹 Video Traditions", use_container_width=True):
        st.switch_page("pages/2_Video_Traditions.py")
    st.caption("Upload videos of cultural practices")

with feature_cols[2]:
    if st.button("🎭 Cultural Stories", use_container_width=True):
        st.switch_page("pages/3_🎭_Cultural_Stories.py")
    st.caption("Share and read cultural narratives")

with feature_cols[3]:
    if st.button("🎊 Festivals & Events", use_container_width=True):
        st.switch_page("pages/6_Festivals_Events.py")
    st.caption("Explore Indian festivals")

# Add second row of features
st.markdown("### 🌟 Explore & Discover")
feature_cols2 = st.columns(2)

with feature_cols2[0]:
    if st.button("🖼️ Community Gallery", use_container_width=True):
        st.switch_page("pages/5_Community_Gallery.py")
    st.caption("View all uploaded content from community")

with feature_cols2[1]:
    if is_logged_in():
        if st.button("📝 My Contributions", use_container_width=True):
            st.switch_page("pages/7_My_Contributions.py")
        st.caption("Manage your personal uploads")
    else:
        st.markdown("""
        <div style="
            padding: 1rem;
            border-radius: 8px;
            background-color: #F8F9FA;
            text-align: center;
            border: 2px dashed #DEE2E6;
        ">
            <p style="margin: 0; color: #6C757D;">Login to view your contributions</p>
        </div>
        """, unsafe_allow_html=True)



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
