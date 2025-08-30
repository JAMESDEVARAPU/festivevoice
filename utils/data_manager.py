import json
import os
from datetime import datetime
from typing import List, Dict, Any
import threading

# Thread lock for file operations
file_lock = threading.Lock()

DATA_FILE = "data/corpus_data.json"

def ensure_data_directory():
    """Ensure the data directory exists."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

def load_corpus_data() -> List[Dict[str, Any]]:
    """
    Load corpus data from JSON file.
    Returns empty list if file doesn't exist or is corrupted.
    """
    try:
        ensure_data_directory()
        
        if not os.path.exists(DATA_FILE):
            return []
        
        with file_lock:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
        # Ensure data is a list
        if isinstance(data, list):
            return data
        else:
            print(f"Warning: Data file contains {type(data)}, expected list")
            return []
            
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {DATA_FILE}: {e}")
        return []
    except Exception as e:
        print(f"Error loading corpus data: {e}")
        return []

def save_corpus_data(data: List[Dict[str, Any]]) -> bool:
    """
    Save corpus data to JSON file.
    Returns True if successful, False otherwise.
    """
    try:
        ensure_data_directory()
        
        with file_lock:
            # Create backup of existing data
            if os.path.exists(DATA_FILE):
                backup_file = f"{DATA_FILE}.backup"
                with open(DATA_FILE, 'r', encoding='utf-8') as original:
                    with open(backup_file, 'w', encoding='utf-8') as backup:
                        backup.write(original.read())
            
            # Write new data
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        
        return True
        
    except Exception as e:
        print(f"Error saving corpus data: {e}")
        return False

def save_user_data(user_entry: Dict[str, Any]) -> bool:
    """
    Save a single user contribution to the corpus.
    Appends to existing data.
    """
    try:
        # Add metadata
        user_entry['id'] = generate_entry_id()
        user_entry['timestamp'] = datetime.now().isoformat()
        
        # Load existing data
        corpus_data = load_corpus_data()
        
        # Append new entry
        corpus_data.append(user_entry)
        
        # Save updated data
        return save_corpus_data(corpus_data)
        
    except Exception as e:
        print(f"Error saving user data: {e}")
        return False

def generate_entry_id() -> str:
    """Generate a unique ID for a corpus entry."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    return f"entry_{timestamp}"

def get_data_by_type(data_type: str) -> List[Dict[str, Any]]:
    """Get all corpus entries of a specific type."""
    corpus_data = load_corpus_data()
    return [entry for entry in corpus_data if entry.get('type') == data_type]

def get_data_by_language(language: str) -> List[Dict[str, Any]]:
    """Get all corpus entries in a specific language."""
    corpus_data = load_corpus_data()
    return [
        entry for entry in corpus_data 
        if entry.get('language') == language or entry.get('user_language') == language
    ]

def get_data_by_region(region: str) -> List[Dict[str, Any]]:
    """Get all corpus entries from a specific region."""
    corpus_data = load_corpus_data()
    return [entry for entry in corpus_data if entry.get('region') == region]

def get_data_by_festival(festival: str) -> List[Dict[str, Any]]:
    """Get all corpus entries linked to a specific festival."""
    corpus_data = load_corpus_data()
    return [entry for entry in corpus_data if entry.get('festival_event') == festival]

def get_festival_content_summary() -> Dict[str, Dict[str, int]]:
    """Get summary of content types for each festival."""
    corpus_data = load_corpus_data()
    festival_summary = {}
    
    for entry in corpus_data:
        festival = entry.get('festival_event', 'Not Specified')
        if festival != 'Not Specified':
            if festival not in festival_summary:
                festival_summary[festival] = {
                    'voice_stories': 0,
                    'video_traditions': 0,
                    'cultural_stories': 0,
                    'festival_events': 0,
                    'total': 0
                }
            
            entry_type = entry.get('type', '')
            if entry_type == 'voice_story':
                festival_summary[festival]['voice_stories'] += 1
            elif entry_type == 'video_tradition':
                festival_summary[festival]['video_traditions'] += 1
            elif entry_type == 'cultural_story':
                festival_summary[festival]['cultural_stories'] += 1
            elif entry_type == 'festival_event':
                festival_summary[festival]['festival_events'] += 1
            
            festival_summary[festival]['total'] += 1
    
    return festival_summary

def get_recent_data(limit: int = 10) -> List[Dict[str, Any]]:
    """Get the most recent corpus entries."""
    corpus_data = load_corpus_data()
    
    # Sort by timestamp (most recent first)
    sorted_data = sorted(
        corpus_data, 
        key=lambda x: x.get('timestamp', ''), 
        reverse=True
    )
    
    return sorted_data[:limit]

