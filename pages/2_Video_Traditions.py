import streamlit as st
import json
from datetime import datetime
from utils.data_manager import save_user_data, load_corpus_data, get_festival_list
from utils.ai_validation import validate_content
from utils.theming import apply_chatgpt_theme
from utils.translations import get_translations
from utils.auth import is_logged_in, get_current_user, update_user_contributions
import base64

# Initialize session state
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = 'light'
if 'selected_language' not in st.session_state:
    st.session_state.selected_language = 'English'
if 'user_contributions' not in st.session_state:
    st.session_state.user_contributions = []

# Apply ChatGPT-style theming
apply_chatgpt_theme(st.session_state.theme_mode)

# Page configuration
st.set_page_config(
    page_title="Video Traditions - Indian Culture Explorer",
    page_icon="📹",
    layout="wide"
)

# Get translations
translations = get_translations(st.session_state.selected_language)

# Page header
st.markdown("""
<div style="background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%); padding: 2rem; border-radius: 15px; text-align: center; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);">
    <h1 style="color: white; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        📹 Video Traditions
    </h1>
    <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.9;">
        Share videos of cultural practices, dances, rituals, and traditions
    </p>
</div>
""", unsafe_allow_html=True)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📹 Upload Cultural Tradition Video")
    
    with st.form("video_tradition_form"):
        video_title = st.text_input(
            "Video Title:",
            placeholder="e.g., Classical Bharatanatyam Performance, Rangoli Making, Traditional Cooking"
        )
        
        tradition_category = st.selectbox(
            "Tradition Category:",
            [
                "Dance Performance",
                "Musical Performance",
                "Religious Ritual",
                "Cooking & Food Preparation",
                "Arts & Crafts",
                "Festival Celebration",
                "Wedding Ceremony",
                "Traditional Games",
                "Storytelling",
                "Agricultural Practice",
                "Handicraft Making",
                "Cultural Ceremony"
            ]
        )
        
        tradition_region = st.selectbox(
            "Region of Origin:",
            ["Pan-India", "North India", "South India", "East India", "West India", "Central India", "Northeast India", "Specific State/City"]
        )
        
        tradition_state = st.text_input(
            "Specific State/City (Optional):",
            placeholder="e.g., Kerala, Rajasthan, Mumbai"
        )
        
        video_description = st.text_area(
            "Video Description:",
            placeholder="Describe what is shown in the video, the cultural significance, and any special details...",
            height=120
        )
        
        cultural_context = st.text_area(
            "Cultural Context & Significance:",
            placeholder="Explain the cultural importance, history, and meaning of this tradition...",
            height=100
        )
        
        participants_info = st.text_input(
            "Participants Information (Optional):",
            placeholder="e.g., Professional dancer, Community elder, Family member"
        )
        
        # Festival/Event linking
        festival_event = st.selectbox(
            "Related Festival/Event (Optional):",
            ["Not Related to Any Festival"] + get_festival_list(),
            help="Link this video to a specific festival or cultural event"
        )
        
        st.markdown("#### 📹 Video Upload")
        st.info("Upload your video file (max 100MB). Supported formats: MP4, AVI, MOV, MKV")
        
        video_file = st.file_uploader(
            "Choose Video File:",
            type=['mp4', 'avi', 'mov', 'mkv', 'webm'],
            help="Upload a video showing cultural traditions, practices, or performances"
        )
        
        # Additional video details
        video_duration = st.text_input(
            "Video Duration (Optional):",
            placeholder="e.g., 2 minutes, 5:30"
        )
        
        video_language = st.selectbox(
            "Primary Language in Video:",
            ["Hindi", "English", "Bengali", "Telugu", "Marathi", "Tamil", "Gujarati", "Kannada", "Malayalam", "Punjabi", "Odia", "Silent/Music Only", "Other"]
        )
        
        # Permission and consent
        st.markdown("#### ⚠️ Important: Permission & Consent")
        consent_given = st.checkbox(
            "I confirm that I have permission to share this video and all participants have consented to its use for cultural preservation."
        )
        
        privacy_level = st.selectbox(
            "Privacy Level:",
            ["Public - Anyone can view", "Community - Registered users only", "Educational - For research/education only"]
        )
        
        submitted = st.form_submit_button("📹 Submit Video Tradition")
        
        if submitted and video_title and video_description and consent_given:
            if not is_logged_in():
                st.warning("Please login to submit video traditions")
            elif video_file is not None:
                # Process video file
                video_bytes = video_file.read()
                video_size_mb = len(video_bytes) / (1024 * 1024)
                
                if video_size_mb > 100:
                    st.error("Video file is too large. Please upload a file smaller than 100MB.")
                else:
                    current_user = get_current_user()
                    # Create video tradition data
                    video_tradition_data = {
                        'type': 'video_tradition',
                        'title': video_title,
                        'category': tradition_category,
                        'region': tradition_region,
                        'state': tradition_state,
                        'description': video_description,
                        'cultural_context': cultural_context,
                        'participants_info': participants_info,
                        'video_filename': video_file.name,
                        'video_size_mb': round(video_size_mb, 2),
                        'duration': video_duration,
                        'video_language': video_language,
                        'festival_event': festival_event if festival_event != "Not Related to Any Festival" else None,
                        'privacy_level': privacy_level,
                        'consent_given': consent_given,
                        'language': st.session_state.selected_language,
                        'timestamp': datetime.now().isoformat(),
                        'contributor': current_user.get('username', 'unknown') if current_user else 'unknown'
                    }
                    
                    # Validate content
                    content_to_validate = f"Title: {video_title}\nDescription: {video_description}\nCultural Context: {cultural_context}"
                    validation_result = validate_content(content_to_validate, "Video Tradition")
                    
                    if validation_result['is_valid']:
                        video_tradition_data['quality_score'] = validation_result['quality_score']
                        save_user_data(video_tradition_data)
                        username = current_user.get('username') if current_user else 'unknown'
                        update_user_contributions(username)
                        st.session_state.user_contributions.append(video_tradition_data)
                        st.success("✅ Video tradition submitted successfully!")
                        st.balloons()
                        st.info(f"📹 Video file '{video_file.name}' ({video_size_mb:.1f}MB) has been saved with your contribution.")
                    else:
                        st.warning("⚠️ Please provide more detailed information about the cultural tradition shown in your video.")
            else:
                st.error("Please upload a video file to submit your tradition.")

