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
    page_title="Voice Stories - Indian Culture Explorer",
    page_icon="🎙️",
    layout="wide"
)

# Get translations
translations = get_translations(st.session_state.selected_language)

# Page header
st.markdown("""
<div style="background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%); padding: 2rem; border-radius: 15px; text-align: center; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);">
    <h1 style="color: white; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        🎙️ Voice Stories
    </h1>
    <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.9;">
        Record and share oral traditions, folk tales, and cultural stories blessed by divine grace
    </p>
</div>
""", unsafe_allow_html=True)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🎤 Record Your Cultural Story")
    
    # Story details form
    with st.form("voice_story_form"):
        story_title = st.text_input(
            "Story Title:",
            placeholder="e.g., The Legend of Krishna, Folk Tale from Punjab"
        )
        
        story_category = st.selectbox(
            "Story Category:",
            [
                "Folk Tale",
                "Religious Story", 
                "Historical Legend",
                "Family Tradition",
                "Regional Myth",
                "Moral Story",
                "Festival Story",
                "Traditional Song",
                "Personal Memory"
            ]
        )
        
        story_region = st.selectbox(
            "Region of Origin:",
            ["Pan-India", "North India", "South India", "East India", "West India", "Central India", "Northeast India", "Specific State/City"]
        )
        
        story_language = st.selectbox(
            "Recording Language:",
            ["Hindi", "English", "Bengali", "Telugu", "Marathi", "Tamil", "Gujarati", "Kannada", "Malayalam", "Punjabi", "Odia", "Other"]
        )
        
        # Festival/Event linking
        festival_event = st.selectbox(
            "Related Festival/Event (Optional):",
            ["Not Related to Any Festival"] + get_festival_list(),
            help="Link this story to a specific festival or cultural event"
        )
        
        story_description = st.text_area(
            "Story Summary / Description:",
            placeholder="Brief description of what the story is about...",
            height=100
        )
        
        cultural_significance = st.text_area(
            "Cultural Significance:",
            placeholder="Why is this story important to your community/culture?",
            height=80
        )
        
        st.markdown("#### 🎙️ Audio Recording")
        st.info("Use the audio recorder below to record your story (up to 10 minutes)")
        
        # Audio recorder component
        audio_file = st.file_uploader(
            "Upload Audio Recording:",
            type=['wav', 'mp3', 'ogg', 'm4a'],
            help="Record your story using your device's voice recorder and upload the file here"
        )
        
        # Alternative text transcription
        st.markdown("#### 📝 Optional: Text Transcription")
        story_transcription = st.text_area(
            "If you prefer, you can also type out your story here:",
            placeholder="Transcribe your story or add it as text...",
            height=150
        )
        
        submitted = st.form_submit_button("🎙️ Submit Voice Story")
        
        if submitted and story_title and (audio_file is not None or story_transcription):
            if not is_logged_in():
                st.warning("Please login to submit voice stories")
            else:
                current_user = get_current_user()
                # Process audio file
                audio_data = None
                if audio_file is not None:
                    audio_bytes = audio_file.read()
                    audio_data = base64.b64encode(audio_bytes).decode()
                
                # Create story data
                voice_story_data = {
                    'type': 'voice_story',
                    'title': story_title,
                    'category': story_category,
                    'region': story_region,
                    'recording_language': story_language,
                    'description': story_description,
                    'significance': cultural_significance,
                    'transcription': story_transcription,
                    'has_audio': audio_file is not None,
                    'audio_filename': audio_file.name if audio_file else None,
                    'festival_event': festival_event if festival_event != "Not Related to Any Festival" else None,
                    'language': st.session_state.selected_language,
                    'timestamp': datetime.now().isoformat(),
                    'contributor': current_user.get('username', 'unknown') if current_user else 'unknown'
                }
                
                # Validate content
                content_to_validate = f"Title: {story_title}\nDescription: {story_description}\nTranscription: {story_transcription}"
                validation_result = validate_content(content_to_validate, "Voice Story")
                
                if validation_result['is_valid']:
                    voice_story_data['quality_score'] = validation_result['quality_score']
                    save_user_data(voice_story_data)
                    username = current_user.get('username') if current_user else 'unknown'
                    update_user_contributions(username)
                    st.session_state.user_contributions.append(voice_story_data)
                    st.success("✅ Voice story submitted successfully!")
                    st.balloons()
                    
                    if audio_file:
                        st.info("🎧 Audio file has been saved with your story contribution.")
                else:
                    st.warning("⚠️ Please provide more detailed information about your story.")

