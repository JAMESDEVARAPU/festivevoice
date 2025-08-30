import streamlit as st
import json
from datetime import datetime
from utils.theming import apply_chatgpt_theme
from utils.data_manager import save_user_data, load_corpus_data, get_festival_list
from utils.ai_validation import validate_content
from utils.translations import get_translations
from utils.auth import is_logged_in, get_current_user, update_user_contributions

st.set_page_config(page_title="Cultural Stories", page_icon="🎭", layout="wide")

# Apply theming
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = 'light'
apply_chatgpt_theme(st.session_state.theme_mode)

# Get translations
selected_language = st.session_state.get('selected_language', 'English')
translations = get_translations(selected_language)

st.title("🎭 Indian Cultural Stories")
st.markdown("### Share and Discover the Rich Narrative Heritage of India")

# Story categories
story_categories = {
    "Mythology & Epics": {
        "description": "Stories from Ramayana, Mahabharata, Puranas, and regional mythologies",
        "examples": ["Ramayana tales", "Krishna leelas", "Local deity stories", "Puranic narratives"],
        "icon": "🏛️"
    },
    "Folk Tales": {
        "description": "Traditional stories passed down through generations",
        "examples": ["Village stories", "Panchatantra tales", "Regional folklore", "Animal fables"],
        "icon": "🌾"
    },
    "Festival Stories": {
        "description": "Narratives behind Indian festivals and celebrations",
        "examples": ["Diwali stories", "Holi legends", "Regional festival tales", "Seasonal celebrations"],
        "icon": "🎉"
    },
    "Historical Legends": {
        "description": "Stories of heroes, rulers, and historical events",
        "examples": ["Shivaji tales", "Freedom fighter stories", "Royal legends", "Battle narratives"],
        "icon": "⚔️"
    },
    "Family Traditions": {
        "description": "Personal and family cultural narratives",
        "examples": ["Wedding customs", "Birth rituals", "Coming of age stories", "Family legends"],
        "icon": "👨‍👩‍👧‍👦"
    },
    "Regional Stories": {
        "description": "Stories specific to states, regions, or communities",
        "examples": ["Tribal stories", "Coastal legends", "Mountain folklore", "Desert tales"],
        "icon": "🗺️"
    }
}

# Category selection
st.subheader("📚 Explore Story Categories")
selected_category = st.selectbox(
    "Choose a story category:",
    list(story_categories.keys())
)

category_data = story_categories[selected_category]
event_bg_color = st.session_state.get('event_color', '#E3F2FD')

# Display category information
st.markdown(f"""
<div style="background-color: {event_bg_color}; padding: 20px; border-radius: 10px; margin: 10px 0;">
    <h3>{category_data['icon']} {selected_category}</h3>
    <p><strong>Description:</strong> {category_data['description']}</p>
    <p><strong>Examples:</strong> {', '.join(category_data['examples'])}</p>
</div>
""", unsafe_allow_html=True)

# Story submission form
st.markdown("---")
st.subheader(f"✍️ Share Your {selected_category} Story")

col1, col2 = st.columns([2, 1])

with col1:
    story_title = st.text_input(
        "Story Title:",
        placeholder="Give your story a compelling title..."
    )
    
    story_content = st.text_area(
        "Story Content:",
        placeholder="Share your story here. Include cultural details, moral lessons, and vivid descriptions...",
        height=200
    )
    
    story_origin = st.text_input(
        "Origin/Source:",
        placeholder="Where did you learn this story? (e.g., grandmother, regional tradition, ancient text...)"
    )
    
    story_language = st.selectbox(
        "Original language of the story:",
        ["Sanskrit", "Hindi", "Tamil", "Bengali", "Telugu", "Marathi", "Gujarati", 
         "Kannada", "Malayalam", "Punjabi", "Urdu", "Odia", "Regional dialect", "English", "Other"]
    )

with col2:
    st.markdown("#### 📝 Story Guidelines")
    st.info("""
    **Great stories include:**
    • Clear beginning, middle, end
    • Cultural context and significance  
    • Moral or lesson learned
    • Vivid descriptions of settings
    • Character details and motivations
    • Regional or family variations
    • Historical context if known
    """)
    
    story_region = st.text_input(
        "Region/State:",
        placeholder="Which region is this story from?"
    )
    
    story_moral = st.text_area(
        "Moral/Lesson:",
        placeholder="What is the key message or teaching?",
        height=80
    )
    
    audience_age = st.selectbox(
        "Suitable for:",
        ["All ages", "Children", "Adults", "Elderly", "Religious audiences"]
    )
    
    # Festival/Event linking
    festival_event = st.selectbox(
        "Related Festival/Event (Optional):",
        ["Not Related to Any Festival"] + get_festival_list(),
        help="Link this story to a specific festival or cultural event"
    )

# Additional story details
with st.expander("📖 Additional Story Details (Optional)"):
    col3, col4 = st.columns(2)
    
    with col3:
        characters = st.text_area(
            "Main Characters:",
            placeholder="Describe the key characters in your story...",
            height=80
        )
        
        setting_time = st.text_input(
            "Time Period:",
            placeholder="When does this story take place?"
        )
    
    with col4:
        setting_place = st.text_input(
            "Setting/Location:",
            placeholder="Where does this story take place?"
        )
        
        variations = st.text_area(
            "Known Variations:",
            placeholder="Are there different versions of this story?",
            height=80
        )

