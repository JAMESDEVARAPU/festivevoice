import streamlit as st
import json
from datetime import datetime
from utils.data_manager import load_corpus_data
from utils.theming import apply_chatgpt_theme
from utils.translations import get_translations
from utils.auth import is_logged_in, get_current_user, auth_sidebar

# Initialize session state
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = 'light'
if 'selected_language' not in st.session_state:
    st.session_state.selected_language = 'English'

# Apply ChatGPT-style theming with full background
apply_chatgpt_theme(st.session_state.theme_mode)

# Add full page Lord Venkateswara background
try:
    import base64
    with open('attached_assets/81J34SDlNeL_1754506571834.jpg', 'rb') as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()
    
    st.markdown(f"""
    <style>
    .stApp {{
        background: 
            linear-gradient(rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.88)),
            url('data:image/jpeg;base64,{img_base64}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    .main .block-container {{
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(2px);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 215, 0, 0.15);
    }}
    </style>
    """, unsafe_allow_html=True)
except:
    pass

# Page configuration
st.set_page_config(
    page_title="My Contributions - Indian Culture Explorer",
    page_icon="📝",
    layout="wide"
)

# Get translations
translations = get_translations(st.session_state.selected_language)

# Check if user is logged in
if not is_logged_in():
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
    ">
        <h1 style="color: white; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">
            📝 Login Required
        </h1>
        <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.9;">
            Please login to view your contributions
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Show auth sidebar
    with st.sidebar:
        auth_sidebar()
    
    st.stop()

# Get current user
current_user = get_current_user()
username = current_user.get('username', 'Unknown') if current_user else 'Unknown'

# Page header
st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
">
    <h1 style="color: white; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        📝 My Contributions
    </h1>
    <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.9;">
        Welcome {username}! Here are all your cultural contributions
    </p>
