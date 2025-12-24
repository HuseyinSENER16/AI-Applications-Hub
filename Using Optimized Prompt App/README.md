# 🚀 Prompt Optimization Tool

A Python application that uses the Google Gemini API to optimize prompts based on a predefined template.

## ✨ Features

- 🖥️ Clean, user-friendly interface with input and output text areas
- 🔗 Integration with Google Gemini API for prompt optimization using the gemini-3-flash-preview model
- 📝 Template-based optimization using the OptimizePrompt.md template
- 🔐 API key management

## 📋 Requirements

- 🐍 Python 3.7+
- 📦 Google Generative AI library (`google-generativeai`)
- 🆓 Google API key (using gemini-3-flash-preview model) - can be set as environment variable

## 🛠️ Setup

1. Install the required library:
   ```bash
   pip install google-generativeai
   ```

2. Obtain a Google API key from the [Google AI Studio](https://aistudio.google.com/)

3. (Optional) Set the API key as an environment variable:
   ```bash
   # On Windows
   set GEMINI_API_KEY=your_api_key_here

   # On macOS/Linux
   export GEMINI_API_KEY=your_api_key_here
   ```

## 🎯 Usage

1. Run the application:
   ```bash
   python prompt_optimizer.py
   ```

2. 📝 Enter your raw prompt in the "Prompt" text area

3. 🔐 Click the "Set API Key" button and enter your API key (or set the `GEMINI_API_KEY` environment variable beforehand)

4. ⚡ Click the "Optimize" button to get the optimized prompt

5. 📋 The optimized prompt will appear in the "Optimized Prompt" text area

## 🔍 How It Works

The application uses the template provided in `OptimizedPrompt.md` to structure the optimization request to the Google AI API. The raw prompt entered by the user replaces the `[INSERT RAW PROMPT HERE]` placeholder in the template, and the `gemini-3-flash-preview` model generates an optimized version based on the template's structure and guidelines.

## 📝 Notes

- 🤔 The application will prompt for an API key if it's not already set in the environment
- 🔒 The "Optimized Prompt" area is read-only to prevent accidental changes
- 📐 The window is resizable for better user experience