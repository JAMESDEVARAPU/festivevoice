# Overview

The Indian Culture Explorer is a Streamlit-based web application designed to preserve, share, and explore India's rich cultural heritage. The platform serves as a collaborative knowledge base where users can contribute historical information, stories, language learning content, and cultural data while participating in educational quizzes. The application supports multiple Indian languages and provides data export capabilities for research purposes.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Framework**: Streamlit for rapid web application development
- **Multi-page Structure**: Organized into distinct functional modules (Historical Timeline, Language Learning, Cultural Stories, Quiz, Data Export)
- **Theming System**: Custom ChatGPT-inspired light/dark mode theming with CSS injection
- **Internationalization**: Support for multiple Indian languages with translation utilities
- **Session Management**: Streamlit session state for user preferences, theme settings, and quiz progress

## Backend Architecture
- **Data Storage**: JSON file-based storage system for corpus data with thread-safe operations
- **Content Validation**: AI-powered content validation using OpenAI and Anthropic APIs with fallback to basic validation
- **Modular Utilities**: Separated concerns across utility modules (theming, data management, translations, AI validation)
- **File Structure**: Clean separation between main application, pages, utilities, and data storage

## Data Management
- **Storage Format**: JSON-based corpus data storage in `data/corpus_data.json`
- **Thread Safety**: File locking mechanisms to prevent data corruption during concurrent access
- **Data Categories**: Support for multiple content types (historical events, stories, language content, quiz questions)
- **Export Capabilities**: Data analytics and export functionality for research purposes

## Content Management System
- **User Contributions**: Structured forms for submitting cultural content across different categories
- **Quality Assurance**: AI validation system to ensure content accuracy and cultural appropriateness
- **Content Organization**: Categorized storage by type (mythology, folk tales, historical events, language content)
- **Search and Discovery**: Organized presentation of cultural content by categories and regions

# External Dependencies

## AI Services
- **OpenAI API**: Primary content validation and quality assessment service
- **Anthropic API**: Secondary validation service as fallback option

## Python Libraries
- **streamlit**: Core web application framework
- **pandas**: Data manipulation and export functionality
- **json**: Data serialization and storage operations
- **datetime**: Timestamp management for user contributions
- **threading**: Thread-safe file operations
- **io**: In-memory file operations for data export

## Data Sources
- **Local JSON Storage**: Primary data persistence without external database dependencies
- **User-Generated Content**: Community-driven content creation and validation
- **Translation Services**: Built-in translation utilities for supported Indian languages

## Configuration
- **Environment Variables**: API keys for AI validation services (OPENAI_API_KEY)
- **Session State**: Streamlit session management for user preferences and application state
- **File System**: Local file-based configuration and data storage