def search_corpus(query: str) -> List[Dict[str, Any]]:
    """
    Search corpus data for entries containing the query.
    Searches in content, title, and other text fields.
    """
    corpus_data = load_corpus_data()
    query_lower = query.lower()
    
    matching_entries = []
    
    for entry in corpus_data:
        # Check various text fields
        text_fields = [
            entry.get('content', ''),
            entry.get('title', ''),
            entry.get('question', ''),
            entry.get('original_word', ''),
            entry.get('english_translation', ''),
            entry.get('moral_lesson', ''),
            entry.get('explanation', '')
        ]
        
        # Check if query appears in any text field
        if any(query_lower in str(field).lower() for field in text_fields):
            matching_entries.append(entry)
    
    return matching_entries

def get_festival_list() -> List[str]:
    """Get list of major Indian festivals for linking content."""
    return [
        "Diwali", "Holi", "Dussehra", "Navratri", "Karva Chauth", "Raksha Bandhan",
        "Krishna Janmashtami", "Ganesh Chaturthi", "Durga Puja", "Kali Puja",
        "Onam", "Pongal", "Makar Sankranti", "Baisakhi", "Gudi Padwa",
        "Eid al-Fitr", "Eid al-Adha", "Christmas", "Good Friday", "Easter",
        "Guru Nanak Jayanti", "Buddha Purnima", "Mahavir Jayanti",
        "Poila Boishakh", "Bihu", "Vishu", "Ugadi", "Chaitra Navratri",
        "Ram Navami", "Hanuman Jayanti", "Shivratri", "Teej", "Chhath Puja",
        "Regional Festival", "Other"
    ]

