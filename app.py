import streamlit as st
from faq_logic import process_user_input
import time

# 1. Advanced UI Configuration
st.set_page_config(page_title="TechAssist | Next-Gen Support", page_icon="💻", layout="wide")

# 2. Professional Landing Page CSS
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }

    /* Animation Keyframes */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Chat Bubble Animation */
    .stChatMessage {
        animation: fadeInUp 0.5s ease-out forwards;
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        background: rgba(255, 255, 255, 0.05) !important;
        margin-bottom: 15px;
    }

    /* Landing Page Header */
    .hero-text {
        text-align: center;
        padding: 50px 0 20px 0;
        background: -webkit-linear-gradient(#00d4ff, #005f73);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.3);
        border-right: 1px solid rgba(0, 212, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Portfolio Section
with st.sidebar:
    st.image("https://img.icons8.com/clouds/100/000000/laptop.png")
    st.markdown("### Developer: Sriram Ponnaganti")
    st.divider()
    st.info("💡 **Tip:** Try asking about 'Smartphone Reset' or 'Pairing Earbuds'.")
    st.success("System Status: Online ✅")

# 4. Hero Section (The Landing Page Look)
st.markdown("<h1 class='hero-text'>TechAssist AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa; margin-top: -20px;'>Enterprise-Grade Self-Service Support Solution</p>", unsafe_allow_html=True)

# 5. Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Container for messages to control layout
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User Input at the bottom
if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with chat_container:
        with st.chat_message("user"):
            st.markdown(prompt)

    # Simulated "Thinking" animation
    with st.spinner("Analyzing intent..."):
        time.sleep(0.5) # Makes the bot feel more "human"
        result = process_user_input(prompt)

    # Bot Response
    with chat_container:
        with st.chat_message("assistant"):
            if result["status"] == "success":
                st.markdown(f"**Assistant:** {result['answer']}")
                st.caption(f"⚡ Routed to: {result['category']} | Confidence: {result['score']}")
            else:
                st.error(result["message"])
                response = result["message"]
    
    st.session_state.messages.append({"role": "assistant", "content": result.get('answer', result.get('message'))})