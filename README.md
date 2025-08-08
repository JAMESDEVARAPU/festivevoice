An AI-powered multimedia platform for preserving and sharing India's rich cultural heritage, focusing on festivals and cultural traditions through community contributions.

## 🎯 Project Overview

This Streamlit-based web application serves as a comprehensive platform for documenting and preserving India's cultural heritage through:

- **Voice Stories**: Record oral traditions, folk tales, and cultural narratives
- **Video Traditions**: Share cultural practices, dances, rituals, and traditions
- **Festival Documentation**: Capture and explore India's vibrant festival celebrations
- **Community Gallery**: Browse and discover cultural contributions from the community
- **Personal Dashboard**: Manage individual contributions with analytics and export capabilities

## ✨ Key Features

### 🔐 User Authentication
- Secure user registration and login system
- Password hashing with session management
- Personal contribution tracking and management

### 🎨 Modern Interface
- ChatGPT-inspired light/dark mode theming
- FestiveVoice orange branding with professional design
- Responsive and culturally sensitive user interface
- Multilingual support for Indian languages

### 🤖 AI-Powered Content Validation
- OpenAI and Anthropic API integration for content quality assessment
- Automated validation of cultural accuracy and appropriateness
- Fallback validation system for reliable content processing

### 📊 Data Management
- JSON-based storage system with thread-safe operations
- Data export capabilities for research purposes
- Analytics and contribution tracking
- Search and filtering functionality

### 🌐 Multimedia Support
- Audio file upload for voice recordings
- Video file upload with format validation
- Size limits and quality optimization
- Metadata tracking and storage

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-gitlab-repo-url>
   cd indian-cultural-heritage-platform
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py --server.port 5000
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

### Replit Deployment

1. Import the repository into Replit
2. Install dependencies using the package manager
3. Add API keys in the Secrets tab:
   - `OPENAI_API_KEY`
   - `ANTHROPIC_API_KEY`
4. Run the application using the configured workflow

## 📁 Project Structure

```
├── app.py                      # Main application entry point
├── pages/                      # Streamlit pages
│   ├── 1_Voice_Stories.py     # Voice recording interface
│   ├── 2_Video_Traditions.py  # Video upload interface
│   ├── 5_Community_Gallery.py # Community content browser
│   ├── 6_Festivals_Events.py  # Festival documentation
│   └── 7_My_Contributions.py  # Personal dashboard
├── utils/                      # Utility modules
│   ├── auth.py                # Authentication system
│   ├── data_manager.py        # Data operations
│   ├── theming.py             # UI theming
│   ├── translations.py        # Multilingual support
│   └── validation.py          # AI content validation
├── data/                       # Data storage
│   └── corpus_data.json       # Application data
├── assets/                     # Static assets
├── attached_assets/            # User uploaded content
├── requirements.txt            # Python dependencies
├── replit.md                  # Project documentation
└── README.md                  # This file
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit with custom HTML/CSS
- **Backend**: Python with JSON file storage
- **AI Integration**: OpenAI GPT-4o and Anthropic Claude APIs
- **Authentication**: Custom secure authentication system
- **Theming**: Custom ChatGPT-inspired design system
- **Data Processing**: Pandas for analytics and export

| header | header |
| James | Designer |
|        |        |
|        |        |

## 🔧 Configuration

### API Keys
The application requires API keys for AI validation features:
- **OpenAI API**: Primary content validation service
- **Anthropic API**: Secondary validation with fallback support


## 📊 Data Export

The platform supports data export in multiple formats:
- **CSV**: Contribution analytics and metadata
- **JSON**: Raw data export for advanced processing
- **Filtered Exports**: Custom data selections based on criteria






**Built with ❤️ for preserving India's rich cultural heritage**