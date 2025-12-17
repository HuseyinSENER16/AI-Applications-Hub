# 🚀 Creating a Simple RAG Workflow Using Local LLM

This project demonstrates how to build a **Retrieval-Augmented Generation (RAG)** workflow using **LlamaIndex** and local LLMs. It allows you to chat with your private documents entirely offline, ensuring data privacy and reducing latency.

---

## 📖 Overview

**RAG (Retrieval-Augmented Generation)** is a powerful technique that enhances LLM capabilities by retrieving relevant information from a specific dataset before generating a response. This ensures the model's output is grounded in factual, provided data rather than just its training knowledge.

### Why LlamaIndex Workflows?
This project utilizes the new **LlamaIndex Workflows** API, which provides:
- **Event-Driven Architecture**: Each step in the RAG process (Ingestion, Retrieval, Synthesis) is triggered by events.
- **Modularity**: Easily swap out components (e.g., use a different retriever or LLM).
- **Asynchronous Execution**: Designed for high-performance, non-blocking operations.

---

## 🛠️ Tech Stack

- 🦙 **LlamaIndex**: Data framework for LLM applications.
- 📦 **Ollama**: Local LLM runner.
- 🤗 **HuggingFace**: Embedding models (`bge-small-en-v1.5`).
- 🐍 **Python**: Core programming language.
- 📓 **Jupyter Notebook**: Interactive exploration.

---

## 📂 Project Structure

```text
Creating Simple RAG Workflow Using Local LLM/
├── data/                    # 📁 Your documents go here
│   └── History_Moment.txt   # Example text file
├── RAGExampleApp.py         # 🐍 Core workflow implementation
├── RAGExampleApp.ipynb      # 📓 Interactive notebook version
├── requirements.txt         # 📋 Python dependencies
├── env.example              # ⚙️ Environment variable template
└── README.md                # 📖 Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Install [Ollama](https://ollama.ai/) and pull the required model:
  ```bash
  ollama pull granite4:350m
  ```

### 2. Installation
Clone the repository and install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Usage

#### Run the Python Script:
```bash
python RAGExampleApp.py
```

#### Steps Involved:
1.  **Ingestion** 📥: The script reads document(s) from the `data/` folder.
2.  **Indexing** 🗂️: It converts the text into vector embeddings and stores them in a Vector Store Index.
3.  **Retrieval** 🔍: When a query is made, it finds the most relevant document chunks.
4.  **Synthesis** ✍️: The LLM generates a response based on the retrieved context.

---

## 💡 Example

**Query:** *"How old was Sultan Mehmed when he became the leader of the Ottoman Empire?"*

**RAG Process:**
1.  Searches `History_Moment.txt` for "Sultan Mehmed leader age".
2.  Retrieves the relevant paragraph.
3.  Synthesizes the answer: *"Sultan Mehmed II was 12 years old when he first ascended to the throne in 1444..."*

---

## 🔧 Workflow Customization

You can change the models easily in `RAGExampleApp.py`:

```python
# Customizing the models
workflow = RAGWorkflow(
    model_name="llama3", 
    embedding_model="sentence-transformers/all-MiniLM-L6-v2"
)
```

---

## 🔐 Privacy
Since everything runs locally via Ollama and HuggingFace, your data **never leaves your machine**. 

---
*Created with ❤️ for AI Application Hub.*