</div>
""", unsafe_allow_html=True)

# Load all data and filter by current user
data = load_corpus_data()
user_contributions = [item for item in data if item.get('contributor') == username]

# Statistics overview
col1, col2, col3, col4 = st.columns(4)

voice_stories = [item for item in user_contributions if item.get('type') == 'voice_story']
video_traditions = [item for item in user_contributions if item.get('type') == 'video_tradition']
festival_events = [item for item in user_contributions if item.get('type') == 'festival_event']
cultural_facts = [item for item in user_contributions if item.get('type') == 'cultural_fact']

with col1:
    st.markdown(f"""
    <div style="
        background-color: #E8F5E8;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #4CAF50;
    ">
        <h3 style="margin: 0; color: #2E7D32;">🎙️ Voice Stories</h3>
        <h2 style="margin: 0.5rem 0 0 0; color: #1B5E20;">{len(voice_stories)}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="
        background-color: #E3F2FD;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #2196F3;
    ">
        <h3 style="margin: 0; color: #1976D2;">📹 Video Traditions</h3>
        <h2 style="margin: 0.5rem 0 0 0; color: #0D47A1;">{len(video_traditions)}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="
        background-color: #FFF3E0;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #FF9800;
    ">
        <h3 style="margin: 0; color: #F57C00;">🎊 Festival Events</h3>
        <h2 style="margin: 0.5rem 0 0 0; color: #E65100;">{len(festival_events)}</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="
        background-color: #F3E5F5;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #9C27B0;
    ">
        <h3 style="margin: 0; color: #7B1FA2;">💡 Cultural Facts</h3>
        <h2 style="margin: 0.5rem 0 0 0; color: #4A148C;">{len(cultural_facts)}</h2>
    </div>
    """, unsafe_allow_html=True)

if not user_contributions:
    st.info("🌟 You haven't made any contributions yet! Visit other pages to start sharing your cultural knowledge.")
    st.stop()

# Filter and sorting options
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    content_filter = st.selectbox(
        "Filter by Type:",
        ["All", "Voice Stories", "Video Traditions", "Festival Events", "Cultural Facts"]
    )

with col2:
    sort_by = st.selectbox(
        "Sort by:",
        ["Recent First", "Oldest First", "Quality Score", "Title A-Z"]
    )

with col3:
    items_per_page = st.selectbox(
        "Items per page:",
        [5, 10, 20, 50]
    )

# Filter contributions
filtered_contributions = user_contributions.copy()

if content_filter == "Voice Stories":
    filtered_contributions = voice_stories
elif content_filter == "Video Traditions":
    filtered_contributions = video_traditions
elif content_filter == "Festival Events":
    filtered_contributions = festival_events
elif content_filter == "Cultural Facts":
    filtered_contributions = cultural_facts

# Sort contributions
if sort_by == "Recent First":
    filtered_contributions.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
elif sort_by == "Oldest First":
    filtered_contributions.sort(key=lambda x: x.get('timestamp', ''))
elif sort_by == "Quality Score":
    filtered_contributions.sort(key=lambda x: x.get('quality_score', 0), reverse=True)
elif sort_by == "Title A-Z":
    filtered_contributions.sort(key=lambda x: x.get('title', x.get('content', '')).lower())

# Pagination
total_items = len(filtered_contributions)
total_pages = (total_items + items_per_page - 1) // items_per_page

if total_pages > 1:
    page = st.selectbox(f"Page (1-{total_pages}):", range(1, total_pages + 1))
    start_idx = (page - 1) * items_per_page
    end_idx = min(start_idx + items_per_page, total_items)
    page_contributions = filtered_contributions[start_idx:end_idx]
else:
    page_contributions = filtered_contributions

# Display contributions
st.markdown("---")
st.markdown(f"### 📚 Your Contributions ({len(filtered_contributions)} items)")

for item in page_contributions:
    item_type = item.get('type', 'unknown')
    timestamp = item.get('timestamp', '')
    
    # Parse timestamp for display
    try:
        dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        formatted_date = dt.strftime('%Y-%m-%d %H:%M')
    except:
        formatted_date = timestamp

    # Different display based on type
    if item_type == 'voice_story':
        with st.expander(f"🎙️ Voice Story: {item.get('title', 'Untitled')} - {formatted_date}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"**Title:** {item.get('title', 'Untitled')}")
                st.markdown(f"**Category:** {item.get('category', 'Unknown')}")
                st.markdown(f"**Region:** {item.get('region', 'Unknown')}")
                st.markdown(f"**Language:** {item.get('recording_language', 'Unknown')}")
                st.markdown(f"**Description:** {item.get('description', '')}")
                if item.get('transcription'):
                    st.markdown("**Story Text:**")
                    st.write(item.get('transcription'))
                if item.get('significance'):
                    st.markdown(f"**Cultural Significance:** {item.get('significance')}")
            with col2:
                st.markdown(f"**Quality Score:** {item.get('quality_score', 'N/A')}")
                if item.get('has_audio'):
                    st.markdown("🎧 **Audio Available**")
                    st.markdown(f"*File: {item.get('audio_filename', 'Unknown')}*")

    elif item_type == 'video_tradition':
        with st.expander(f"📹 Video: {item.get('title', 'Untitled')} - {formatted_date}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"**Title:** {item.get('title', 'Untitled')}")
                st.markdown(f"**Category:** {item.get('category', 'Unknown')}")
                st.markdown(f"**Region:** {item.get('region', 'Unknown')}")
                if item.get('state'):
                    st.markdown(f"**Location:** {item.get('state')}")
                st.markdown(f"**Description:** {item.get('description', '')}")
                if item.get('cultural_context'):
                    st.markdown(f"**Cultural Context:** {item.get('cultural_context')}")
                if item.get('participants_info'):
                    st.markdown(f"**Participants:** {item.get('participants_info')}")
            with col2:
                st.markdown(f"**Quality Score:** {item.get('quality_score', 'N/A')}")
                st.markdown(f"**Duration:** {item.get('duration', 'Unknown')}")
                st.markdown(f"**Language:** {item.get('video_language', 'Unknown')}")
                st.markdown(f"**File Size:** {item.get('video_size_mb', 0)}MB")
                st.markdown(f"**Privacy:** {item.get('privacy_level', 'Unknown')}")

    elif item_type == 'festival_event':
        with st.expander(f"🎊 Festival: {item.get('name', 'Untitled')} - {formatted_date}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"**Festival Name:** {item.get('name', 'Untitled')}")
                st.markdown(f"**Category:** {item.get('category', 'Unknown')}")
                st.markdown(f"**Region:** {item.get('region', 'Unknown')}")
                if item.get('months'):
                    st.markdown(f"**Celebration Months:** {', '.join(item.get('months', []))}")
                st.markdown(f"**Description:** {item.get('description', '')}")
                if item.get('traditions'):
                    st.markdown(f"**Traditions:** {item.get('traditions')}")
                if item.get('foods'):
                    st.markdown(f"**Traditional Foods:** {item.get('foods')}")
                if item.get('significance'):
                    st.markdown(f"**Cultural Significance:** {item.get('significance')}")
            with col2:
                st.markdown(f"**Quality Score:** {item.get('quality_score', 'N/A')}")

    elif item_type == 'cultural_fact':
        with st.expander(f"💡 Cultural Fact: {item.get('category', 'General')} - {formatted_date}"):
            st.markdown(f"**Category:** {item.get('category', 'Unknown')}")
            st.markdown(f"**Content:** {item.get('content', '')}")
            st.markdown(f"**Quality Score:** {item.get('quality_score', 'N/A')}")

# Export options
st.markdown("---")
st.markdown("### 📊 Export Your Data")

col1, col2 = st.columns(2)

with col1:
    if st.button("📄 Export as JSON", use_container_width=True):
        import json
        export_data = {
            'username': username,
            'export_date': datetime.now().isoformat(),
            'total_contributions': len(user_contributions),
            'contributions': user_contributions
        }
        json_str = json.dumps(export_data, indent=2, ensure_ascii=False)
        st.download_button(
            label="Download JSON File",
            data=json_str,
            file_name=f"{username}_contributions_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )

with col2:
    if st.button("📊 Export Summary as Text", use_container_width=True):
        summary_text = f"""
