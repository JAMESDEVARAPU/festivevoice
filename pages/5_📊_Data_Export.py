import streamlit as st
import json
import pandas as pd
from datetime import datetime
import io
from utils.theming import apply_chatgpt_theme
from utils.data_manager import load_corpus_data
from utils.translations import get_translations

st.set_page_config(page_title="Data Export", page_icon="📊", layout="wide")

# Apply theming
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = 'light'
apply_chatgpt_theme(st.session_state.theme_mode)

# Get translations
selected_language = st.session_state.get('selected_language', 'English')
translations = get_translations(selected_language)

st.title("📊 Corpus Data Analytics & Export")
st.markdown("### Analyze and Export Collected Cultural Data")

# Load corpus data
corpus_data = load_corpus_data()

if not corpus_data:
    st.warning("📭 No data available for export. Start contributing to build the corpus!")
    st.stop()

# Data overview
st.subheader("📈 Data Overview")

# Calculate statistics
total_entries = len(corpus_data)
data_types = {}
languages = {}
regions = {}
categories = {}

for entry in corpus_data:
    # Count by type
    entry_type = entry.get('type', 'Unknown')
    data_types[entry_type] = data_types.get(entry_type, 0) + 1
    
    # Count by language
    lang = entry.get('language', entry.get('user_language', 'Unknown'))
    languages[lang] = languages.get(lang, 0) + 1
    
    # Count by region
    region = entry.get('region', 'Unknown')
    if region != 'Unknown':
        regions[region] = regions.get(region, 0) + 1
    
    # Count by category
    category = entry.get('category', entry.get('period', 'General'))
    categories[category] = categories.get(category, 0) + 1

# Display metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Entries", total_entries)
with col2:
    st.metric("Data Types", len(data_types))
with col3:
    st.metric("Languages Covered", len(languages))
with col4:
    st.metric("Regions Covered", len(regions))

# Data distribution charts
st.markdown("---")
st.subheader("📊 Data Distribution")

tab1, tab2, tab3, tab4 = st.tabs(["Data Types", "Languages", "Regions", "Categories"])

with tab1:
    if data_types:
        # Create DataFrame for chart
        df_types = pd.DataFrame(list(data_types.items()), columns=['Type', 'Count'])
        df_types = df_types.sort_values('Count', ascending=True)
        
        st.bar_chart(df_types.set_index('Type'))
        
        # Detailed breakdown
        st.markdown("#### Detailed Breakdown by Type")
        for data_type, count in sorted(data_types.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_entries) * 100
            st.markdown(f"• **{data_type}**: {count} entries ({percentage:.1f}%)")

with tab2:
    if languages:
        df_langs = pd.DataFrame(list(languages.items()), columns=['Language', 'Count'])
        df_langs = df_langs.sort_values('Count', ascending=True)
        
        st.bar_chart(df_langs.set_index('Language'))
        
        st.markdown("#### Language Distribution")
        for lang, count in sorted(languages.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_entries) * 100
            st.markdown(f"• **{lang}**: {count} entries ({percentage:.1f}%)")

with tab3:
    if regions:
        st.markdown("#### Regional Contributions")
        for region, count in sorted(regions.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_entries) * 100
            st.markdown(f"• **{region}**: {count} entries ({percentage:.1f}%)")
    else:
        st.info("No regional data available")

with tab4:
    if categories:
        df_cats = pd.DataFrame(list(categories.items()), columns=['Category', 'Count'])
        df_cats = df_cats.sort_values('Count', ascending=True)
        
        st.bar_chart(df_cats.set_index('Category'))
        
        st.markdown("#### Category Breakdown")
        for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_entries) * 100
            st.markdown(f"• **{category}**: {count} entries ({percentage:.1f}%)")

# Data quality analysis
st.markdown("---")
st.subheader("🎯 Data Quality Analysis")

quality_scores = [entry.get('quality_score', 0) for entry in corpus_data if entry.get('quality_score')]

if quality_scores:
    col5, col6, col7 = st.columns(3)
    
    with col5:
        avg_quality = sum(quality_scores) / len(quality_scores)
        st.metric("Average Quality Score", f"{avg_quality:.2f}/5")
    
    with col6:
        high_quality = len([score for score in quality_scores if score >= 4])
        st.metric("High Quality Entries", f"{high_quality} ({high_quality/len(quality_scores)*100:.1f}%)")
    
    with col7:
        recent_entries = [entry for entry in corpus_data if entry.get('timestamp')]
        if recent_entries:
            recent_entries.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
            st.metric("Most Recent Entry", recent_entries[0].get('timestamp', '')[:10])

# Export functionality
st.markdown("---")
st.subheader("💾 Export Data")

export_format = st.selectbox(
    "Choose export format:",
    ["JSON", "CSV", "Excel"]
)

# Filter options
st.markdown("#### Export Filters")
col8, col9, col10 = st.columns(3)

with col8:
    filter_type = st.multiselect(
        "Filter by data type:",
        options=list(data_types.keys()),
        default=list(data_types.keys())
    )

