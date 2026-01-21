<<<<<<< HEAD
import streamlit as st
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Hugging Face API
api_key = os.getenv("HUGGINGFACE_API_TOKEN")
if not api_key:
    # Fallback/Placeholder if key is missing or is the old Gemini key
    api_key = ""

client = InferenceClient(token=api_key)

# Streamlit UI Configuration
st.set_page_config(page_title="Nova Intelligence", page_icon="⚡", layout="wide")

# Custom CSS for Premium UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* Remove Top Header */
    header {visibility: hidden;}
    
    /* Accent Gradient Text */
    h1 {
        background: linear-gradient(to right, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3.5rem;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0a0a0a;
        border-right: 1px solid #1f1f1f;
    }
    
    /* Chat Message styling */
    .stChatMessage {
        padding: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* User Message - Colorful Gradient */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px 20px 0 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        border: none;
    }
    
    /* Assistant Message - Clean Dark with Neon Border */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
        background: #111;
        border-radius: 20px 20px 20px 0;
        border: 1px solid #333;
        border-left: 4px solid #FF416C;
    }
    
    /* Text Input Field */
    div[data-testid="stChatInput"] input {
        background-color: #1a1a1a;
        color: white;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 12px;
    }
    
    div[data-testid="stChatInput"] input:focus {
        border-color: #FF416C;
        box-shadow: 0 0 10px rgba(255, 65, 108, 0.2);
    }
    
    /* Buttons */
    div.stButton > button {
        background: linear-gradient(to right, #FF4B2B, #FF416C);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255, 65, 108, 0.4);
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(255, 65, 108, 0.6);
    }
    
</style>
""", unsafe_allow_html=True)

st.title("Nova Intelligence")
st.caption("Advanced AI Assistant | Powered by Qwen 2.5")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Control Panel")
    
    # System Prompt (Persona)
    system_prompt = st.text_area(
        "🧠 System Persona", 
        value="You are Nova, a helpful and intelligent AI assistant.",
        help="Define how the AI should behave."
    )
    
    # Model Parameters
    temperature = st.slider("🌡️ Creativity", min_value=0.1, max_value=2.0, value=0.7, step=0.1)
    max_tokens = st.slider("📏 Max Length", min_value=50, max_value=2048, value=512, step=10)
    
    st.markdown("---")
    
    # Clear Chat Button
    if st.button("🗑️ Reset Memory"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("Designed with 💖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What's on your mind?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    if not api_key:
         st.error("⚠️ No Hugging Face API Token found. Please add HUGGINGFACE_API_TOKEN to your .env file.")
    else:
        try:
            # Prepare messages for API
            # Start with System Prompt
            api_messages = [{"role": "system", "content": system_prompt}] 
            
            # Add History
            api_messages += [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
            
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                # Call API with streaming
                stream = client.chat.completions.create(
                    model="Qwen/Qwen2.5-72B-Instruct", 
                    messages=api_messages, 
                    max_tokens=max_tokens,
                    temperature=temperature,
                    stream=True
                )
                
                # Use st.write_stream to handle the stream generator
                response_text = st.write_stream(
                    chunk.choices[0].delta.content 
                    for chunk in stream 
                    if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content
                )
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
=======
import streamlit as st
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Hugging Face API
api_key = os.getenv("HUGGINGFACE_API_TOKEN")
if not api_key:
    # Fallback/Placeholder if key is missing or is the old Gemini key
    api_key = ""

client = InferenceClient(token=api_key)

# Streamlit UI Configuration
st.set_page_config(page_title="Nova Intelligence", page_icon="⚡", layout="wide")

# Custom CSS for Premium UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* Remove Top Header */
    header {visibility: hidden;}
    
    /* Accent Gradient Text */
    h1 {
        background: linear-gradient(to right, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3.5rem;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0a0a0a;
        border-right: 1px solid #1f1f1f;
    }
    
    /* Chat Message styling */
    .stChatMessage {
        padding: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* User Message - Colorful Gradient */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px 20px 0 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        border: none;
    }
    
    /* Assistant Message - Clean Dark with Neon Border */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
        background: #111;
        border-radius: 20px 20px 20px 0;
        border: 1px solid #333;
        border-left: 4px solid #FF416C;
    }
    
    /* Text Input Field */
    div[data-testid="stChatInput"] input {
        background-color: #1a1a1a;
        color: white;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 12px;
    }
    
    div[data-testid="stChatInput"] input:focus {
        border-color: #FF416C;
        box-shadow: 0 0 10px rgba(255, 65, 108, 0.2);
    }
    
    /* Buttons */
    div.stButton > button {
        background: linear-gradient(to right, #FF4B2B, #FF416C);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255, 65, 108, 0.4);
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(255, 65, 108, 0.6);
    }
    
</style>
""", unsafe_allow_html=True)

st.title("Nova Intelligence")
st.caption("Advanced AI Assistant | Powered by Qwen 2.5")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Control Panel")
    
    # System Prompt (Persona)
    system_prompt = st.text_area(
        "🧠 System Persona", 
        value="You are Nova, a helpful and intelligent AI assistant.",
        help="Define how the AI should behave."
    )
    
    # Model Parameters
    temperature = st.slider("🌡️ Creativity", min_value=0.1, max_value=2.0, value=0.7, step=0.1)
    max_tokens = st.slider("📏 Max Length", min_value=50, max_value=2048, value=512, step=10)
    
    st.markdown("---")
    
    # Clear Chat Button
    if st.button("🗑️ Reset Memory"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("Designed with 💖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What's on your mind?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    if not api_key:
         st.error("⚠️ No Hugging Face API Token found. Please add HUGGINGFACE_API_TOKEN to your .env file.")
    else:
        try:
            # Prepare messages for API
            # Start with System Prompt
            api_messages = [{"role": "system", "content": system_prompt}] 
            
            # Add History
            api_messages += [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
            
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                # Call API with streaming
                stream = client.chat.completions.create(
                    model="Qwen/Qwen2.5-72B-Instruct", 
                    messages=api_messages, 
                    max_tokens=max_tokens,
                    temperature=temperature,
                    stream=True
                )
                
                # Use st.write_stream to handle the stream generator
                response_text = st.write_stream(
                    chunk.choices[0].delta.content 
                    for chunk in stream 
                    if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content
                )
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
>>>>>>> 7f293982e1e326780625a14d1ac13f09b78c5a17
