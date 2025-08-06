import streamlit as st

def apply_chatgpt_theme(theme_mode: str = 'light'):
    """
    Apply ChatGPT-inspired theming to the Streamlit app.
    
    Args:
        theme_mode: Either 'light' or 'dark'
    """
    
    if theme_mode == 'dark':
        # Dark mode colors
        bg_color = "#343541"
        text_color = "#ECECF1"
        secondary_bg = "#444654"
        accent_color = "#10A37F"
        sidebar_bg = "#2C2D33"
        input_bg = "#40414F"
        border_color = "#4E5163"
    else:
        # Light mode colors  
        bg_color = "#FFFFFF"
        text_color = "#000000"
        secondary_bg = "#F7F7F8"
        accent_color = "#10A37F"
        sidebar_bg = "#F7F7F8"
        input_bg = "#FFFFFF"
        border_color = "#E5E5E5"
    
    # Apply custom CSS
    st.markdown(f"""
    <style>
    /* Main app background */
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    
    /* Sidebar styling */
    .css-1d391kg {{
        background-color: {sidebar_bg};
    }}
    
    .css-1cypcdb {{
        background-color: {sidebar_bg};
    }}
    
    /* Main content area */
    .main .block-container {{
        background-color: {bg_color};
        color: {text_color};
        padding-top: 2rem;
    }}
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {{
        color: {text_color} !important;
        font-family: "Söhne", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    
    /* Text elements */
    p, li, span, div {{
        color: {text_color} !important;
    }}
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > div > div {{
        background-color: {input_bg} !important;
        color: {text_color} !important;
        border: 1px solid {border_color} !important;
        border-radius: 8px;
    }}
    
    /* Buttons */
    .stButton > button {{
        background-color: {accent_color};
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.2s;
    }}
    
    .stButton > button:hover {{
        background-color: #0E8C6B;
        transform: translateY(-1px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    
    /* Metrics */
    .metric-container {{
        background-color: {secondary_bg};
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid {border_color};
    }}
    
    /* Expandable sections */
    .streamlit-expanderHeader {{
        background-color: {secondary_bg} !important;
        color: {text_color} !important;
        border-radius: 8px;
    }}
    
    .streamlit-expanderContent {{
        background-color: {bg_color} !important;
        border: 1px solid {border_color};
        border-radius: 0 0 8px 8px;
    }}
    
    /* Success/Info/Warning messages */
    .stSuccess {{
        background-color: rgba(16, 163, 127, 0.1);
        color: {text_color};
        border: 1px solid {accent_color};
        border-radius: 8px;
    }}
    
    .stInfo {{
        background-color: rgba(59, 130, 246, 0.1);
        color: {text_color};
        border: 1px solid #3B82F6;
        border-radius: 8px;
    }}
    
    .stWarning {{
        background-color: rgba(245, 158, 11, 0.1);
        color: {text_color};
        border: 1px solid #F59E0B;
        border-radius: 8px;
    }}
    
    .stError {{
        background-color: rgba(239, 68, 68, 0.1);
        color: {text_color};
        border: 1px solid #EF4444;
        border-radius: 8px;
    }}
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 2px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background-color: {secondary_bg};
        color: {text_color};
        border-radius: 8px 8px 0 0;
        padding: 0.5rem 1rem;
        border: 1px solid {border_color};
    }}
    
    .stTabs [aria-selected="true"] {{
        background-color: {accent_color} !important;
        color: white !important;
    }}
    
    /* Radio buttons */
    .stRadio > div {{
        background-color: {secondary_bg};
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid {border_color};
    }}
    
    /* Selectbox */
    .stSelectbox > div > div {{
        background-color: {input_bg};
        border: 1px solid {border_color};
        border-radius: 8px;
    }}
    
    /* Columns with cards */
    .element-container {{
        background-color: {bg_color};
    }}
    
    /* Download button */
    .stDownloadButton > button {{
        background-color: {accent_color};
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }}
    
    /* Color picker */
    .stColorPicker > div > div {{
        background-color: {input_bg};
        border: 1px solid {border_color};
        border-radius: 8px;
    }}
    
    /* Slider */
    .stSlider > div > div > div > div {{
        background-color: {accent_color};
    }}
    
    /* Chat-like message containers */
    .chat-message {{
        background-color: {secondary_bg};
        padding: 1rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid {border_color};
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}
    
    .user-message {{
        background-color: {accent_color};
        color: white;
        margin-left: 20%;
    }}
    
    .assistant-message {{
        background-color: {secondary_bg};
        color: {text_color};
        margin-right: 20%;
    }}
    
    /* Custom event card styling */
    .event-card {{
        background-color: {secondary_bg};
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid {border_color};
        margin: 1rem 0;
        transition: all 0.2s;
    }}
    
    .event-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    
    /* Progress indicators */
    .stProgress > div > div > div > div {{
        background-color: {accent_color};
    }}
    
    /* Dataframe styling */
    .dataframe {{
        background-color: {bg_color} !important;
        color: {text_color} !important;
    }}
    
    /* Footer styling */
    .footer {{
        background-color: {secondary_bg};
        color: {text_color};
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin-top: 3rem;
        border: 1px solid {border_color};
    }}
    
    /* Responsive design */
    @media (max-width: 768px) {{
        .main .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}
        
        .chat-message {{
            margin: 0.5rem 0;
        }}
        
        .user-message,
        .assistant-message {{
            margin-left: 0;
            margin-right: 0;
        }}
    }}
    
    /* Loading animations */
    .stSpinner > div {{
        border-color: {accent_color} transparent transparent transparent;
    }}
    
    /* Custom scrollbar for dark mode */
    ::-webkit-scrollbar {{
        width: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: {secondary_bg};
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: {border_color};
        border-radius: 4px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: {accent_color};
    }}
    </style>
    """, unsafe_allow_html=True)

