# 🧠 Streamlit Thinking UI with Ollama

This project demonstrates how to implement a **"Thinking UI"** in a Streamlit chat application, similar to how modern reasoning models (like DeepSeek-R1 or Qwen-2.5-Coder) display their internal monologue.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Features

- **💡 Thinking Phase Visualization**: Dedicated UI state using `st.status` to show the model's reasoning process in real-time.
- **🌊 Real-time Streaming**: Full support for streaming responses from Ollama, providing a responsive and fluid chat experience.
- **📜 Persistent Reasoning History**: Long-term chat history preserves the "thinking" blocks within `st.expander` components, allowing you to review the model's logic for past messages.
- **🤖 Ollama Integration**: Powered by local LLMs via Ollama (configured for `qwen3:4b`).
- **🎨 Premium Chat Interface**: Clean, modern chat UI using Streamlit's native chat elements.

## 🚀 How it Works

The application splits the LLM response into two distinct phases:

1.  **Thinking Phase**: The app detects the `<think>` tag and starts capturing content into a status container.
2.  **Response Phase**: Once the `</think>` tag is encountered, the status container closes, and the final answer is streamed directly into the chat message.

## 🛠️ Setup & Installation

1.  **Install dependencies**:
    ```bash
    pip install streamlit ollama
    ```

2.  **Ensure Ollama is running** and you have the model pulled:
    ```bash
    ollama pull qwen3:4b
    ```

3.  **Run the application**:
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure

- `app.py`: The main application logic containing the streaming handlers and Streamlit UI components.
- `assets/`: (Optional) Directory for UI assets like logos.

---

*Built with ❤️ using Streamlit and Ollama.*
