import streamlit as st
import json
import os
from datetime import datetime
from utils.theming import apply_chatgpt_theme
from utils.data_manager import save_user_data, load_corpus_data, get_data_by_type
from utils.translations import get_translations, SUPPORTED_LANGUAGES
from utils.ai_validation import validate_content
from utils.auth import auth_sidebar, is_logged_in, get_current_user, update_user_contributions

# Page config
st.set_page_config(
    page_title="Festival Images",
    page_icon="🖼️",
    layout="wide"
)

# Initialize session state
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = 'light'
if 'selected_language' not in st.session_state:
    st.session_state.selected_language = 'English'

# Apply theming
apply_chatgpt_theme(st.session_state.theme_mode)

# Check authentication first
if not is_logged_in():
    st.markdown("""
    <div style="
        background-color: #FFF3CD;
        border: 2px solid #FFEAA7;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
    ">
        <h2 style="color: #856404;">🔒 Authentication Required</h2>
        <p style="color: #856404; font-size: 1.1rem;">
            Please login from the main page to access Festival Images
        </p>
        <p style="color: #856404;">
            👈 Use the sidebar to login or register
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# Sidebar
with st.sidebar:
    # Language selection
    selected_lang = st.selectbox(
        "Language",
        options=list(SUPPORTED_LANGUAGES.keys()),
        index=list(SUPPORTED_LANGUAGES.keys()).index(st.session_state.selected_language),
        key="lang_selector_images"
    )
    st.session_state.selected_language = selected_lang
    
    st.markdown("---")
    auth_sidebar()

# Get translations
translations = get_translations(st.session_state.selected_language)

# Page header
st.markdown("""
<div style="background: linear-gradient(135deg, #FF7F50 0%, #FF6B35 100%); padding: 1.5rem; border-radius: 15px; text-align: center; margin-bottom: 2rem;">
    <h1 style="color: white; margin: 0; font-size: 2rem;">🖼️ Festival Images</h1>
    <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.9;">Visual celebrations of Indian festivals and traditions</p>
</div>
""", unsafe_allow_html=True)

# Create tabs for different functionalities
tab1, tab2, tab3 = st.tabs(["📋 Browse Images", "📤 Upload Image", "🎨 Image Gallery"])

with tab1:
    st.subheader("🖼️ Festival Image Collection")
    
    # Load festival images data
    festival_images = get_data_by_type('festival_image')
    
    if festival_images:
        # Filter options
        col1, col2 = st.columns([1, 1])
        
        with col1:
            festivals = list(set([img.get('festival_event', 'Other') for img in festival_images if img.get('festival_event')]))
            selected_festival = st.selectbox("Filter by Festival:", ["All"] + sorted(festivals))
        
        with col2:
            regions = list(set([img.get('region', 'Unknown') for img in festival_images]))
            selected_region = st.selectbox("Filter by Region:", ["All"] + sorted(regions))
        
        # Apply filters
        filtered_images = festival_images
        if selected_festival != "All":
            filtered_images = [img for img in filtered_images if img.get('festival_event') == selected_festival]
        if selected_region != "All":
            filtered_images = [img for img in filtered_images if img.get('region') == selected_region]
        
        st.markdown(f"**Found {len(filtered_images)} images**")
        
        # Display images in grid
        for i in range(0, len(filtered_images), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(filtered_images):
                    img = filtered_images[i + j]
                    with col:
                        st.markdown(f"""
                        <div style="
                            border: 1px solid #ddd;
                            border-radius: 10px;
                            padding: 1rem;
                            margin-bottom: 1rem;
                            background: white;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                        ">
                            <h4 style="margin: 0 0 0.5rem 0; color: #333;">{img.get('title', 'Untitled')}</h4>
                            <p style="color: #666; font-size: 0.9rem; margin: 0.5rem 0;">
                                <strong>Festival:</strong> {img.get('festival_event', 'General')}<br>
                                <strong>Region:</strong> {img.get('region', 'Unknown')}<br>
                                <strong>Type:</strong> {img.get('image_type', 'Photo')}
                            </p>
                            <p style="color: #555; font-size: 0.85rem; margin: 0.5rem 0;">
                                {img.get('description', 'No description available')[:100]}...
                            </p>
                            <small style="color: #888;">
                                Uploaded by: {img.get('contributor', 'Unknown')} | 
                                Quality: {'⭐' * img.get('quality_score', 3)}
                            </small>
                        </div>
                        """, unsafe_allow_html=True)
    else:
        st.info("🖼️ No festival images uploaded yet. Be the first to share festival visuals!")

with tab2:
    st.subheader("📤 Upload Festival Image")
    
    current_user = get_current_user()
    
    with st.form("upload_festival_image"):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            image_title = st.text_input(
                "Image Title *",
                placeholder="e.g., Diwali Rangoli Decoration"
            )
            
            image_description = st.text_area(
                "Description *",
                placeholder="Describe the festival image, its cultural significance, and context...",
                height=100
            )
            
            cultural_context = st.text_area(
                "Cultural Context",
                placeholder="Explain the cultural and religious significance of this image...",
                height=80
            )
        
        with col2:
            festival_event = st.selectbox(
                "Festival/Event *",
                ["Diwali", "Holi", "Navratri", "Ganesh Chaturthi", "Durga Puja", "Dussehra", 
                 "Krishna Janmashtami", "Karva Chauth", "Raksha Bandhan", "Makar Sankranti",
                 "Pongal", "Onam", "Baisakhi", "Ugadi", "Gudi Padwa", "Bihu", "Chhath Puja",
                 "Teej", "Sri Rama Navami", "Maha Shivratri", "Other"]
            )
            
            image_type = st.selectbox(
                "Image Type *",
                ["Decoration", "Ritual", "Food Preparation", "Traditional Dress", 
                 "Arts & Crafts", "Community Celebration", "Temple/Religious Site", 
                 "Folk Performance", "Family Gathering", "Other"]
            )
            
            region = st.selectbox(
                "Region *",
                ["North India", "South India", "East India", "West India", "Central India", "Northeast India", "Pan-India"]
            )
            
            state = st.text_input("State/Territory", placeholder="e.g., Maharashtra, Tamil Nadu")
        
        # Image upload (simulated - in real app this would handle actual file uploads)
        uploaded_file = st.file_uploader(
            "Upload Image File",
            type=['jpg', 'jpeg', 'png', 'gif'],
            help="Upload festival images (max 10MB)"
        )
        
        # Metadata
        col3, col4 = st.columns(2)
        with col3:
            photographer = st.text_input("Photographer/Source", placeholder="Optional: credit the photographer")
        
        with col4:
            image_date = st.date_input("When was this taken?", value=datetime.now().date())
        
        privacy_consent = st.checkbox(
            "I confirm that I have permission to share this image and it respects cultural sensitivities",
            help="Required for image submission"
        )
        
        submitted = st.form_submit_button("Upload Festival Image", type="primary")
        
        if submitted:
            if not all([image_title, image_description, festival_event, image_type, region]):
                st.error("❌ Please fill in all required fields marked with *")
            elif not privacy_consent:
                st.error("❌ Please confirm you have permission to share this image")
            else:
                # Validate content with AI
                content_to_validate = f"{image_title}: {image_description} {cultural_context}"
                validation_result = validate_content(content_to_validate, "Festival Image")
                
                if validation_result['is_valid']:
                    # Save image metadata to corpus
                    username = current_user.get('username', 'unknown') if current_user else 'unknown'
                    
                    image_data = {
                        'type': 'festival_image',
                        'title': image_title,
                        'description': image_description,
                        'cultural_context': cultural_context,
                        'festival_event': festival_event,
                        'image_type': image_type,
                        'region': region,
                        'state': state,
                        'photographer': photographer,
                        'image_date': image_date.isoformat(),
                        'image_filename': f"{image_title.lower().replace(' ', '_')}.jpg" if uploaded_file else "sample_image.jpg",
                        'privacy_consent': privacy_consent,
                        'language': st.session_state.selected_language,
                        'timestamp': datetime.now().isoformat(),
                        'quality_score': validation_result['quality_score'],
                        'contributor': username
                    }
                    
                    if save_user_data(image_data):
                        update_user_contributions(username)
                        st.success("✅ Festival image uploaded successfully!")
                        st.balloons()
                        
                        # Show preview
                        st.markdown("### 🖼️ Image Preview")
                        st.json(image_data)
                    else:
                        st.error("❌ Failed to save image data. Please try again.")
                else:
                    st.warning("⚠️ Please provide more detailed description of the festival image.")

with tab3:
    st.subheader("🎨 Festival Image Gallery")
    
    # Sample festival images with descriptions
    sample_images = [
        {
            'title': 'Diwali Rangoli Art',
            'festival': 'Diwali',
            'description': 'Traditional geometric rangoli patterns made with colored powders',
            'region': 'Pan-India'
        },
        {
            'title': 'Ganesh Visarjan Procession',
            'festival': 'Ganesh Chaturthi',
            'description': 'Community procession carrying Ganesha idols to water bodies',
            'region': 'West India'
        },
        {
            'title': 'Holi Color Celebration',
            'festival': 'Holi',
            'description': 'People celebrating with vibrant colored powders',
            'region': 'North India'
        },
        {
            'title': 'Navratri Garba Dance',
            'festival': 'Navratri',
            'description': 'Traditional Gujarati folk dance during Navratri nights',
            'region': 'West India'
        },
        {
            'title': 'Onam Pookalam',
            'festival': 'Onam',
            'description': 'Intricate flower carpet decorations for Onam festival',
            'region': 'South India'
        },
        {
            'title': 'Durga Puja Pandal',
            'festival': 'Durga Puja',
            'description': 'Elaborately decorated temporary structures housing Durga idols',
            'region': 'East India'
        }
    ]
    
    # Display sample gallery
    st.markdown("### 🌟 Sample Festival Images")
    st.markdown("*In a full implementation, actual uploaded images would appear here*")
    
    for i in range(0, len(sample_images), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(sample_images):
                img = sample_images[i + j]
                with col:
                    st.markdown(f"""
                    <div style="
                        border: 2px solid #FF7F50;
                        border-radius: 15px;
                        padding: 1.5rem;
                        margin-bottom: 1rem;
                        background: linear-gradient(145deg, #fff, #f8f9fa);
                        box-shadow: 0 4px 8px rgba(255, 127, 80, 0.2);
                    ">
                        <div style="
                            width: 100%;
                            height: 200px;
                            background: linear-gradient(45deg, #FF7F50, #FF6B35);
                            border-radius: 10px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            margin-bottom: 1rem;
                        ">
                            <span style="color: white; font-size: 3rem;">🖼️</span>
                        </div>
                        <h4 style="margin: 0 0 0.5rem 0; color: #FF6B35;">{img['title']}</h4>
                        <p style="color: #666; font-size: 0.9rem; margin: 0.5rem 0;">
                            <strong>Festival:</strong> {img['festival']}<br>
                            <strong>Region:</strong> {img['region']}
                        </p>
                        <p style="color: #555; font-size: 0.9rem; margin: 0.5rem 0;">
                            {img['description']}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666;">
    <p>🖼️ Help preserve India's visual cultural heritage through festival images</p>
    <small>Images help document traditions, celebrations, and cultural practices for future generations</small>
</div>
""", unsafe_allow_html=True)