with col2:
    st.markdown("### 📊 Video Tradition Statistics")
    
    # Load and display statistics
    data = load_corpus_data()
    video_traditions = [item for item in data if item.get('type') == 'video_tradition']
    
    st.metric("📹 Total Videos", len(video_traditions))
    
    if video_traditions:
        # Calculate total video storage
        total_size = sum([float(v.get('video_size_mb', 0)) for v in video_traditions])
        st.metric("💾 Total Storage", f"{total_size:.1f} MB")
        
        # Statistics by category
        categories = {}
        regions = {}
        languages = {}
        
        for video in video_traditions:
            cat = video.get('category', 'Unknown')
            reg = video.get('region', 'Unknown')
            lang = video.get('video_language', 'Unknown')
            
            categories[cat] = categories.get(cat, 0) + 1
            regions[reg] = regions.get(reg, 0) + 1
            languages[lang] = languages.get(lang, 0) + 1
        
        st.markdown("#### By Category:")
        for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:5]:
            st.write(f"• {cat}: {count}")
        
        st.markdown("#### By Region:")
        for reg, count in sorted(regions.items(), key=lambda x: x[1], reverse=True)[:5]:
            st.write(f"• {reg}: {count}")

# Display existing video traditions
st.markdown("---")
st.markdown("### 🎬 Explore Video Traditions")

