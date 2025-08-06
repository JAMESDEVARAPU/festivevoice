import streamlit as st
import json
from datetime import datetime
from utils.theming import apply_chatgpt_theme
from utils.data_manager import save_user_data
from utils.ai_validation import validate_content
from utils.translations import get_translations

st.set_page_config(page_title="Historical Timeline", page_icon="🏛️", layout="wide")

# Apply theming
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = 'light'
apply_chatgpt_theme(st.session_state.theme_mode)

# Get translations
selected_language = st.session_state.get('selected_language', 'English')
translations = get_translations(selected_language)

st.title("🏛️ Indian Historical Timeline")
st.markdown("### Explore and Contribute to India's Rich History")

# Event background color from session state
event_bg_color = st.session_state.get('event_color', '#E3F2FD')

# Historical periods with contribution opportunities
periods = {
    "Indus Valley Civilization (3300-1300 BCE)": {
        "description": "One of the world's earliest urban civilizations",
        "key_events": ["Harappan settlements", "Advanced drainage systems", "Indus script"],
        "contribution_prompt": "Share any local legends or archaeological findings from this period"
    },
    "Vedic Period (1500-500 BCE)": {
        "description": "Foundation of Hindu philosophy and culture",
        "key_events": ["Composition of Vedas", "Caste system development", "Early Sanskrit literature"],
        "contribution_prompt": "Contribute Vedic hymns, mantras, or their interpretations"
    },
    "Mauryan Empire (322-185 BCE)": {
        "description": "First pan-Indian empire under Chandragupta and Ashoka",
        "key_events": ["Ashoka's conversion to Buddhism", "Edicts of Ashoka", "Trade with Hellenistic world"],
        "contribution_prompt": "Share stories about Ashoka's dhamma or Buddhist teachings"
    },
    "Gupta Empire (320-550 CE)": {
        "description": "Golden Age of Indian culture and science",
        "key_events": ["Advancements in mathematics", "Classical Sanskrit literature", "Temple architecture"],
        "contribution_prompt": "Contribute information about scientific discoveries or literary works"
    },
    "Medieval Period (1000-1500 CE)": {
        "description": "Islamic invasions and cultural synthesis",
        "key_events": ["Delhi Sultanate", "Bhakti movement", "Indo-Islamic architecture"],
        "contribution_prompt": "Share stories of cultural synthesis and religious harmony"
    },
    "Mughal Empire (1526-1857 CE)": {
        "description": "Peak of Indo-Islamic culture and architecture",
        "key_events": ["Akbar's religious tolerance", "Taj Mahal construction", "Mughal miniature paintings"],
        "contribution_prompt": "Contribute information about Mughal art, architecture, or court culture"
    },
    "British Colonial Period (1858-1947)": {
        "description": "Struggle for independence and modern nation building",
        "key_events": ["1857 Revolt", "Indian National Congress formation", "Gandhi's movements"],
        "contribution_prompt": "Share family stories or local freedom struggle narratives"
    },
    "Independent India (1947-Present)": {
        "description": "Modern India's journey as a democratic republic",
        "key_events": ["Partition", "Green Revolution", "IT revolution"],
        "contribution_prompt": "Share contemporary cultural developments or regional progress stories"
    }
}

# Interactive timeline
st.markdown("---")
st.subheader("🕰️ Interactive Timeline")

selected_period = st.selectbox(
    "Select a historical period to explore:",
    list(periods.keys())
)

period_data = periods[selected_period]

# Display period information
st.markdown(f"""
<div style="background-color: {event_bg_color}; padding: 20px; border-radius: 10px; margin: 10px 0;">
    <h3>{selected_period}</h3>
    <p><strong>Description:</strong> {period_data['description']}</p>
    <p><strong>Key Events:</strong></p>
    <ul>
        {''.join([f'<li>{event}</li>' for event in period_data['key_events']])}
    </ul>
</div>
""", unsafe_allow_html=True)

