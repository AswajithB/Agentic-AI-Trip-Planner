import streamlit as st
import requests
import datetime

BASE_URL = "http://localhost:8000"  # Backend endpoint

# --- Page Configuration ---
st.set_page_config(
    page_title="Travel Planner AI",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS (Dark Mode) ---
st.markdown("""
<style>
    /* Main App Background */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    /* Header */
    .main-header {
        font-family: 'Helvetica Neue', sans-serif;
        color: #FAFAFA;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #FF4B4B, #FF914D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    
    /* Subheader */
    .sub-header {
        text-align: center;
        color: #A3A8B8;
        margin-bottom: 2rem;
    }

    /* Chat Message Bubbles */
    .chat-message {
        padding: 1.5rem; 
        border-radius: 0.5rem; 
        margin-bottom: 1rem; 
        display: flex
    }
    
    /* User Message - Darker Blue/Grey */
    .chat-message.user {
        background-color: #262730;
        border-left: 5px solid #4285f4;
        color: #E0E0E0;
    }
    
    /* Bot Message - Dark Grey/Black */
    .chat-message.bot {
        background-color: #1A1C24;
        border-left: 5px solid #0f9d58;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        color: #E0E0E0;
    }
    
    /* Sidebar Text */
    .sidebar-text {
        font-size: 0.9rem;
        color: #909090;
    }
    
    /* Input Box styling (Streamlit handles this mostly, but we can try to blend) */
    .stTextInput > div > div > input {
        background-color: #262730;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2060/2060284.png", width=100)
    st.title("Trip Settings")
    
    st.markdown("### 🛠️ Functionality")
    st.markdown("""
    - **Plan a basic trip**: "Plan a 3-day trip to Paris"
    - **Get estimates**: "How much for a hotel in Mumbai?"
    - **Weather checks**: "Weather in Tokyo next week"
    """)
    
    st.markdown("---")
    if st.button("🗑️ Clear Chat History", type="primary"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("<div class='sidebar-text'>Powered by LangGraph & Groq</div>", unsafe_allow_html=True)

# --- Main Interface ---
st.markdown("<h1 class='main-header'>🌍 AI Travel Planner</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Your personal AI agent for crafting perfect travel itineraries.</p>", unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Where do you want to go today?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("🤖 Thinking... plotting the best route..."):
            try:
                payload = {"question": prompt}
                response = requests.post(f"{BASE_URL}/query", json=payload)
                
                if response.status_code == 200:
                    answer = response.json().get("answer", "I couldn't generate a plan. Please try again.")
                    
                    # Format the response with a nice header
                    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                    formatted_response = f"""
                    {answer}
                    
                    ---
                    *Generated at {timestamp}*
                    """
                    st.markdown(formatted_response)
                    st.session_state.messages.append({"role": "assistant", "content": formatted_response})
                else:
                    error_msg = f"❌ Error: {response.text}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
            
            except Exception as e:
                error_msg = f"❌ Connection Error: {e}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})