with col9:
    filter_language = st.multiselect(
        "Filter by language:",
        options=list(languages.keys()),
        default=list(languages.keys())
    )

with col10:
    min_quality = st.slider(
        "Minimum quality score:",
        min_value=0.0,
        max_value=5.0,
        value=0.0,
        step=0.1
    )

# Apply filters
filtered_data = []
for entry in corpus_data:
    # Type filter
    if entry.get('type') not in filter_type:
        continue
    
    # Language filter
    entry_lang = entry.get('language', entry.get('user_language', 'Unknown'))
    if entry_lang not in filter_language:
        continue
    
    # Quality filter
    entry_quality = entry.get('quality_score', 0)
    if entry_quality < min_quality:
        continue
    
    filtered_data.append(entry)

st.info(f"📊 {len(filtered_data)} entries match your filter criteria (out of {total_entries} total)")

# Generate export file
if st.button("🔽 Generate Export File") and filtered_data:
    if export_format == "JSON":
        export_data = json.dumps(filtered_data, indent=2, ensure_ascii=False)
        st.download_button(
            label="📥 Download JSON",
            data=export_data,
            file_name=f"indian_culture_corpus_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
    
    elif export_format == "CSV":
        # Flatten the data for CSV
        flattened_data = []
        for entry in filtered_data:
            flat_entry = {}
            for key, value in entry.items():
                if isinstance(value, (list, dict)):
                    flat_entry[key] = json.dumps(value, ensure_ascii=False)
                else:
                    flat_entry[key] = value
            flattened_data.append(flat_entry)
        
        df = pd.DataFrame(flattened_data)
        csv_data = df.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv_data,
            file_name=f"indian_culture_corpus_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    
    elif export_format == "Excel":
        # Create Excel file
        flattened_data = []
        for entry in filtered_data:
            flat_entry = {}
            for key, value in entry.items():
                if isinstance(value, (list, dict)):
                    flat_entry[key] = json.dumps(value, ensure_ascii=False)
                else:
                    flat_entry[key] = value
            flattened_data.append(flat_entry)
        
        df = pd.DataFrame(flattened_data)
        
        # Create Excel buffer
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Cultural_Corpus', index=False)
        
        st.download_button(
            label="📥 Download Excel",
            data=excel_buffer.getvalue(),
            file_name=f"indian_culture_corpus_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# Sample data preview
st.markdown("---")
st.subheader("👁️ Data Preview")

if st.checkbox("Show sample data (first 10 entries)"):
    sample_data = filtered_data[:10]
    
    for i, entry in enumerate(sample_data):
        with st.expander(f"Entry {i+1}: {entry.get('type', 'Unknown')} - {entry.get('timestamp', '')[:10]}"):
            # Display entry details
            for key, value in entry.items():
                if key not in ['timestamp']:  # Skip timestamp in main display
                    if isinstance(value, str) and len(value) > 100:
                        st.markdown(f"**{key}**: {value[:100]}...")
                    else:
                        st.markdown(f"**{key}**: {value}")

# Data usage guidelines
st.markdown("---")
st.subheader("📋 Data Usage Guidelines")

st.markdown("""
### 🔒 Data Privacy & Usage
- This cultural corpus is collected for educational and research purposes
- Personal identifying information is not stored
- Data represents community knowledge and cultural heritage
- Usage should respect the cultural significance of the content
- Attribution to contributors and cultural communities is encouraged

### 📊 Research Applications
- Linguistic analysis of Indian languages
- Cultural preservation and documentation
- Educational content development
- AI model training for Indian cultural contexts
- Academic research in anthropology, linguistics, and cultural studies

### 🤝 Ethical Considerations
- Respect cultural sensitivities
- Acknowledge community contributions
- Use data responsibly and ethically
- Share insights back with contributing communities
- Maintain accuracy and context of cultural information
""")

# API access information (for advanced users)
st.markdown("---")
st.subheader("🔌 API Access")

with st.expander("Advanced: API Access Information"):
    st.markdown("""
    ### 📡 Programmatic Access
    For researchers and developers who need programmatic access to the corpus data:
    
    ```python
    # Example Python code to load corpus data
    import json
    
    def load_corpus_data():
        with open('data/corpus_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    
    # Filter by type
    def filter_by_type(data, data_type):
        return [item for item in data if item.get('type') == data_type]
    
    # Filter by language
    def filter_by_language(data, language):
        return [item for item in data if item.get('language') == language]
    ```
    
    ### 📚 Data Schema
    Each corpus entry follows this general structure:
    - `type`: Type of cultural data (story, vocabulary, historical_fact, etc.)
    - `content`: Main content or text
    - `language`: Primary language of the content
    - `region`: Geographic region (if applicable)
    - `category`: Content category
    - `timestamp`: When the data was contributed
    - `quality_score`: AI-validated quality score (0-5)
    """)

# Navigation
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("🧠 ← Cultural Quiz"):
        st.switch_page("pages/4_🧠_Cultural_Quiz.py")
with col2:
    if st.button("🏠 Back to Home"):
        st.switch_page("app.py")
