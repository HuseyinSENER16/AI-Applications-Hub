# 🤖 Building a 100% Local Chatbot with Chainlit and Ollama

Welcome to a comprehensive guide on creating a fully local chatbot that runs entirely on your machine without any external dependencies. This implementation uses Chainlit for the UI and Ollama for local LLM processing.

## 📋 Table of Contents
- [✨ Features](#features)
- [🔧 Prerequisites](#prerequisites)
- [🚀 Getting Started](#getting-started)
- [📋 Code Structure](#code-structure)
- [💻 Detailed Code Explanation](#detailed-code-explanation)
- [📸 Screenshots](#screenshots)
- [🔄 How It Works](#how-it-works)
- [💡 Customization Tips](#customization-tips)
- [🚀 Future Enhancements](#future-enhancements)

## ✨ Features

- 🏠 **100% Local Processing**: No external APIs or internet required after setup
- 🎨 **Beautiful UI**: Chainlit provides an elegant chat interface
- 👁️ **Vision Support**: Can process images using Llama3.2-Vision model
- 📝 **Streaming Responses**: Real-time token streaming for natural interaction
- 📁 **File Upload**: Supports image uploads for multimodal interactions
- 🧠 **Conversation Memory**: Maintains context throughout the chat session

## 🔧 Prerequisites

Before running the application, ensure you have:

- 🐍 Python 3.8+ installed
- 🦙 [Ollama](https://ollama.ai/) installed and running
- 🧠 Downloaded a compatible model (e.g., `granite4:350m` as used in the code)
- 🧩 Required Python packages: `chainlit`, `ollama`

Install the required packages:
```bash
pip install chainlit ollama
```

Pull the required model:
```bash
ollama pull granite4:350m
```

## 🚀 Getting Started

1. Clone or download the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure Ollama is running: `ollama serve`
4. Pull the model: `ollama pull granite4:350m`
5. Run the application: `chainlit run Test.py`
6. Open your browser to the provided URL (usually http://localhost:8000)

## 📋 Code Structure

```text
Test.py
├── Import Statements
├── Chat Session Initialization
│   └── System Role Setup
├── Tool Function
│   ├── Message History Management
│   ├── Image Processing
│   └── Ollama Interaction
├── Message Handler
│   ├── Image Detection
│   ├── Response Streaming
│   └── User Interaction
└── Execution Flow
```

## 💻 Detailed Code Explanation

### 1. 📦 **Import Statements**

```python
import chainlit as cl
import ollama
```

- `chainlit` provides the UI framework for our chatbot
- `ollama` enables interaction with local LLMs

### 2. 🎯 **Chat Session Initialization**

```python
@cl.on_chat_start
async def start_chat():
    cl.user_session.set(
        "interaction",
        [
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            }
        ],
    )

    msg = cl.Message(content="")

    start_message = "Hello, I'm your 100% local alternative to ChatGPT running on Llama3.2-Vision. How can I help you today?"

    for token in start_message:
        await msg.stream_token(token)

    await msg.send()
```

This function runs when a new chat session begins:

- ✅ **Session Setup**: Creates an initial conversation history with a system prompt
- ✅ **Welcome Message**: Creates a streaming welcome message to the user
- ✅ **User Experience**: The message appears character by character for a natural feel

### 3. ⚙️ **Tool Function**

```python
@cl.step(type="tool")
async def tool(input_message, image=None):

    interaction = cl.user_session.get("interaction")

    if image:
        interaction.append({"role": "user",
                            "content": input_message,
                            "images": image})
    else:
        interaction.append({"role": "user",
                            "content": input_message})

    response = ollama.chat(model="granite4:350m",
                           messages=interaction)

    interaction.append({"role": "assistant",
                        "content": response.message.content})

    return response
```

This function handles the core interaction logic:

- 🔍 **History Management**: Retrieves the current conversation history
- 🖼️ **Multimodal Support**: Adds user message with or without images
- 🧠 **LLM Processing**: Calls the local Ollama model with the conversation history
- 📥 **Response Storage**: Saves the AI's response to the conversation history
- 📤 **Return**: Returns the model's response for further processing

### 4. 📨 **Message Handler**

```python
@cl.on_message
async def main(message: cl.Message):

    images = [file for file in message.elements if "image" in file.mime]

    if images:
        tool_res = await tool(message.content, [i.path for i in images])

    else:
        tool_res = await tool(message.content)

    msg = cl.Message(content="")

    for token in tool_res.message.content:
        await msg.stream_token(token)

    await msg.send()
```

This function processes each user message:

- 🖼️ **Image Detection**: Checks if the message contains images
- 🔧 **Tool Execution**: Calls the tool function with or without images
- 💬 **Response Streaming**: Streams the AI's response token by token
- 📤 **Message Delivery**: Sends the complete response to the user

## 📸 Screenshots

### 🖥️ Local Chatbot Interface
```
┌─────────────────────────────────────────┐
│    Local Chatbot Interface             │
├─────────────────────────────────────────┤
│                                         │
│  💬 Hello, I'm your 100% local          │
│      alternative to ChatGPT running     │
│      on Llama3.2-Vision. How can       │
│      I help you today?                 │
│                                         │
│  [Type your message here...]           │
│                                         │
└─────────────────────────────────────────┘
```

## 🔄 How It Works

1. 🚀 **Initialization**: When the chat starts, a system message is set up
2. 🎉 **Welcome**: A streaming welcome message is displayed to the user
3. 📨 **User Input**: When a user sends a message:
   - The system checks for images in the message
   - The message (with or without images) is sent to the Ollama model
   - Conversation history is maintained for context
4. 🤖 **AI Response**: The local model processes the input and generates a response
5. 📤 **Delivery**: The response is streamed token by token to the user
6. 🔄 **Loop**: The process repeats for the next message

## 💡 Customization Tips

### 🧠 **Changing Models**
To use a different model, replace `"granite4:350m"` with your preferred model:
```python
response = ollama.chat(model="your-preferred-model", messages=interaction)
```

### 🎨 **Customizing System Prompt**
Modify the system message in the `start_chat()` function:
```python
{
    "role": "system",
    "content": "You are a custom helpful assistant with specific capabilities.",
}
```

### 🖼️ **Enhanced Vision Processing**
Add image preprocessing capabilities by extending the image handling in the tool function.

## 🚀 Future Enhancements

- 📄 **Document Processing**: Add support for PDF, DOCX and other document formats
- 🎯 **Fine-tuning**: Implement custom fine-tuning capabilities
- 🔐 **Privacy Controls**: Add enhanced privacy and data handling options
- 🌐 **Multi-language Support**: Add support for multiple languages
- ⚡ **Performance Optimization**: Implement caching and optimization techniques

## 📚 Resources

- [Chainlit Documentation](https://docs.chainlit.io/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Local LLM Models](https://ollama.ai/library)

## 🤝 Contributing

We welcome contributions to improve this local chatbot implementation! Feel free to submit issues or pull requests to enhance functionality.

## 📝 License

This project is open source and available under the MIT License.