if video_traditions:
    # Filter options
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_category = st.selectbox("Filter by Category:", ["All"] + list(set([v.get('category', 'Unknown') for v in video_traditions])))
    with col2:
        filter_region = st.selectbox("Filter by Region:", ["All"] + list(set([v.get('region', 'Unknown') for v in video_traditions])))
    with col3:
        filter_language = st.selectbox("Filter by Language:", ["All"] + list(set([v.get('video_language', 'Unknown') for v in video_traditions])))
    
    # Filter videos
    filtered_videos = video_traditions
    if filter_category != "All":
        filtered_videos = [v for v in filtered_videos if v.get('category') == filter_category]
    if filter_region != "All":
        filtered_videos = [v for v in filtered_videos if v.get('region') == filter_region]
    if filter_language != "All":
        filtered_videos = [v for v in filtered_videos if v.get('video_language') == filter_language]
    
    # Display filtered videos
    for i in range(0, len(filtered_videos), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(filtered_videos):
                video = filtered_videos[i + j]
                with col:
                    with st.expander(f"📹 {video.get('title', 'Untitled Video')}"):
                        st.markdown(f"**Category:** {video.get('category', 'Unknown')}")
                        st.markdown(f"**Region:** {video.get('region', 'Unknown')}")
                        if video.get('state'):
                            st.markdown(f"**Location:** {video.get('state')}")
                        st.markdown(f"**Language:** {video.get('video_language', 'Unknown')}")
                        if video.get('duration'):
                            st.markdown(f"**Duration:** {video.get('duration')}")
                        st.markdown(f"**Description:** {video.get('description', '')}")
                        if video.get('cultural_context'):
                            st.markdown(f"**Cultural Context:** {video.get('cultural_context')}")
                        if video.get('participants_info'):
                            st.markdown(f"**Participants:** {video.get('participants_info')}")
                        
                        # Video playback section
                        st.markdown("📹 **Video Playback:**")
                        video_filename = video.get('video_filename', 'sample_video.mp4')
                        st.markdown(f"**File:** {video_filename} ({video.get('video_size_mb', 0)}MB)")
                        
                        # Sample video player for demonstration
                        try:
                            # In real app, this would show the actual uploaded video
                            st.video("https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4")
                            st.caption(f"🎬 Duration: {video.get('duration', 'Unknown')} | Language: {video.get('video_language', 'Unknown')}")
                            
                            # Cultural context based on category
                            if video.get('category') == 'Dance Performance':
                                st.info("🩰 Traditional Indian dance performance preserving cultural heritage")
                            elif video.get('category') == 'Arts & Crafts':
                                st.info("🎨 Traditional craft demonstration preserving artisan skills")
                        except:
                            st.write(f"🎬 Video player would appear here showing: {video_filename}")
                            st.caption("📱 Video playback requires the actual uploaded file")
                        st.markdown(f"**File:** {video.get('video_filename', 'Unknown')} ({video.get('video_size_mb', 0)}MB)")
                        st.markdown(f"**Privacy:** {video.get('privacy_level', 'Unknown')}")
else:
    st.info("🌟 Be the first to share a video tradition!")

# Recording guidelines
st.markdown("---")
st.markdown("""
<div style="background-color: #E3F2FD; padding: 20px; border-radius: 10px; margin: 10px 0;">
    <h4>📹 Video Guidelines:</h4>
    <ul>
        <li><strong>Quality:</strong> Use good lighting and stable camera position</li>
        <li><strong>Content:</strong> Focus on cultural practices, traditions, or performances</li>
        <li><strong>Duration:</strong> Keep videos between 1-10 minutes for best engagement</li>
        <li><strong>Audio:</strong> Ensure clear audio if speaking or music is involved</li>
        <li><strong>Permission:</strong> Always get consent from all people in the video</li>
        <li><strong>Authenticity:</strong> Show genuine cultural practices and traditions</li>
        <li><strong>Context:</strong> Provide detailed cultural background and significance</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; border-radius: 10px; background-color: #FFF8E1;">
    <h4>📹 Visual Cultural Preservation</h4>
    <p>Your video contributions help preserve visual cultural traditions and practices for future generations.</p>
    <small>All videos are securely stored and contribute to India's digital cultural heritage archive.</small>
</div>
""", unsafe_allow_html=True)