# Submit story
if st.button("📚 Submit Story") and story_title and story_content:
    # Validate content with AI
    validation_result = validate_content(
        f"{story_title}: {story_content}",
        f"Cultural story in category: {selected_category}"
    )
    
    if validation_result['is_valid']:
        if not is_logged_in():
            st.warning("Please login to submit cultural stories")
        else:
            current_user = get_current_user()
            # Save story to corpus
            user_data = {
                'type': 'cultural_story',
                'category': selected_category,
                'title': story_title,
                'content': story_content,
                'origin': story_origin,
                'original_language': story_language,
                'region': story_region,
                'moral_lesson': story_moral,
                'audience_age': audience_age,
                'characters': characters,
                'setting_time': setting_time,
                'setting_place': setting_place,
                'variations': variations,
                'festival_event': festival_event if festival_event != "Not Related to Any Festival" else None,
                'user_language': selected_language,
                'timestamp': datetime.now().isoformat(),
                'quality_score': validation_result['quality_score'],
                'contributor': current_user.get('username', 'unknown') if current_user else 'unknown'
            }
            
            save_user_data(user_data)
            username = current_user.get('username') if current_user else 'unknown'
            update_user_contributions(username)
            if 'user_contributions' not in st.session_state:
                st.session_state.user_contributions = []
            st.session_state.user_contributions.append(user_data)
            
            st.success("✅ Thank you for sharing your cultural story!")
            st.balloons()
    else:
        st.warning("⚠️ Please provide more details to make your story more complete.")

# Story exploration section
st.markdown("---")
st.subheader("📖 Explore Community Stories")

# Load existing stories
corpus_data = load_corpus_data()
cultural_stories = [item for item in corpus_data if item.get('type') == 'cultural_story']

if cultural_stories:
    # Filter by category
    category_stories = [story for story in cultural_stories if story.get('category') == selected_category]
    
    if category_stories:
        st.markdown(f"**{len(category_stories)} stories found in {selected_category}**")
        
        for i, story in enumerate(category_stories[-5:]):  # Show last 5 stories
            with st.expander(f"📚 {story.get('title', 'Untitled Story')}"):
                col5, col6 = st.columns([3, 1])
                
                with col5:
                    st.markdown(f"**Story:** {story.get('content', '')[:300]}...")
                    if story.get('moral_lesson'):
                        st.markdown(f"**Moral:** {story.get('moral_lesson')}")
                
                with col6:
                    st.markdown(f"**Region:** {story.get('region', 'Unknown')}")
                    st.markdown(f"**Language:** {story.get('original_language', 'Unknown')}")
                    st.markdown(f"**Audience:** {story.get('audience_age', 'All ages')}")
                    if story.get('quality_score'):
                        st.metric("Quality", f"{story.get('quality_score')}/5")
    else:
        st.info(f"No stories yet in {selected_category}. Be the first to contribute!")
else:
    st.info("No stories have been shared yet. Be the first to contribute!")

# Interactive story features
st.markdown("---")
st.subheader("🎯 Interactive Story Features")

tabs = st.tabs(["🔍 Story Search", "🏆 Story Challenges", "📊 Story Analytics"])

with tabs[0]:
    st.markdown("#### Search Stories by Keywords")
    search_term = st.text_input("Search for stories containing:")
    search_region = st.selectbox("Filter by region:", ["All regions", "North India", "South India", "East India", "West India", "Central India"])
    
    if search_term and cultural_stories:
        matching_stories = [
            story for story in cultural_stories 
            if search_term.lower() in story.get('content', '').lower() or 
               search_term.lower() in story.get('title', '').lower()
        ]
        st.write(f"Found {len(matching_stories)} stories matching '{search_term}'")

with tabs[1]:
    st.markdown("#### Weekly Story Challenges")
    challenges = [
        "Share a story about monsoon season",
        "Tell a tale involving animals as main characters",
        "Describe a festival celebration from your region",
        "Share a story passed down in your family",
        "Tell about a local hero or legend"
    ]
    
    current_challenge = st.selectbox("This week's challenge:", challenges)
    st.info(f"💡 Challenge: {current_challenge}")
    
    if st.button("Accept Challenge"):
        st.success("🎯 Challenge accepted! Use the story submission form above.")

with tabs[2]:
    if cultural_stories:
        # Simple analytics
        category_counts = {}
        language_counts = {}
        region_counts = {}
        
        for story in cultural_stories:
            cat = story.get('category', 'Unknown')
            category_counts[cat] = category_counts.get(cat, 0) + 1
            
            lang = story.get('original_language', 'Unknown')
            language_counts[lang] = language_counts.get(lang, 0) + 1
            
            reg = story.get('region', 'Unknown')
            region_counts[reg] = region_counts.get(reg, 0) + 1
        
        col7, col8, col9 = st.columns(3)
        
        with col7:
            st.markdown("**Stories by Category**")
            for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                st.markdown(f"• {cat}: {count}")
        
        with col8:
            st.markdown("**Stories by Language**")
            for lang, count in sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                st.markdown(f"• {lang}: {count}")
        
        with col9:
            st.markdown("**Stories by Region**")
            for reg, count in sorted(region_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                st.markdown(f"• {reg}: {count}")

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📚 ← Language Learning"):
        st.switch_page("pages/2_📚_Language_Learning.py")
with col2:
    if st.button("🏠 Back to Home"):
        st.switch_page("app.py")
with col3:
    if st.button("🧠 Cultural Quiz →"):
        st.switch_page("pages/4_🧠_Cultural_Quiz.py")
