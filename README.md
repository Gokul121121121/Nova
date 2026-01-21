# ✨ Nova Intelligence

**Nova Intelligence** is a modern, AI-powered chatbot designed to assist users with coding, creative writing, and problem-solving through a sleek, premium interface.

## 🎯 Problem Statement
In today's fast-paced digital environment, users often struggle to find accessible, high-quality AI assistance that is both visually appealing and functionally robust without expensive subscriptions. **Nova Intelligence** bridges this gap by providing a free, open-source interface to top-tier LLMs (Large Language Models) like Qwen 2.5 and Mistral 7B, wrapped in a native-app-like experience.

## 🏗️ Architecture
This project is built using:
- **Frontend**: [Streamlit](https://streamlit.io/) (Python-based web app framework).
- **Backend/AI**: [Hugging Face Inference API](https://huggingface.co/inference-api) (Serverless access to open-source models).
- **Model**: `Qwen/Qwen2.5-72B-Instruct` (A state-of-the-art open model optimized for chat and instruction following).

### Key Features
- **🧠 Memory**: Maintains conversation context using session state.
- **⚡ Streaming**: Real-time token-by-token response generation.
- **🎨 Premium UI**: Custom dark-mode aesthetic with glassmorphism and gradient accents.
- **⚙️ Configurable**: Adjustable 'Creativity' (Temperature) and 'System Persona'.

## 🚀 Setup Instructions

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Gokul121121121/Nova.git
    cd Nova
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**
    Create a `.env` file in the root directory and add your Hugging Face Token:
    ```
    HUGGINGFACE_API_TOKEN=hf_your_token_here
    ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 🤖 AI Services Used
- **Hugging Face Hub**: We utilize the `huggingface_hub` Python library to communicate with the Inference API.
- **LLM**: The primary model is **Qwen 2.5**, selected for its high performance on reasoning and coding tasks.

## 🎥 Project Demo
[Link to Video Demo] (To be added)

---
*Created for the AI/ML Internship Assessment.*
