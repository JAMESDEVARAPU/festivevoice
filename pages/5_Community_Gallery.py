import streamlit as st
import json
from datetime import datetime
from utils.data_manager import load_corpus_data
from utils.theming import apply_chatgpt_theme
from utils.translations import get_translations
from utils.auth import auth_sidebar

# Initialize session state
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = 'light'
if 'selected_language' not in st.session_state:
    st.session_state.selected_language = 'English'

# Apply ChatGPT-style theming
apply_chatgpt_theme(st.session_state.theme_mode)

# Page configuration
st.set_page_config(
    page_title="Community Gallery - Indian Culture Explorer",
    page_icon="🖼️",
    layout="wide"
)

# Get translations
translations = get_translations(st.session_state.selected_language)

# Page header
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(255, 107, 53, 0.95) 0%, rgba(247, 147, 30, 0.95) 100%);
    background-image: 
        radial-gradient(circle at 25% 25%, rgba(255, 215, 0, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 75% 75%, rgba(255, 165, 0, 0.1) 0%, transparent 45%);
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
        top: 8px;
        left: 15px;
        right: 15px;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.4), transparent);
    "></div>
    <div style="
        position: absolute;
        bottom: 8px;
        left: 15px;
        right: 15px;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.4), transparent);
    "></div>
    
    <div style="position: relative; z-index: 2;">
        <h1 style="color: white; margin: 0; text-shadow: 0 2px 6px rgba(0,0,0,0.3);">
            🖼️ Community Gallery
        </h1>
        <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.95; text-shadow: 0 1px 3px rgba(0,0,0,0.3);">
            Explore cultural contributions blessed by the divine community
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar for authentication
with st.sidebar:
    auth_sidebar()

# Load all data
data = load_corpus_data()

if not data:
    st.info("🌟 No content has been uploaded yet. Be the first to contribute!")
    st.stop()

# Content statistics overview
col1, col2, col3, col4 = st.columns(4)

voice_stories = [item for item in data if item.get('type') == 'voice_story']
video_traditions = [item for item in data if item.get('type') == 'video_tradition']
festival_events = [item for item in data if item.get('type') == 'festival_event']
cultural_stories = [item for item in data if item.get('type') == 'cultural_story']

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
        <h3 style="margin: 0; color: #7B1FA2;">📚 Cultural Stories</h3>
        <h2 style="margin: 0.5rem 0 0 0; color: #4A148C;">{len(cultural_stories)}</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Filter and search options
st.markdown("### 🔍 Explore Community Content")

col1, col2, col3, col4 = st.columns(4)

with col1:
    content_type = st.selectbox(
        "Content Type:",
        ["All", "Voice Stories", "Video Traditions", "Festival Events", "Cultural Stories"]
    )

with col2:
    # Get unique contributors
    contributors = list(set([item.get('contributor', 'Unknown') for item in data if item.get('contributor')]))
    contributor_filter = st.selectbox(
        "Contributor:",
        ["All"] + sorted(contributors)
    )

with col3:
    # Get unique regions
    regions = list(set([item.get('region', 'Unknown') for item in data if item.get('region')]))
    region_filter = st.selectbox(
        "Region:",
        ["All"] + sorted(regions)
    )

with col4:
    sort_by = st.selectbox(
        "Sort by:",
        ["Recent First", "Oldest First", "Quality Score", "Contributor A-Z"]
    )

# Search functionality
search_term = st.text_input("🔍 Search content by title, description, or keywords:")

# Filter data based on selections
filtered_data = data.copy()

# Filter by content type
if content_type == "Voice Stories":
    filtered_data = voice_stories
elif content_type == "Video Traditions":
    filtered_data = video_traditions
elif content_type == "Festival Events":
    filtered_data = festival_events
elif content_type == "Cultural Stories":
    filtered_data = cultural_stories

# Filter by contributor
if contributor_filter != "All":
    filtered_data = [item for item in filtered_data if item.get('contributor') == contributor_filter]

# Filter by region
if region_filter != "All":
    filtered_data = [item for item in filtered_data if item.get('region') == region_filter]