def toggle_theme():
    """Toggle between light and dark themes."""
    if st.session_state.theme_mode == 'light':
        st.session_state.theme_mode = 'dark'
    else:
        st.session_state.theme_mode = 'light'

def get_theme_colors(theme_mode: str = 'light') -> dict:
    """
    Get theme colors for use in components.
    
    Returns:
        dict: Dictionary containing color values for the specified theme
    """
    
    if theme_mode == 'dark':
        return {
            'bg_color': "#343541",
            'text_color': "#ECECF1",
            'secondary_bg': "#444654",
            'accent_color': "#10A37F",
            'sidebar_bg': "#2C2D33",
            'input_bg': "#40414F",
            'border_color': "#4E5163",
            'success_color': "#10A37F",
            'warning_color': "#F59E0B",
            'error_color': "#EF4444",
            'info_color': "#3B82F6"
        }
    else:
        return {
            'bg_color': "#FFFFFF",
            'text_color': "#000000",
            'secondary_bg': "#F7F7F8",
            'accent_color': "#10A37F",
            'sidebar_bg': "#F7F7F8",
            'input_bg': "#FFFFFF",
            'border_color': "#E5E5E5",
            'success_color': "#10A37F",
            'warning_color': "#F59E0B",
            'error_color': "#EF4444",
            'info_color': "#3B82F6"
        }

def create_styled_card(content: str, title: str = "", card_type: str = "default", theme_mode: str = 'light') -> str:
    """
    Create a styled card component with ChatGPT-like styling.
    
    Args:
        content: The main content of the card
        title: Optional title for the card
        card_type: Type of card ('default', 'success', 'warning', 'error', 'info')
        theme_mode: Current theme mode
    
    Returns:
        str: HTML string for the styled card
    """
    
    colors = get_theme_colors(theme_mode)
    
    # Determine card colors based on type
    if card_type == 'success':
        bg_color = f"rgba(16, 163, 127, 0.1)"
        border_color = colors['success_color']
    elif card_type == 'warning':
        bg_color = f"rgba(245, 158, 11, 0.1)"
        border_color = colors['warning_color']
    elif card_type == 'error':
        bg_color = f"rgba(239, 68, 68, 0.1)"
        border_color = colors['error_color']
    elif card_type == 'info':
        bg_color = f"rgba(59, 130, 246, 0.1)"
        border_color = colors['info_color']
    else:
        bg_color = colors['secondary_bg']
        border_color = colors['border_color']
    
    title_html = f"<h4 style='margin-top: 0; color: {colors['text_color']};'>{title}</h4>" if title else ""
    
    card_html = f"""
    <div style="
        background-color: {bg_color};
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid {border_color};
        margin: 1rem 0;
        color: {colors['text_color']};
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        transition: all 0.2s;
    ">
        {title_html}
        <div style="color: {colors['text_color']};">
            {content}
        </div>
    </div>
    """
    
    return card_html

def create_chatgpt_message(content: str, is_user: bool = False, theme_mode: str = 'light') -> str:
    """
    Create a ChatGPT-style message bubble.
    
    Args:
        content: Message content
        is_user: Whether this is a user message (True) or assistant message (False)
        theme_mode: Current theme mode
    
    Returns:
        str: HTML string for the message bubble
    """
    
    colors = get_theme_colors(theme_mode)
    
    if is_user:
        bg_color = colors['accent_color']
        text_color = "white"
        margin_style = "margin-left: 20%; margin-right: 0;"
        avatar = "🧑‍💻"
    else:
        bg_color = colors['secondary_bg']
        text_color = colors['text_color']
        margin_style = "margin-left: 0; margin-right: 20%;"
        avatar = "🤖"
    
    message_html = f"""
    <div style="
        background-color: {bg_color};
        color: {text_color};
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        {margin_style}
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        max-width: 80%;
    ">
        <div style="display: flex; align-items: flex-start; gap: 0.5rem;">
            <span style="font-size: 1.2rem;">{avatar}</span>
            <div style="flex: 1;">
                {content}
            </div>
        </div>
    </div>
    """
    
    return message_html

def apply_responsive_layout():
    """Apply responsive layout adjustments for mobile and tablet devices."""
    
    st.markdown("""
    <style>
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-top: 1rem !important;
        }
        
        .stButton > button {
            width: 100%;
            margin-bottom: 0.5rem;
        }
        
        .stColumns > div {
            margin-bottom: 1rem;
        }
        
        /* Make cards full width on mobile */
        .chat-message,
        .user-message,
        .assistant-message,
        .event-card {
            margin-left: 0 !important;
            margin-right: 0 !important;
            max-width: 100% !important;
        }
        
        /* Reduce font sizes on mobile */
        h1 { font-size: 1.5rem !important; }
        h2 { font-size: 1.3rem !important; }
        h3 { font-size: 1.1rem !important; }
    }
    
    /* Tablet responsiveness */
    @media (min-width: 768px) and (max-width: 1024px) {
        .main .block-container {
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }
        
        .chat-message {
            max-width: 90%;
        }
        
        .user-message {
            margin-left: 10%;
        }
        
        .assistant-message {
            margin-right: 10%;
        }
    }
    
    /* Improve touch targets for mobile */
    @media (max-width: 768px) {
        .stButton > button,
        .stSelectbox > div > div,
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            min-height: 44px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
