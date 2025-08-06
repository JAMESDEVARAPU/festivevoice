import streamlit as st
import json
import random
from datetime import datetime
from utils.theming import apply_chatgpt_theme
from utils.data_manager import save_user_data, load_corpus_data
from utils.ai_validation import validate_content
from utils.translations import get_translations

st.set_page_config(page_title="Cultural Quiz", page_icon="🧠", layout="wide")

# Apply theming
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = 'light'
apply_chatgpt_theme(st.session_state.theme_mode)

# Initialize quiz session state
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_questions_answered' not in st.session_state:
    st.session_state.quiz_questions_answered = 0
if 'current_quiz_type' not in st.session_state:
    st.session_state.current_quiz_type = None

# Get translations
selected_language = st.session_state.get('selected_language', 'English')
translations = get_translations(selected_language)

st.title("🧠 Indian Cultural Knowledge Quiz")
st.markdown("### Test Your Knowledge & Contribute Questions")

# Quiz categories with sample questions
quiz_categories = {
    "History & Heritage": {
        "icon": "🏛️",
        "description": "Ancient civilizations, empires, and historical events",
        "sample_questions": [
            {
                "question": "Which empire was known as the 'Golden Age' of Indian culture?",
                "options": ["Mauryan Empire", "Gupta Empire", "Mughal Empire", "Chola Empire"],
                "correct": 1,
                "explanation": "The Gupta Empire (320-550 CE) is considered the Golden Age due to remarkable achievements in science, mathematics, astronomy, religion, and philosophy."
            },
            {
                "question": "The ancient university of Nalanda was located in which present-day state?",
                "options": ["Uttar Pradesh", "Bihar", "West Bengal", "Odisha"],
                "correct": 1,
                "explanation": "Nalanda University was located in Bihar and was one of the world's first residential universities."
            }
        ]
    },
    "Languages & Literature": {
        "icon": "📚",
        "description": "Indian languages, scripts, and literary works",
        "sample_questions": [
            {
                "question": "How many official languages are recognized by the Indian Constitution?",
                "options": ["18", "20", "22", "24"],
                "correct": 2,
                "explanation": "The Indian Constitution recognizes 22 official languages in the Eighth Schedule."
            },
            {
                "question": "The epic 'Ramayana' was originally written in which language?",
                "options": ["Hindi", "Sanskrit", "Tamil", "Pali"],
                "correct": 1,
                "explanation": "The Ramayana was originally composed in Sanskrit by sage Valmiki."
            }
        ]
    },
    "Festivals & Traditions": {
        "icon": "🎉",
        "description": "Indian festivals, customs, and cultural practices",
        "sample_questions": [
            {
                "question": "Diwali is primarily celebrated to commemorate:",
                "options": ["Lord Rama's return to Ayodhya", "Goddess Lakshmi's blessing", "Victory of good over evil", "All of the above"],
                "correct": 3,
                "explanation": "Diwali has multiple significances including Lord Rama's return, Goddess Lakshmi worship, and the general triumph of light over darkness."
            }
        ]
    },
    "Arts & Music": {
        "icon": "🎭",
        "description": "Classical arts, music, dance, and performing traditions",
        "sample_questions": [
            {
                "question": "Which classical dance form originated in Tamil Nadu?",
                "options": ["Kathak", "Bharatanatyam", "Odissi", "Manipuri"],
                "correct": 1,
                "explanation": "Bharatanatyam is the classical dance form that originated in Tamil Nadu."
            }
        ]
    },
    "Geography & Regions": {
        "icon": "🗺️",
        "description": "Indian geography, states, and regional cultures",
        "sample_questions": [
            {
                "question": "Which state is known as the 'Land of Five Rivers'?",
                "options": ["Haryana", "Punjab", "Rajasthan", "Gujarat"],
                "correct": 1,
                "explanation": "Punjab gets its name from 'Panch' (five) and 'Ab' (water/rivers), referring to the five rivers that flow through it."
            }
        ]
    },
    "Food & Cuisine": {
        "icon": "🍛",
        "description": "Regional cuisines, cooking traditions, and food culture",
        "sample_questions": [
            {
                "question": "Which spice is known as the 'Queen of Spices'?",
                "options": ["Cardamom", "Black Pepper", "Cinnamon", "Saffron"],
                "correct": 0,
                "explanation": "Cardamom is called the 'Queen of Spices' due to its distinctive flavor and high value."
            }
        ]
    }
}

# Event background color
event_bg_color = st.session_state.get('event_color', '#E3F2FD')

# Quiz mode selection
st.subheader("🎯 Choose Your Quiz Mode")

quiz_mode = st.radio(
    "Select how you'd like to participate:",
    ["Take Quiz", "Contribute Questions", "View Leaderboard"],
    horizontal=True
)

