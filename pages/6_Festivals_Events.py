import streamlit as st
import json
from datetime import datetime
from utils.data_manager import save_user_data, load_corpus_data
from utils.ai_validation import validate_content
from utils.theming import apply_chatgpt_theme
from utils.translations import get_translations, SUPPORTED_LANGUAGES
from utils.auth import is_logged_in, get_current_user, update_user_contributions

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
    page_title="Festivals & Events - Indian Culture Explorer",
    page_icon="🎊",
    layout="wide"
)

# Get translations
translations = get_translations(st.session_state.selected_language)

# Page header with festival theme
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
        🎊 Festivals & Cultural Events
    </h1>
    <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.9;">
        Share and explore India's vibrant festival celebrations
    </p>
</div>
""", unsafe_allow_html=True)

# Main content columns
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🎆 Add Festival Information")
    
    with st.form("festival_form"):
        festival_name = st.text_input(
            "Festival Name:",
            placeholder="e.g., Diwali, Holi, Eid, Christmas, Dussehra"
        )
        
        festival_category = st.selectbox(
            "Festival Type:",
            [
                "Religious Festival",
                "Harvest Festival", 
                "Seasonal Celebration",
                "Regional Festival",
                "Cultural Event",
                "National Holiday",
                "Local Tradition"
            ]
        )
        
        festival_region = st.selectbox(
            "Primary Region:",
            ["Pan-India", "North India", "South India", "East India", "West India", "Central India", "Northeast India"]
        )
        
        festival_months = st.multiselect(
            "Celebration Months:",
            ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
        )
        
        festival_description = st.text_area(
            "Festival Description:",
            placeholder="Describe the significance, traditions, rituals, foods, and cultural importance...",
            height=150
        )
        
        festival_traditions = st.text_area(
            "Key Traditions & Rituals:",
            placeholder="e.g., lighting diyas, exchanging gifts, special prayers, traditional foods...",
            height=100
        )
        
        festival_foods = st.text_input(
            "Traditional Foods:",
            placeholder="e.g., sweets, special dishes, drinks"
        )
        
        cultural_significance = st.text_area(
            "Cultural & Historical Significance:",
            placeholder="Historical background, mythology, cultural importance...",
            height=100
        )
        
        submitted = st.form_submit_button("🎊 Submit Festival Information")
        
        if submitted and festival_name and festival_description:
            if not is_logged_in():
                st.warning("Please login to submit festival information")
            else:
                current_user = get_current_user()
                # Create comprehensive festival data
                festival_data = {
                    'type': 'festival_event',
                    'name': festival_name,
                    'category': festival_category,
                    'region': festival_region,
                    'months': festival_months,
                    'description': festival_description,
                    'traditions': festival_traditions,
                    'foods': festival_foods,
                    'significance': cultural_significance,
                    'language': st.session_state.selected_language,
                    'timestamp': datetime.now().isoformat(),
                    'contributor': current_user.get('username', 'unknown') if current_user else 'unknown'
                }
                
                # Validate content
                full_content = f"Festival: {festival_name}\nDescription: {festival_description}\nTraditions: {festival_traditions}\nSignificance: {cultural_significance}"
                validation_result = validate_content(full_content, "Cultural Event")
                
                if validation_result['is_valid']:
                    festival_data['quality_score'] = validation_result['quality_score']
                    save_user_data(festival_data)
                    username = current_user.get('username') if current_user else 'unknown'
                    update_user_contributions(username)
                    st.session_state.user_contributions.append(festival_data)
                    st.success("✅ Festival information added successfully!")
                    st.balloons()
                else:
                    st.warning("⚠️ Please provide more detailed information about the festival.")

with col2:
    st.markdown("### 📊 Festival Statistics")
    
    # Load data and show statistics
    data = load_corpus_data()
    festival_data = [item for item in data if item.get('type') == 'festival_event']
    
    st.metric("🎊 Total Festivals", len(festival_data))
    
    if festival_data:
        # Show festivals by region
        regions = {}
        categories = {}
        for item in festival_data:
            region = item.get('region', 'Unknown')
            category = item.get('category', 'Unknown')
            regions[region] = regions.get(region, 0) + 1
            categories[category] = categories.get(category, 0) + 1
        
        st.markdown("#### By Region:")
        for region, count in regions.items():
            st.write(f"• {region}: {count}")
        
        st.markdown("#### By Category:")
        for category, count in categories.items():
            st.write(f"• {category}: {count}")

# Display existing festivals
st.markdown("---")
st.markdown("### 🎆 Explore Indian Festivals")

if festival_data:
    # Create festival cards
    for i in range(0, len(festival_data), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(festival_data):
                festival = festival_data[i + j]
                with col:
                    with st.expander(f"🎊 {festival.get('name', 'Unknown Festival')}"):
                        st.markdown(f"**Region:** {festival.get('region', 'Unknown')}")
                        st.markdown(f"**Type:** {festival.get('category', 'Unknown')}")
                        if festival.get('months'):
                            st.markdown(f"**Months:** {', '.join(festival.get('months', []))}")
                        st.markdown(f"**Description:** {festival.get('description', '')}")
                        if festival.get('traditions'):
                            st.markdown(f"**Traditions:** {festival.get('traditions', '')}")
                        if festival.get('foods'):
                            st.markdown(f"**Traditional Foods:** {festival.get('foods', '')}")
                        if festival.get('significance'):
                            st.markdown(f"**Significance:** {festival.get('significance', '')}")
else:
    st.info("🌟 Be the first to add information about Indian festivals!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; border-radius: 10px; background-color: #FFF8E1;">
    <h4>🤝 Help Preserve Festival Traditions</h4>
    <p>Your contributions help document and preserve India's rich festival heritage for future generations.</p>
    <small>All festival information is validated and stored for cultural preservation.</small>
</div>
""", unsafe_allow_html=True)