# Filter by search term
if search_term:
    search_lower = search_term.lower()
    filtered_data = [
        item for item in filtered_data
        if search_lower in item.get('title', '').lower() or
           search_lower in item.get('name', '').lower() or
           search_lower in item.get('description', '').lower() or
           search_lower in item.get('content', '').lower()
    ]

# Sort data
if sort_by == "Recent First":
    filtered_data.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
elif sort_by == "Oldest First":
    filtered_data.sort(key=lambda x: x.get('timestamp', ''))
elif sort_by == "Quality Score":
    filtered_data.sort(key=lambda x: x.get('quality_score', 0), reverse=True)
elif sort_by == "Contributor A-Z":
    filtered_data.sort(key=lambda x: x.get('contributor', 'Unknown').lower())

# Pagination
items_per_page = 10
total_items = len(filtered_data)
total_pages = (total_items + items_per_page - 1) // items_per_page

if total_items == 0:
    st.info("No content matches your search criteria. Try adjusting the filters.")
    st.stop()

st.markdown(f"**Found {total_items} items**")

if total_pages > 1:
    page = st.selectbox(f"Page (1-{total_pages}):", range(1, total_pages + 1))
    start_idx = (page - 1) * items_per_page
    end_idx = min(start_idx + items_per_page, total_items)
    page_data = filtered_data[start_idx:end_idx]
else:
    page_data = filtered_data

# Display content
st.markdown("---")