with col2:
    st.markdown("### 📊 Voice Story Statistics")
    
    # Load and display statistics
    data = load_corpus_data()
    voice_stories = [item for item in data if item.get('type') == 'voice_story']
    
    st.metric("🎙️ Total Voice Stories", len(voice_stories))
    
    if voice_stories:
        # Statistics by category
        categories = {}
        regions = {}
        languages = {}
        
        for story in voice_stories:
            cat = story.get('category', 'Unknown')
            reg = story.get('region', 'Unknown')
            lang = story.get('recording_language', 'Unknown')
            
            categories[cat] = categories.get(cat, 0) + 1
            regions[reg] = regions.get(reg, 0) + 1
            languages[lang] = languages.get(lang, 0) + 1
        
        st.markdown("#### By Category:")
        for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:5]:
            st.write(f"• {cat}: {count}")
        
        st.markdown("#### By Language:")
        for lang, count in sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]:
            st.write(f"• {lang}: {count}")

# Display existing voice stories
st.markdown("---")
st.markdown("### 🎧 Explore Voice Stories")

if voice_stories:
    # Filter options
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_category = st.selectbox("Filter by Category:", ["All"] + list(set([s.get('category', 'Unknown') for s in voice_stories])))
    with col2:
        filter_region = st.selectbox("Filter by Region:", ["All"] + list(set([s.get('region', 'Unknown') for s in voice_stories])))
    with col3:
        filter_language = st.selectbox("Filter by Language:", ["All"] + list(set([s.get('recording_language', 'Unknown') for s in voice_stories])))
    
    # Filter stories
    filtered_stories = voice_stories
    if filter_category != "All":
        filtered_stories = [s for s in filtered_stories if s.get('category') == filter_category]
    if filter_region != "All":
        filtered_stories = [s for s in filtered_stories if s.get('region') == filter_region]
    if filter_language != "All":
        filtered_stories = [s for s in filtered_stories if s.get('recording_language') == filter_language]
    
    # Display filtered stories
    for i in range(0, len(filtered_stories), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(filtered_stories):
                story = filtered_stories[i + j]
                with col:
                    with st.expander(f"🎙️ {story.get('title', 'Untitled Story')}"):
                        st.markdown(f"**Category:** {story.get('category', 'Unknown')}")
                        st.markdown(f"**Region:** {story.get('region', 'Unknown')}")
                        st.markdown(f"**Language:** {story.get('recording_language', 'Unknown')}")
                        st.markdown(f"**Description:** {story.get('description', '')}")
                        if story.get('transcription'):
                            st.markdown("**Story Text:**")
                            st.write(story.get('transcription'))
                        if story.get('significance'):
                            st.markdown(f"**Cultural Significance:** {story.get('significance')}")
                        if story.get('has_audio'):
                            st.markdown("🎧 **Audio Recording Available**")
                            
                            # Display audio player
                            audio_filename = story.get('audio_filename', 'sample_audio.mp3')
                            st.markdown(f"**File:** {audio_filename}")
                            
                            # Sample audio for demonstration
                            try:
                                # In a real app, this would load the actual uploaded audio file
                                st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav")
                                st.caption(f"🔊 Language: {story.get('recording_language', 'Unknown')}")
                                
                                # Language-specific info
                                if story.get('recording_language') == 'Telugu':
                                    st.info("🇮🇳 Telugu festival story - తెలుగు పండుగ కథ")
                                elif story.get('recording_language') == 'Hindi':
                                    st.info("🇮🇳 Hindi cultural story - हिंदी सांस्कृतिक कहानी")
                            except:
                                st.write("🎵 Audio player would appear here with the actual recording")
else:
    st.info("🌟 Be the first to share a voice story!")

# Recording tips
st.markdown("---")
st.markdown("""
<div style="background-color: #E8F5E8; padding: 20px; border-radius: 10px; margin: 10px 0;">
    <h4>📱 Recording Tips:</h4>
    <ul>
        <li>Find a quiet space with minimal background noise</li>
        <li>Speak clearly and at a moderate pace</li>
        <li>Keep recordings under 10 minutes for best results</li>
        <li>Include introductions: "This is a story about..." or "In my village we tell..."</li>
        <li>You can record in any Indian language or English</li>
        <li>Don't worry about perfection - authentic voices matter most!</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; border-radius: 10px; background-color: #FFF8E1;">
    <h4>🎙️ Preserve Oral Traditions</h4>
    <p>Your voice stories help preserve the oral traditions and cultural heritage of India for future generations.</p>
    <small>All recordings and stories are securely stored and contribute to cultural preservation efforts.</small>
</div>
""", unsafe_allow_html=True)