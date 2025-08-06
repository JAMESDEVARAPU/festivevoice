# Overview

The Indian Culture Explorer is a comprehensive Streamlit-based web application designed to preserve, share, and explore India's rich cultural heritage through multimedia content. The platform serves as a collaborative knowledge base where authenticated users can contribute voice stories, video traditions, festival information, and cultural data while managing their personal contributions dashboard. The application features secure user authentication, multilingual support, and data export capabilities for cultural preservation research.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Framework**: Streamlit for rapid web application development
- **Multi-page Structure**: Organized into multimedia-focused modules (Voice Stories, Video Traditions, Festivals & Events, Cultural Stories, Community Gallery, My Contributions)
- **Authentication UI**: Secure login/registration forms with user profile management
- **Theming System**: Custom ChatGPT-inspired light/dark mode theming with Viswam.ai orange branding
- **Internationalization**: Support for multiple Indian languages with translation utilities
- **Session Management**: Streamlit session state for user authentication, preferences, and contribution tracking

## Backend Architecture
- **Data Storage**: JSON file-based storage system for corpus data and user accounts with thread-safe operations
- **Authentication System**: Secure user registration/login with password hashing and session management
- **Content Validation**: AI-powered content validation using OpenAI and Anthropic APIs with fallback to basic validation
- **Multimedia Support**: Audio and video file upload capabilities with size limits and format validation
- **Modular Utilities**: Separated concerns across utility modules (auth, theming, data management, translations, AI validation)
- **File Structure**: Clean separation between main application, pages, utilities, and data storage

## Data Management
- **Storage Format**: JSON-based corpus data storage in `data/corpus_data.json`
- **Thread Safety**: File locking mechanisms to prevent data corruption during concurrent access
- **Data Categories**: Support for multiple content types (historical events, stories, language content, quiz questions)
- **Export Capabilities**: Data analytics and export functionality for research purposes

## Content Management System
- **User Contributions**: Authenticated multimedia content submission (voice recordings, videos, festival info, cultural facts)
- **Personal Dashboard**: Individual user contribution tracking with filtering, sorting, and export capabilities
- **Quality Assurance**: AI validation system to ensure content accuracy and cultural appropriateness
- **Content Organization**: Categorized storage by type (voice stories, video traditions, festivals, cultural facts)
- **Multimedia Handling**: Audio/video file processing with metadata tracking and storage optimization
- **Search and Discovery**: Organized presentation of cultural content by categories, regions, and contributors
- **Community Gallery**: Public viewing interface for all user-generated content with filtering, search, and contributor recognition

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