def get_corpus_statistics() -> Dict[str, Any]:
    """Get comprehensive statistics about the corpus including internship progress."""
    corpus_data = load_corpus_data()
    
    if not corpus_data:
        return {
            'total_entries': 0,
            'data_types': {},
            'languages': {},
            'regions': {},
            'festivals': {},
            'quality_stats': {},
            'temporal_stats': {},
            'internship_progress': {
                'audio_video_hours': 0,
                'image_text_records': 0,
                'target_audio_video': 80,
                'target_image_text': 800
            }
        }
    
    stats = {
        'total_entries': len(corpus_data),
        'data_types': {},
        'languages': {},
        'regions': {},
        'festivals': {},
        'quality_stats': {},
        'temporal_stats': {},
        'internship_progress': {
            'audio_video_hours': 0,
            'image_text_records': 0,
            'target_audio_video': 80,
            'target_image_text': 800
        }
    }
    
    quality_scores = []
    timestamps = []
    audio_video_hours = 0
    image_text_records = 0
    
    for entry in corpus_data:
        # Count data types
        data_type = entry.get('type', 'Unknown')
        stats['data_types'][data_type] = stats['data_types'].get(data_type, 0) + 1
        
        # Count languages
        language = entry.get('language', entry.get('user_language', 'Unknown'))
        stats['languages'][language] = stats['languages'].get(language, 0) + 1
        
        # Count regions
        region = entry.get('region', 'Unknown')
        if region != 'Unknown':
            stats['regions'][region] = stats['regions'].get(region, 0) + 1
        
        # Count festivals
        festival = entry.get('festival_event', 'Not Specified')
        if festival != 'Not Specified':
            stats['festivals'][festival] = stats['festivals'].get(festival, 0) + 1
        
        # Calculate internship progress
        entry_type = entry.get('type', '')
        if entry_type in ['voice_story', 'video_tradition']:
            # Estimate duration based on content length (rough approximation)
            content_length = len(entry.get('content', ''))
            estimated_minutes = max(1, content_length // 100)  # ~1 min per 100 chars
            audio_video_hours += estimated_minutes / 60
        elif entry_type in ['cultural_story', 'cultural_fact', 'festival_event', 'image_submission']:
            image_text_records += 1
        
        # Collect quality scores
        if 'quality_score' in entry:
            quality_scores.append(entry['quality_score'])
        
        # Collect timestamps
        if 'timestamp' in entry:
            timestamps.append(entry['timestamp'])
    
    # Calculate quality statistics
    if quality_scores:
        stats['quality_stats'] = {
            'average_quality': sum(quality_scores) / len(quality_scores),
            'highest_quality': max(quality_scores),
            'lowest_quality': min(quality_scores),
            'high_quality_count': len([s for s in quality_scores if s >= 4]),
            'low_quality_count': len([s for s in quality_scores if s < 3])
        }
    
    # Calculate temporal statistics
    if timestamps:
        sorted_timestamps = sorted(timestamps)
        stats['temporal_stats'] = {
            'first_entry': sorted_timestamps[0],
            'latest_entry': sorted_timestamps[-1],
            'entries_today': len([
                t for t in timestamps 
                if t.startswith(datetime.now().strftime('%Y-%m-%d'))
            ])
        }
    
    # Update internship progress
    stats['internship_progress'] = {
        'audio_video_hours': round(audio_video_hours, 2),
        'image_text_records': image_text_records,
        'target_audio_video': 80,
        'target_image_text': 800,
        'audio_video_progress': min(100, (audio_video_hours / 80) * 100),
        'image_text_progress': min(100, (image_text_records / 800) * 100)
    }
    
    return stats

def export_corpus_subset(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Export a filtered subset of the corpus based on provided filters.
    
    Filters can include:
    - types: list of data types to include
    - languages: list of languages to include
    - regions: list of regions to include
    - min_quality: minimum quality score
    - date_from: start date (ISO format)
    - date_to: end date (ISO format)
    """
    corpus_data = load_corpus_data()
    filtered_data = []
    
    for entry in corpus_data:
        # Filter by type
        if 'types' in filters and entry.get('type') not in filters['types']:
            continue
        
        # Filter by language
        if 'languages' in filters:
            entry_lang = entry.get('language', entry.get('user_language', ''))
            if entry_lang not in filters['languages']:
                continue
        
        # Filter by region
        if 'regions' in filters and entry.get('region') not in filters['regions']:
            continue
        
        # Filter by quality
        if 'min_quality' in filters:
            entry_quality = entry.get('quality_score', 0)
            if entry_quality < filters['min_quality']:
                continue
        
        # Filter by date
        entry_timestamp = entry.get('timestamp', '')
        if 'date_from' in filters and entry_timestamp < filters['date_from']:
            continue
        if 'date_to' in filters and entry_timestamp > filters['date_to']:
            continue
        
        filtered_data.append(entry)
    
    return filtered_data

def backup_corpus_data() -> bool:
    """Create a timestamped backup of the corpus data."""
    try:
        corpus_data = load_corpus_data()
        
        if not corpus_data:
            return True  # Nothing to backup
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"data/corpus_backup_{timestamp}.json"
        
        ensure_data_directory()
        
        with open(backup_filename, 'w', encoding='utf-8') as f:
            json.dump(corpus_data, f, indent=2, ensure_ascii=False)
        
        print(f"Backup created: {backup_filename}")
        return True
        
    except Exception as e:
        print(f"Error creating backup: {e}")
        return False

def clean_duplicate_entries() -> int:
    """
    Remove duplicate entries from the corpus based on content similarity.
    Returns the number of duplicates removed.
    """
    corpus_data = load_corpus_data()
    
    if len(corpus_data) <= 1:
        return 0
    
    unique_entries = []
    duplicates_removed = 0
    
    for entry in corpus_data:
        is_duplicate = False
        
        for unique_entry in unique_entries:
            # Check for exact content match
            if (entry.get('content') == unique_entry.get('content') and
                entry.get('type') == unique_entry.get('type')):
                is_duplicate = True
                duplicates_removed += 1
                break
        
        if not is_duplicate:
            unique_entries.append(entry)
    
    if duplicates_removed > 0:
        save_corpus_data(unique_entries)
        print(f"Removed {duplicates_removed} duplicate entries")
    
    return duplicates_removed

def validate_corpus_integrity() -> Dict[str, Any]:
    """
    Validate the integrity of the corpus data.
    Returns a report of any issues found.
    """
    corpus_data = load_corpus_data()
    
    validation_report = {
        'total_entries': len(corpus_data),
        'valid_entries': 0,
        'issues': [],
        'warnings': []
    }
    
    required_fields = ['type', 'timestamp']
    
    for i, entry in enumerate(corpus_data):
        entry_issues = []
        
        # Check for required fields
        for field in required_fields:
            if field not in entry:
                entry_issues.append(f"Missing required field: {field}")
        
        # Check timestamp format
        if 'timestamp' in entry:
            try:
                datetime.fromisoformat(entry['timestamp'].replace('Z', '+00:00'))
            except ValueError:
                entry_issues.append("Invalid timestamp format")
        
        # Check content length
        if 'content' in entry and len(entry['content'].strip()) < 5:
            entry_issues.append("Content too short")
        
        if entry_issues:
            validation_report['issues'].append({
                'entry_index': i,
                'entry_id': entry.get('id', 'unknown'),
                'issues': entry_issues
            })
        else:
            validation_report['valid_entries'] += 1
    
    # Check for potential data quality issues
    if validation_report['total_entries'] > 0:
        valid_percentage = (validation_report['valid_entries'] / validation_report['total_entries']) * 100
        
        if valid_percentage < 90:
            validation_report['warnings'].append(f"Low data quality: only {valid_percentage:.1f}% of entries are valid")
        
        # Check for language distribution
        languages = {}
        for entry in corpus_data:
            lang = entry.get('language', entry.get('user_language', 'Unknown'))
            languages[lang] = languages.get(lang, 0) + 1
        
        if len(languages) == 1 and 'Unknown' in languages:
            validation_report['warnings'].append("No language information available")
    
    return validation_report