Cultural Contributions Summary
Username: {username}
Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}

Statistics:
- Voice Stories: {len(voice_stories)}
- Video Traditions: {len(video_traditions)}
- Festival Events: {len(festival_events)}
- Cultural Facts: {len(cultural_facts)}
- Total Contributions: {len(user_contributions)}

Detailed Contributions:
"""
        for i, item in enumerate(user_contributions, 1):
            item_type = item.get('type', 'unknown')
            title = item.get('title', item.get('name', item.get('content', '')[:50]))
            summary_text += f"\n{i}. {item_type.title()}: {title}\n   Date: {item.get('timestamp', 'Unknown')}\n   Quality Score: {item.get('quality_score', 'N/A')}\n"
        
        st.download_button(
            label="Download Summary",
            data=summary_text,
            file_name=f"{username}_summary_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )

# Footer with user profile info
st.markdown("---")
if current_user:
    st.markdown(f"""
    <div style="
        background-color: #F8F9FA;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #DEE2E6;
    ">
        <h4>👤 User Profile</h4>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Email:</strong> {current_user.get('email', 'Not provided')}</p>
        <p><strong>Region:</strong> {current_user.get('region', 'Not specified')}</p>
        <p><strong>Member since:</strong> {current_user.get('registration_date', 'Unknown')[:10]}</p>
        <p><strong>Total Contributions:</strong> {current_user.get('contributions_count', 0)}</p>
    </div>
    """, unsafe_allow_html=True)