for item in page_data:
    item_type = item.get('type', 'unknown')
    contributor = item.get('contributor', 'Unknown')
    timestamp = item.get('timestamp', '')
    
    # Parse timestamp for display
    try:
        dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        formatted_date = dt.strftime('%Y-%m-%d %H:%M')
    except:
        formatted_date = timestamp

    # Display based on content type
    if item_type == 'voice_story':
        with st.container():
            st.markdown(f"""
            <div style="
                background-color: #F8F9FA;
                padding: 1.5rem;
                border-radius: 10px;
                margin-bottom: 1rem;
                border-left: 4px solid #4CAF50;
            ">
                <h4 style="margin: 0 0 0.5rem 0; color: #2E7D32;">
                    🎙️ {item.get('title', 'Untitled Voice Story')}
                </h4>
                <p style="margin: 0; color: #666; font-size: 0.9em;">
                    By {contributor} • {formatted_date} • {item.get('region', 'Unknown')}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**Category:** {item.get('category', 'Unknown')}")
                st.markdown(f"**Language:** {item.get('recording_language', 'Unknown')}")
                st.markdown(f"**Description:** {item.get('description', '')}")
                if item.get('transcription'):
                    with st.expander("📝 Story Transcription"):
                        st.write(item.get('transcription'))
                if item.get('significance'):
                    st.markdown(f"**Cultural Significance:** {item.get('significance')}")
            
            with col2:
                if item.get('quality_score'):
                    st.metric("Quality Score", f"{item.get('quality_score')}/5")
                if item.get('has_audio'):
                    st.info("🎧 Audio Available")

    elif item_type == 'video_tradition':
        with st.container():
            st.markdown(f"""
            <div style="
                background-color: #F8F9FA;
                padding: 1.5rem;
                border-radius: 10px;
                margin-bottom: 1rem;
                border-left: 4px solid #2196F3;
            ">
                <h4 style="margin: 0 0 0.5rem 0; color: #1976D2;">
                    📹 {item.get('title', 'Untitled Video')}
                </h4>
                <p style="margin: 0; color: #666; font-size: 0.9em;">
                    By {contributor} • {formatted_date} • {item.get('region', 'Unknown')}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**Category:** {item.get('category', 'Unknown')}")
                st.markdown(f"**Description:** {item.get('description', '')}")
                if item.get('cultural_context'):
                    st.markdown(f"**Cultural Context:** {item.get('cultural_context')}")
                if item.get('participants_info'):
                    st.markdown(f"**Participants:** {item.get('participants_info')}")
            
            with col2:
                if item.get('quality_score'):
                    st.metric("Quality Score", f"{item.get('quality_score')}/5")
                st.markdown(f"**Duration:** {item.get('duration', 'Unknown')}")
                st.markdown(f"**Language:** {item.get('video_language', 'Unknown')}")
                st.markdown(f"**Size:** {item.get('video_size_mb', 0)}MB")

    elif item_type == 'festival_event':
        with st.container():
            st.markdown(f"""
            <div style="
                background-color: #F8F9FA;
                padding: 1.5rem;
                border-radius: 10px;
                margin-bottom: 1rem;
                border-left: 4px solid #FF9800;
            ">
                <h4 style="margin: 0 0 0.5rem 0; color: #F57C00;">
                    🎊 {item.get('name', 'Untitled Festival')}
                </h4>
                <p style="margin: 0; color: #666; font-size: 0.9em;">
                    By {contributor} • {formatted_date} • {item.get('region', 'Unknown')}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**Category:** {item.get('category', 'Unknown')}")
                if item.get('months'):
                    st.markdown(f"**Celebration Months:** {', '.join(item.get('months', []))}")
                st.markdown(f"**Description:** {item.get('description', '')}")
                if item.get('traditions'):
                    st.markdown(f"**Traditions:** {item.get('traditions')}")
                if item.get('foods'):
                    st.markdown(f"**Traditional Foods:** {item.get('foods')}")
                if item.get('significance'):
                    st.markdown(f"**Significance:** {item.get('significance')}")
            
            with col2:
                if item.get('quality_score'):
                    st.metric("Quality Score", f"{item.get('quality_score')}/5")

    elif item_type == 'cultural_story':
        with st.container():
            st.markdown(f"""
            <div style="
                background-color: #F8F9FA;
                padding: 1.5rem;
                border-radius: 10px;
                margin-bottom: 1rem;
                border-left: 4px solid #9C27B0;
            ">
                <h4 style="margin: 0 0 0.5rem 0; color: #7B1FA2;">
                    📚 {item.get('title', 'Untitled Story')}
                </h4>
                <p style="margin: 0; color: #666; font-size: 0.9em;">
                    By {contributor} • {formatted_date} • {item.get('region', 'Unknown')}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**Category:** {item.get('category', 'Unknown')}")
                st.markdown(f"**Language:** {item.get('original_language', 'Unknown')}")
                content_preview = item.get('content', '')[:300]
                st.markdown(f"**Story:** {content_preview}{'...' if len(item.get('content', '')) > 300 else ''}")
                if item.get('moral_lesson'):
                    st.markdown(f"**Moral:** {item.get('moral_lesson')}")
            
            with col2:
                if item.get('quality_score'):
                    st.metric("Quality Score", f"{item.get('quality_score')}/5")
                st.markdown(f"**Audience:** {item.get('audience_age', 'All ages')}")

    st.markdown("---")

# Contributors section
st.markdown("### 👥 Top Contributors")

# Count contributions by user
contributor_counts = {}
for item in data:
    contributor = item.get('contributor', 'Unknown')
    if contributor != 'Unknown':
        contributor_counts[contributor] = contributor_counts.get(contributor, 0) + 1

if contributor_counts:
    # Sort by contribution count
    sorted_contributors = sorted(contributor_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Display top 10 contributors
    cols = st.columns(5)
    for i, (contributor, count) in enumerate(sorted_contributors[:10]):
        with cols[i % 5]:
            st.markdown(f"""
            <div style="
                background-color: #F8F9FA;
                padding: 1rem;
                border-radius: 8px;
                text-align: center;
                border: 1px solid #DEE2E6;
            ">
                <h4 style="margin: 0; color: #495057;">{contributor}</h4>
                <p style="margin: 0.5rem 0 0 0; color: #6C757D;">{count} contributions</p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; border-radius: 10px; background-color: #FFF8E1;">
    <h4>🤝 Community Cultural Preservation</h4>
    <p>Together, we're building a comprehensive archive of India's rich cultural heritage.</p>
    <small>All content is contributed and validated by community members.</small>
</div>
""", unsafe_allow_html=True)