# Contribution section for selected period
st.markdown("---")
st.subheader(f"📝 Contribute to {selected_period}")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"**{period_data['contribution_prompt']}**")
    
    user_contribution = st.text_area(
        "Your historical contribution:",
        placeholder="Share stories, facts, interpretations, or local knowledge...",
        height=150,
        key=f"contrib_{selected_period}"
    )
    
    contribution_type = st.selectbox(
        "Type of contribution:",
        ["Historical Event", "Cultural Practice", "Personal/Family Story", "Local Legend", 
         "Archaeological Finding", "Literary Reference", "Religious/Philosophical Text"]
    )
    
    source_language = st.selectbox(
        "Original language (if applicable):",
        ["Sanskrit", "Hindi", "Tamil", "Bengali", "Telugu", "Marathi", "Gujarati", 
         "Kannada", "Malayalam", "Punjabi", "Urdu", "Other", "Not Applicable"]
    )

with col2:
    st.markdown("#### 💡 Contribution Tips")
    st.info("""
    • Include specific dates if known
    • Mention geographical locations
    • Cite sources when possible
    • Share personal or family connections
    • Include local variations of stories
    • Mention regional significance
    """)

# Submit contribution
if st.button("Submit Historical Contribution") and user_contribution:
    # Validate with AI
    validation_result = validate_content(
        user_contribution, 
        f"Historical content about {selected_period}"
    )
    
    if validation_result['is_valid']:
        # Save to corpus
        user_data = {
            'type': 'historical_contribution',
            'period': selected_period,
            'content': user_contribution,
            'contribution_type': contribution_type,
            'source_language': source_language,
            'language': selected_language,
            'timestamp': datetime.now().isoformat(),
            'quality_score': validation_result['quality_score']
        }
        
        save_user_data(user_data)
        if 'user_contributions' not in st.session_state:
            st.session_state.user_contributions = []
        st.session_state.user_contributions.append(user_data)
        
        st.success("✅ Thank you for enriching our historical knowledge base!")
        st.balloons()
    else:
        st.warning("⚠️ Please provide more detailed historical information.")

# Additional features
st.markdown("---")
st.subheader("🔍 Advanced Historical Features")

tabs = st.tabs(["📚 Historical Texts", "🗺️ Regional History", "👥 Historical Figures"])

with tabs[0]:
    st.markdown("#### Share Historical Texts and Documents")
    text_title = st.text_input("Text/Document Title:")
    text_content = st.text_area("Content or Description:", height=100)
    text_period = st.selectbox("Historical Period:", list(periods.keys()), key="text_period")
    
    if st.button("Submit Historical Text") and text_title and text_content:
        user_data = {
            'type': 'historical_text',
            'title': text_title,
            'content': text_content,
            'period': text_period,
            'language': selected_language,
            'timestamp': datetime.now().isoformat()
        }
        save_user_data(user_data)
        st.success("✅ Historical text submitted successfully!")

with tabs[1]:
    st.markdown("#### Regional Historical Contributions")
    region = st.text_input("Region/State/City:")
    regional_history = st.text_area("Regional historical information:", height=100)
    
    if st.button("Submit Regional History") and region and regional_history:
        user_data = {
            'type': 'regional_history',
            'region': region,
            'content': regional_history,
            'language': selected_language,
            'timestamp': datetime.now().isoformat()
        }
        save_user_data(user_data)
        st.success("✅ Regional history submitted successfully!")

with tabs[2]:
    st.markdown("#### Historical Figures and Personalities")
    figure_name = st.text_input("Historical Figure Name:")
    figure_info = st.text_area("Information about the historical figure:", height=100)
    figure_period = st.selectbox("Time Period:", list(periods.keys()), key="figure_period")
    
    if st.button("Submit Historical Figure") and figure_name and figure_info:
        user_data = {
            'type': 'historical_figure',
            'name': figure_name,
            'content': figure_info,
            'period': figure_period,
            'language': selected_language,
            'timestamp': datetime.now().isoformat()
        }
        save_user_data(user_data)
        st.success("✅ Historical figure information submitted successfully!")

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("← Back to Home"):
        st.switch_page("app.py")
with col2:
    if st.button("📚 Language Learning →"):
        st.switch_page("pages/2_📚_Language_Learning.py")
with col3:
    if st.button("🎭 Cultural Stories →"):
        st.switch_page("pages/3_🎭_Cultural_Stories.py")
