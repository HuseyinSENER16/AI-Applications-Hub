# Local Chatbot Using Chainlit

This project demonstrates how to create a 100% local chatbot that runs entirely on your machine without any external dependencies. It uses Chainlit for the UI and Ollama for local LLM processing with the Llama3.2-Vision model.

## Features

- 100% Local Processing: No external APIs or internet required after setup
- Beautiful UI: Chainlit provides an elegant chat interface
- Vision Support: Can process images using Llama3.2-Vision model
- Streaming Responses: Real-time token streaming for natural interaction
- File Upload: Supports image uploads for multimodal interactions
- Conversation Memory: Maintains context throughout the chat session

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- Downloaded model (e.g., `granite4:350m`)

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure Ollama is running: `ollama serve`
4. Pull the model: `ollama pull granite4:350m`
5. Run the application: `chainlit run Test.py`

For more detailed information, check out the full documentation in [GUIDE.md](GUIDE.md).