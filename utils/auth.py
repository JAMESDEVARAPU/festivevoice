import streamlit as st
import json
import hashlib
from datetime import datetime
import os
from threading import Lock

# File lock for thread-safe operations
auth_lock = Lock()
AUTH_FILE = "data/users.json"

def ensure_auth_file():
    """Ensure the auth file exists"""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(AUTH_FILE):
        with open(AUTH_FILE, 'w') as f:
            json.dump({}, f)

def hash_password(password: str) -> str:
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Load users from JSON file"""
    ensure_auth_file()
    try:
        with auth_lock:
            with open(AUTH_FILE, 'r') as f:
                return json.load(f)
    except:
        return {}

def save_users(users_data):
    """Save users to JSON file"""
    ensure_auth_file()
    try:
        with auth_lock:
            with open(AUTH_FILE, 'w') as f:
                json.dump(users_data, f, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving user data: {e}")
        return False

def register_user(username, email, password, region, full_name=""):
    """Register a new user"""
    users = load_users()
    
    # Check if user already exists
    if username in users:
        return False, "Username already exists"
    
    # Check if email already exists
    for user_data in users.values():
        if user_data.get('email') == email:
            return False, "Email already registered"
    
    # Create new user
    users[username] = {
        'email': email,
        'password_hash': hash_password(password),
        'region': region,
        'full_name': full_name,
        'registration_date': datetime.now().isoformat(),
        'last_login': None,
        'contributions_count': 0,
        'role': 'user'
    }
    
    if save_users(users):
        return True, "Registration successful"
    else:
        return False, "Registration failed - please try again"

def authenticate_user(username, password):
    """Authenticate user login"""
    users = load_users()
    
    if username not in users:
        return False, "Invalid username or password"
    
    user_data = users[username]
    if user_data['password_hash'] != hash_password(password):
        return False, "Invalid username or password"
    
    # Update last login
    users[username]['last_login'] = datetime.now().isoformat()
    save_users(users)
    
    return True, user_data

def get_user_data(username):
    """Get user data by username"""
    users = load_users()
    return users.get(username)

def update_user_contributions(username):
    """Update user contribution count"""
    users = load_users()
    if username in users:
        users[username]['contributions_count'] = users[username].get('contributions_count', 0) + 1
        save_users(users)

def is_logged_in():
    """Check if user is logged in"""
    return 'authenticated_user' in st.session_state and st.session_state.authenticated_user is not None

def get_current_user():
    """Get current logged in user data"""
    if is_logged_in():
        return st.session_state.authenticated_user
    return None

def logout_user():
    """Logout current user"""
    if 'authenticated_user' in st.session_state:
        del st.session_state.authenticated_user
    if 'user_profile' in st.session_state:
        del st.session_state.user_profile

def login_form():
    """Display login form"""
    st.markdown("### 🔐 Login")
    
    with st.form("login_form"):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        
        col1, col2 = st.columns(2)
        with col1:
            login_submitted = st.form_submit_button("Login", use_container_width=True)
        with col2:
            if st.form_submit_button("Forgot Password?", use_container_width=True):
                st.info("Please contact support to reset your password")
        
        if login_submitted and username and password:
            success, result = authenticate_user(username, password)
            if success:
                user_data = result.copy()
                user_data['username'] = username
                st.session_state.authenticated_user = user_data
                st.success("Login successful!")
                st.rerun()
            else:
                st.error(result)

def registration_form():
    """Display registration form"""
    st.markdown("### 📝 Create Account")
    
    with st.form("registration_form"):
        full_name = st.text_input("Full Name (Optional)", placeholder="Your full name")
        username = st.text_input("Username *", placeholder="Choose a unique username")
        email = st.text_input("Email *", placeholder="your.email@example.com")
        password = st.text_input("Password *", type="password", placeholder="Choose a secure password")
        confirm_password = st.text_input("Confirm Password *", type="password", placeholder="Confirm your password")
        
        region = st.selectbox(
            "Region *",
            ["North India", "South India", "East India", "West India", "Central India", "Northeast India", "Outside India"]
        )
        
        # Terms and conditions
        agree_terms = st.checkbox("I agree to the terms and conditions for cultural data contribution")
        
        register_submitted = st.form_submit_button("Create Account", use_container_width=True)
        
        if register_submitted:
            if not all([username, email, password, confirm_password]):
                st.error("Please fill all required fields marked with *")
            elif password != confirm_password:
                st.error("Passwords do not match")
            elif len(password) < 6:
                st.error("Password must be at least 6 characters long")
            elif not agree_terms:
                st.error("Please agree to the terms and conditions")
            else:
                success, message = register_user(username, email, password, region, full_name)
                if success:
                    st.success(message)
                    st.info("You can now login with your credentials")
                else:
                    st.error(message)

def user_profile_display():
    """Display logged in user profile"""
    user = get_current_user()
    if user:
        username = user.get('username', 'Unknown')
        
        st.markdown(f"### 👤 Welcome, {user.get('full_name') or username}!")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**Username:** {username}")
            st.markdown(f"**Email:** {user.get('email', 'Not provided')}")
            st.markdown(f"**Region:** {user.get('region', 'Not specified')}")
            st.markdown(f"**Contributions:** {user.get('contributions_count', 0)}")
            
            if user.get('last_login'):
                try:
                    last_login = datetime.fromisoformat(user['last_login'].replace('Z', '+00:00'))
                    st.markdown(f"**Last Login:** {last_login.strftime('%Y-%m-%d %H:%M')}")
                except:
                    pass
        
        with col2:
            if st.button("Logout", use_container_width=True):
                logout_user()
                st.success("Logged out successfully!")
                st.rerun()

def auth_sidebar():
    """Authentication sidebar component"""
    if is_logged_in():
        user_profile_display()
    else:
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        with tab1:
            login_form()
        
        with tab2:
            registration_form()

def require_auth(func):
    """Decorator to require authentication for functions"""
    def wrapper(*args, **kwargs):
        if not is_logged_in():
            st.warning("Please login to access this feature")
            auth_sidebar()
            return None
        return func(*args, **kwargs)
    return wrapper