if quiz_mode == "Take Quiz":
    st.markdown("---")
    st.subheader("📝 Take the Cultural Knowledge Quiz")
    
    # Category selection for quiz
    selected_category = st.selectbox(
        "Choose a quiz category:",
        list(quiz_categories.keys())
    )
    
    category_info = quiz_categories[selected_category]
    
    # Display category info
    st.markdown(f"""
    <div style="background-color: {event_bg_color}; padding: 15px; border-radius: 10px; margin: 10px 0;">
        <h4>{category_info['icon']} {selected_category}</h4>
        <p>{category_info['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quiz interface
    if st.button(f"Start {selected_category} Quiz"):
        st.session_state.current_quiz_type = selected_category
        st.session_state.quiz_score = 0
        st.session_state.quiz_questions_answered = 0
    
    # Display quiz questions
    if st.session_state.current_quiz_type == selected_category:
        questions = category_info['sample_questions']
        
        if st.session_state.quiz_questions_answered < len(questions):
            current_q = questions[st.session_state.quiz_questions_answered]
            
            st.markdown(f"**Question {st.session_state.quiz_questions_answered + 1}/{len(questions)}**")
            st.markdown(f"### {current_q['question']}")
            
            # Answer options
            selected_answer = st.radio(
                "Choose your answer:",
                options=range(len(current_q['options'])),
                format_func=lambda x: current_q['options'][x],
                key=f"q_{st.session_state.quiz_questions_answered}"
            )
            
            if st.button("Submit Answer"):
                is_correct = selected_answer == current_q['correct']
                
                if is_correct:
                    st.success("✅ Correct!")
                    st.session_state.quiz_score += 1
                else:
                    st.error(f"❌ Incorrect. The correct answer is: {current_q['options'][current_q['correct']]}")
                
                st.info(f"💡 Explanation: {current_q['explanation']}")
                st.session_state.quiz_questions_answered += 1
                
                # Save quiz attempt data
                quiz_data = {
                    'type': 'quiz_attempt',
                    'category': selected_category,
                    'question': current_q['question'],
                    'user_answer': current_q['options'][selected_answer],
                    'correct_answer': current_q['options'][current_q['correct']],
                    'is_correct': is_correct,
                    'user_language': selected_language,
                    'timestamp': datetime.now().isoformat()
                }
                save_user_data(quiz_data)
                
                if st.session_state.quiz_questions_answered < len(questions):
                    if st.button("Next Question"):
                        st.rerun()
                else:
                    st.markdown("### 🎉 Quiz Complete!")
                    score_percentage = (st.session_state.quiz_score / len(questions)) * 100
                    st.metric("Your Score", f"{st.session_state.quiz_score}/{len(questions)} ({score_percentage:.1f}%)")
                    
                    if score_percentage >= 80:
                        st.success("🌟 Excellent! You're a cultural expert!")
                    elif score_percentage >= 60:
                        st.info("👍 Good job! Keep learning!")
                    else:
                        st.warning("📚 Keep exploring Indian culture!")

elif quiz_mode == "Contribute Questions":
    st.markdown("---")
    st.subheader("✍️ Contribute Quiz Questions")
    
    # Question contribution form
    question_category = st.selectbox(
        "Question category:",
        list(quiz_categories.keys()),
        key="contrib_category"
    )
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        question_text = st.text_area(
            "Your question:",
            placeholder="Write a clear, interesting question about Indian culture...",
            height=100
        )
        
        # Options
        st.markdown("**Answer options:**")
        option1 = st.text_input("Option 1:")
        option2 = st.text_input("Option 2:")
        option3 = st.text_input("Option 3:")
        option4 = st.text_input("Option 4:")
        
        correct_option = st.selectbox(
            "Which option is correct?",
            ["Option 1", "Option 2", "Option 3", "Option 4"]
        )
        
        explanation = st.text_area(
            "Explanation:",
            placeholder="Explain why this answer is correct and provide additional context...",
            height=80
        )
    
    with col2:
        st.markdown("#### 💡 Question Guidelines")
        st.info("""
        **Good questions:**
        • Are factually accurate
        • Have one clearly correct answer
        • Include educational explanations
        • Cover diverse aspects of culture
        • Are appropriate for all audiences
        • Include interesting trivia
        """)
        
        difficulty_level = st.selectbox(
            "Difficulty level:",
            ["Easy", "Medium", "Hard"]
        )
        
        source = st.text_input(
            "Source/Reference:",
            placeholder="Where did you learn this fact?"
        )
        
        region = st.text_input(
            "Specific region (if applicable):",
            placeholder="Does this relate to a specific area?"
        )
    
    # Submit question
    if st.button("Submit Question") and question_text and all([option1, option2, option3, option4]) and explanation:
        # Validate question content
        validation_result = validate_content(
            f"Question: {question_text} Answer: {explanation}",
            f"Quiz question about {question_category}"
        )
        
        if validation_result['is_valid']:
            question_data = {
                'type': 'quiz_question_contribution',
                'category': question_category,
                'question': question_text,
                'options': [option1, option2, option3, option4],
                'correct_option': correct_option,
                'explanation': explanation,
                'difficulty': difficulty_level,
                'source': source,
                'region': region,
                'user_language': selected_language,
                'timestamp': datetime.now().isoformat(),
                'quality_score': validation_result['quality_score']
            }
            
            save_user_data(question_data)
            if 'user_contributions' not in st.session_state:
                st.session_state.user_contributions = []
            st.session_state.user_contributions.append(question_data)
            
            st.success("✅ Thank you for contributing a quiz question!")
            st.balloons()
        else:
            st.warning("⚠️ Please provide more detailed explanations and ensure accuracy.")

elif quiz_mode == "View Leaderboard":
    st.markdown("---")
    st.subheader("🏆 Cultural Knowledge Leaderboard")
    
    # Load quiz data for analytics
    corpus_data = load_corpus_data()
    quiz_attempts = [item for item in corpus_data if item.get('type') == 'quiz_attempt']
    question_contributions = [item for item in corpus_data if item.get('type') == 'quiz_question_contribution']
    
    if quiz_attempts or question_contributions:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📊 Quiz Statistics")
            if quiz_attempts:
                total_attempts = len(quiz_attempts)
                correct_answers = len([q for q in quiz_attempts if q.get('is_correct')])
                accuracy_rate = (correct_answers / total_attempts * 100) if total_attempts > 0 else 0
                
                st.metric("Total Quiz Attempts", total_attempts)
                st.metric("Overall Accuracy", f"{accuracy_rate:.1f}%")
                
                # Category performance
                category_stats = {}
                for attempt in quiz_attempts:
                    cat = attempt.get('category', 'Unknown')
                    if cat not in category_stats:
                        category_stats[cat] = {'correct': 0, 'total': 0}
                    category_stats[cat]['total'] += 1
                    if attempt.get('is_correct'):
                        category_stats[cat]['correct'] += 1
                
                st.markdown("**Category Performance:**")
                for cat, stats in category_stats.items():
                    accuracy = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
                    st.markdown(f"• {cat}: {accuracy:.1f}% ({stats['correct']}/{stats['total']})")
        
        with col2:
            st.markdown("#### 🌟 Contribution Stats")
            if question_contributions:
                st.metric("Questions Contributed", len(question_contributions))
                
                # Quality distribution
                quality_scores = [q.get('quality_score', 0) for q in question_contributions if q.get('quality_score')]
                if quality_scores:
                    avg_quality = sum(quality_scores) / len(quality_scores)
                    st.metric("Average Question Quality", f"{avg_quality:.1f}/5")
                
                # Contribution by category
                contrib_categories = {}
                for contrib in question_contributions:
                    cat = contrib.get('category', 'Unknown')
                    contrib_categories[cat] = contrib_categories.get(cat, 0) + 1
                
                st.markdown("**Questions by Category:**")
                for cat, count in sorted(contrib_categories.items(), key=lambda x: x[1], reverse=True):
                    st.markdown(f"• {cat}: {count}")
    else:
        st.info("📊 No quiz data available yet. Start taking quizzes or contributing questions!")

# Personal progress
st.markdown("---")
st.subheader("📈 Your Progress")

if 'user_contributions' in st.session_state:
    user_quiz_data = [
        contrib for contrib in st.session_state.user_contributions 
        if contrib.get('type') in ['quiz_attempt', 'quiz_question_contribution']
    ]
    
    if user_quiz_data:
        quiz_attempts_user = [c for c in user_quiz_data if c.get('type') == 'quiz_attempt']
        question_contribs_user = [c for c in user_quiz_data if c.get('type') == 'quiz_question_contribution']
        
        col3, col4, col5 = st.columns(3)
        
        with col3:
            st.metric("Quiz Attempts", len(quiz_attempts_user))
        
        with col4:
            correct_user = len([q for q in quiz_attempts_user if q.get('is_correct')])
            user_accuracy = (correct_user / len(quiz_attempts_user) * 100) if quiz_attempts_user else 0
            st.metric("Your Accuracy", f"{user_accuracy:.1f}%")
        
        with col5:
            st.metric("Questions Contributed", len(question_contribs_user))
    else:
        st.info("🎯 Take your first quiz or contribute a question to see your progress!")

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🎭 ← Cultural Stories"):
        st.switch_page("pages/3_🎭_Cultural_Stories.py")
with col2:
    if st.button("🏠 Back to Home"):
        st.switch_page("app.py")
with col3:
    if st.button("📊 Data Export →"):
        st.switch_page("pages/5_📊_Data_Export.py")
