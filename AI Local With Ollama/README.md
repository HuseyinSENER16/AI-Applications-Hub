# 🔥 Running Local AI with Ollama: Complete Guide

<div align="center">

![Ollama Logo](https://github.com/jmorganca/ollama/assets/6827808/6e1837a9-aaaa-4e07-9d8b-c6d9d5c5e60a)
<br>
<span style="font-size: larger;">**Run and Deploy Local LLMs Effortlessly**</span>

</div>

---

## 📋 Table of Contents
- [Introduction](#introduction)
- [What is Ollama?](#what-is-ollama)
- [Installation](#installation)
- [Running Models](#running-models)
- [Configuration](#configuration)
- [API Usage](#api-usage)
- [Code Examples](#code-examples)
- [Performance Tips](#performance-tips)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)

---

## 💡 Introduction

Welcome to the world of **Local AI**! This guide will walk you through setting up, configuring, and using **Ollama** to run large language models (LLMs) locally on your machine. No cloud required, no privacy concerns, and full control over your AI models.

With Ollama, you can:
- 🚀 Run powerful LLMs like Llama 2, Llama 3, Mistral, and more
- 🛡️ Keep your data private and secure
- 💻 Work offline without internet dependency
- ⚙️ Customize and fine-tune models as needed
- 📦 Easy installation and management

---

## ❓ What is Ollama?

Ollama is a powerful, open-source framework that makes it easy to run large language models locally on your machine. Ollama packages machine learning models in containers, making them portable and easy to use across different platforms.

### Key Features:
- 📦 Simple packaging of LLMs with container technology
- 🌐 REST API for model interaction
- 🖥️ Cross-platform support (Windows, macOS, Linux)
- 🔧 Easy model management
- 🧠 Optimized for performance on consumer hardware
- 🔄 Continuous updates with new models

---

## ⚙️ Installation

### Windows Installation

#### Option 1: Download from Official Site
1. Go to [ollama.com](https://ollama.com) and download the Windows installer
2. Run the installer and follow the on-screen instructions
3. Restart your terminal/CMD to update PATH

#### Option 2: Using Package Managers

**Using Chocolatey:**
```powershell
choco install ollama
```

**Using Scoop:**
```powershell
scoop install ollama
```

#### Option 3: Windows Subsystem for Linux (WSL)
If you're using WSL, you can follow the Linux installation instructions:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### macOS Installation

**Using Homebrew:**
```bash
brew install ollama
```

**Using installer from website:**
1. Download from [ollama.com](https://ollama.com)
2. Install the .pkg file

### Linux Installation

**Using script:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Manual installation:**
```bash
# Download the binary
wget https://ollama.ai/download/ollama-linux-amd64.tgz
tar -xzf ollama-linux-amd64.tgz
sudo mv ollama /usr/bin/ollama

# Create the service
sudo tee /etc/systemd/system/ollama.service <<EOF
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3

[Install]
WantedBy=default.target
EOF

# Start the service
sudo systemctl daemon-reload
sudo systemctl start ollama
```

---

## 🚀 Running Models

### Starting Ollama

After installation, start the Ollama service:

**Windows:**
- The Ollama service should start automatically after installation
- Or manually start from the Start menu

**macOS/Linux:**
```bash
ollama serve
```

On Linux, if installed as a service:
```bash
sudo systemctl start ollama
```

### Popular Models to Try

Here are some popular models you can run with Ollama:

#### Llama Models
```bash
# Llama 3 (Recommended - most capable)
ollama pull llama3
ollama run llama3

# Llama 2 (Previous generation, still powerful)
ollama pull llama2
ollama run llama2
```

#### Other Popular Models
```bash
# Mistral (Great for efficiency)
ollama pull mistral

# Mixtral (Mistral's more powerful variant)
ollama pull mixtral

# CodeLlama (Specialized for code)
ollama pull codellama

# Phi-2 (Microsoft's small but capable model)
ollama pull phi

# Vicuna (Based on Llama 2, good for chat)
ollama pull vicuna
```

### Running a Model

Once you have a model downloaded, you can run it:

```bash
ollama run <model_name>
```

Example:
```bash
ollama run llama3
```

You'll enter an interactive chat session where you can ask questions and get responses from the model.

---

## ⚙️ Configuration

### Environment Variables

You can configure Ollama behavior using environment variables:

```bash
# Change where models are stored (default: ~/.ollama)
export OLLAMA_MODELS=/path/to/models

# Bind to a specific IP address (default: 127.0.0.1)
export OLLAMA_HOST=0.0.0.0

# Use a different port (default: 11434)
export OLLAMA_PORT=8080

# Enable additional logging
export OLLAMA_DEBUG=1
```

### GPU Configuration (if available)

Ollama automatically detects and uses available GPU hardware. To see if your GPU is being used:

```bash
# Check model information and GPU usage
ollama show <model_name> --modelfile
```

For NVIDIA GPUs (CUDA support):
- Ensure you have CUDA drivers installed
- Ollama will automatically use GPU acceleration when available

For more advanced GPU configuration, you can set:

```bash
# Force CUDA usage (NVIDIA)
export CUDA_VISIBLE_DEVICES=0

# Limit VRAM usage (in GB)
export OLLAMA_NUM_GPU=1  # Use 1 GPU
```

---

## 🌐 API Usage

Ollama provides a REST API that allows programmatic access to your models.

### API Endpoints

- `POST /api/generate` - Generate completions
- `POST /api/chat` - Chat completions
- `POST /api/embeddings` - Generate embeddings
- `GET /api/tags` - List local models
- `POST /api/pull` - Pull models from registry
- `DELETE /api/delete` - Delete models
- `POST /api/copy` - Copy models

### Example API Usage

#### Generate Text
```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3",
    "prompt": "Why is the sky blue?",
    "stream": false
  }'
```

#### Chat Completion
```bash
curl http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3",
    "messages": [
      {
        "role": "user",
        "content": "Why is the sky blue?"
      }
    ]
  }'
```

#### Stream Responses
```bash
curl http://localhost:11434/api/generate \
  -N \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3",
    "prompt": "Write a poem about AI",
    "stream": true
  }'
```

---

## 💻 Code Examples

### Python Example

Here's how to use Ollama with Python:

```python
import requests
import json

def generate_with_ollama(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result["response"]
    else:
        return f"Error: {response.status_code}"

# Example usage
prompt = "Explain quantum computing in simple terms"
result = generate_with_ollama(prompt)
print(result)
```

#### Using the Official Python Client

First install the client:
```bash
pip install ollama
```

Then use it:
```python
import ollama

# Generate text
response = ollama.generate(model='llama3', prompt='Why is the sky blue?')
print(response['response'])

# Chat completion
response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?'
    }
])
print(response['message']['content'])
```

### JavaScript/Node.js Example

```javascript
import ollama from 'ollama'

// Generate text
const response = await ollama.generate({
  model: 'llama3',
  prompt: 'Why is the sky blue?',
  stream: false,
})

console.log(response.response)

// Chat completion
const chatResponse = await ollama.chat({
  model: 'llama3',
  messages: [{ role: 'user', content: 'Why is the sky blue?' }],
})
console.log(chatResponse.message.content)
```

### Go Example

```go
package main

import (
    "context"
    "fmt"
    "github.com/ollama/ollama/api"
)

func main() {
    client, err := api.ClientFromEnvironment()
    if err != nil {
        panic(err)
    }

    req := &api.GenerateRequest{
        Model:  "llama3",
        Prompt: "Why is the sky blue?",
    }

    ctx := context.Background()
    respFunc := func(resp api.GenerateResponse) error {
        fmt.Print(resp.Response)
        return nil
    }

    err = client.Generate(ctx, req, respFunc)
    if err != nil {
        panic(err)
    }
}
```

---

## 💡 Performance Tips

### Memory Management

- **RAM**: Models need memory to operate. The larger the model, the more RAM required
- **VRAM**: For GPU acceleration, VRAM requirements vary by model
- **Swap**: Configure swap space on Linux if needed for large models

### Model Selection Based on Hardware

| Model | RAM Required | Best For |
|-------|-------------|----------|
| phi | < 4GB | Very weak hardware |
| mistral | 4-8GB | Good balance |
| llama2 | 8-16GB | Most laptops |
| llama3 | 8-16GB | Modern laptops |
| mixtral | 24GB+ | High-end systems |

### Optimization Settings

```bash
# Reduce context window to save memory
ollama run llama3 --options='{"num_ctx": 1024}'

# Reduce number of threads (for older CPUs)
ollama run llama3 --options='{"num_thread": 2}'

# Limit GPU usage
ollama run llama3 --options='{"num_gpu": 1}'
```

### Loading Multiple Models

Use `ollama serve` and HTTP API to load multiple models in different contexts:

```bash
# Start Ollama server
ollama serve &

# Use different models in your applications
curl -s http://localhost:11434/api/generate -d '{"model": "llama3", "prompt": "Hello"}'
curl -s http://localhost:11434/api/generate -d '{"model": "mistral", "prompt": "Hello"}'
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: "Failed to connect to Ollama server"
**Solutions:**
1. Make sure Ollama service is running:
   ```bash
   ollama serve
   ```
2. Check if service is running on the correct port:
   ```bash
   curl http://localhost:11434/api/tags
   ```

#### Issue: "CUDA error" on Windows/Linux
**Solutions:**
1. Check NVIDIA drivers: `nvidia-smi`
2. Ensure CUDA is properly installed
3. Verify compatibility between Ollama and CUDA versions

#### Issue: "Model not found"
**Solutions:**
1. Pull the model first: `ollama pull <model_name>`
2. Check available models: `ollama list`

#### Issue: "Out of memory"
**Solutions:**
1. Use smaller models
2. Increase swap space
3. Close other memory-intensive applications
4. Use CPU instead of GPU: `OLLAMA_NUM_GPU=0 ollama run <model>`

### Debugging Commands

```bash
# Check if server is running
curl http://localhost:11434

# List downloaded models
ollama list

# Show model information
ollama show <model_name>

# Check system resources
ollama -v

# Enable debug mode
export OLLAMA_DEBUG=1
```

---

## 📚 Resources

### Official Resources
- [Ollama Official Website](https://ollama.com)
- [Ollama GitHub Repository](https://github.com/ollama/ollama)
- [Ollama Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Ollama Models Library](https://ollama.ai/library)

### Model Information
- [Model Library](https://ollama.ai/library) - Browse and download various models
- [Model Cards](https://ollama.ai/library) - Detailed information about each model

### Community Resources
- [Ollama Discord](https://discord.gg/ollama) - Community support
- [GitHub Discussions](https://github.com/ollama/ollama/discussions) - Questions and discussions

### Tutorials and Examples
- [Official Examples](https://github.com/ollama/ollama/tree/main/examples) - Code examples in multiple languages
- [Community Tutorials](https://github.com/topics/ollama) - Community-created guides

---

## ✅ Conclusion

Running local AI with Ollama provides numerous advantages:

- **Privacy**: Your data never leaves your machine
- **Cost-effective**: No ongoing cloud costs
- **Control**: Full control over model parameters
- **Flexibility**: Works offline, customizable
- **Learning**: Great for understanding AI models

Start with smaller models like `phi` or `mistral` if you have limited hardware, and progressively try larger models like `llama3` as you get more familiar with the system.

Happy experimenting with local AI! 🎉

---

<div align="center">

**Made with ❤️ using Ollama**

*If you found this guide helpful, consider starring the Ollama project on GitHub!*

</div>