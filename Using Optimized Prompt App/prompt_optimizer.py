import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog
from typing import Optional
import google.generativeai as genai
import os
import threading
import time

def get_api_key():
    """Get the Gemini API key from environment variable or user input."""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        api_key = simpledialog.askstring("API Key", "Enter your Gemini API key:", show='*')
        if api_key:
            os.environ['GEMINI_API_KEY'] = api_key
    return api_key

def optimize_prompt_logic(raw_text: str) -> str:
    """
    Function to optimize prompt using Gemini API with the provided template.

    Args:
        raw_text: The input prompt text to optimize

    Returns:
        The optimized prompt text
    """
    if not raw_text.strip():
        return "Please enter a prompt to optimize."

    # Get API key
    api_key = get_api_key()
    if not api_key:
        return "API key is required to use the optimization service."

    try:
        # Configure the API
        genai.configure(api_key=api_key)

        # Read the template from the markdown file
        template_path = os.path.join(os.path.dirname(__file__), "OptimizedPrompt.md")
        if not os.path.exists(template_path):
            return f"Template file not found: {template_path}"

        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        # Replace the placeholder in the template with the raw prompt
        prompt_to_send = template_content.replace("[INSERT RAW PROMPT HERE]", raw_text)

        # Initialize the model - using the gemini-3-flash-preview model
        model = genai.GenerativeModel('gemini-3-flash-preview')

        # Generate content
        response = model.generate_content(prompt_to_send)

        # Return the optimized prompt
        if response.text:
            return response.text.strip()
        else:
            return "Could not generate an optimized prompt. Please try again."

    except Exception as e:
        return f"Error occurred while optimizing prompt: {str(e)}"

class PromptOptimizerApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.setup_ui()

    def setup_ui(self) -> None:
        """Set up the user interface with proper layout and styling."""
        self.root.title("Prompt Optimization Tool")
        self.root.geometry("800x600")

        # Configure grid weights for resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Configure style
        style = ttk.Style()
        style.theme_use('clam')  # Use a clean theme
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        style.configure("TButton", padding=10, font=("Arial", 10))
        style.configure("Accent.TButton", foreground="white", background="#007acc")

        # Main container frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)  # Raw text area
        main_frame.grid_rowconfigure(2, weight=0)  # Button area (no expansion)
        main_frame.grid_rowconfigure(3, weight=0)  # Progress bar area (no expansion)
        main_frame.grid_rowconfigure(4, weight=0)  # Label (no expansion)
        main_frame.grid_rowconfigure(5, weight=2)  # Optimized text area (more space)
        main_frame.grid_columnconfigure(0, weight=1)

        # Top section: Raw prompt input
        raw_label = ttk.Label(main_frame, text="Prompt", font=("Arial", 12, "bold"))
        raw_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.raw_text_area = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            width=80,
            height=4,  # Reduced to 4 lines
            font=("Arial", 10),
            padx=10,
            pady=5
        )
        self.raw_text_area.grid(row=1, column=0, sticky="nsew", pady=(0, 20))

        # Center section: Optimize button
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=10)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        self.optimize_button = ttk.Button(
            button_frame,
            text="Optimize",
            command=self.optimize_prompt,
            style="Accent.TButton"
        )
        self.optimize_button.grid(row=0, column=0, padx=(0, 5))

        self.api_key_button = ttk.Button(
            button_frame,
            text="Set API Key",
            command=self.set_api_key
        )
        self.api_key_button.grid(row=0, column=1, padx=(5, 0))

        # Progress bar section
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            length=300
        )
        self.progress.grid(row=3, column=0, pady=10, sticky="ew")
        self.progress.grid_remove()  # Initially hidden

        # Bottom section: Optimized prompt output
        optimized_label = ttk.Label(main_frame, text="Optimized Prompt", font=("Arial", 12, "bold"))
        optimized_label.grid(row=4, column=0, sticky="w", pady=(20, 5))

        self.optimized_text_area = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            width=80,
            height=16,  # Increased to accommodate more lines
            font=("Arial", 10),
            state=tk.DISABLED,  # Set to read-only
            padx=10,
            pady=5
        )
        self.optimized_text_area.grid(row=5, column=0, sticky="nsew")

    def set_api_key(self) -> None:
        """Allow user to set the API key."""
        api_key = simpledialog.askstring("API Key", "Enter your Gemini API key:", show='*')
        if api_key:
            os.environ['GEMINI_API_KEY'] = api_key
            messagebox.showinfo("Success", "API key has been set successfully!")

    def optimize_prompt(self) -> None:
        """Handle the optimization process when the button is clicked."""
        # Get the raw text
        raw_text = self.raw_text_area.get("1.0", tk.END).strip()

        # Enable the progress bar
        self.progress.grid()  # Make progress bar visible
        self.progress.start(10)  # Start the animation

        # Disable the optimize button to prevent multiple requests
        self.optimize_button.config(state=tk.DISABLED)

        # Run the optimization in a separate thread to prevent UI freezing
        threading.Thread(
            target=self._optimize_prompt_thread,
            args=(raw_text,),
            daemon=True
        ).start()

    def _optimize_prompt_thread(self, raw_text: str) -> None:
        """Run the optimization in a separate thread."""
        # Call the optimization function
        optimized_text = optimize_prompt_logic(raw_text)

        # Update the UI in the main thread
        self.root.after(0, self._update_ui_with_result, optimized_text)

    def _update_ui_with_result(self, optimized_text: str) -> None:
        """Update the UI with the result from the background thread."""
        # Stop and hide the progress bar
        self.progress.stop()
        self.progress.grid_remove()

        # Re-enable the optimize button
        self.optimize_button.config(state=tk.NORMAL)

        # Update the optimized text area
        self.optimized_text_area.config(state=tk.NORMAL)  # Temporarily enable to update
        self.optimized_text_area.delete("1.0", tk.END)
        self.optimized_text_area.insert("1.0", optimized_text)
        self.optimized_text_area.config(state=tk.DISABLED)  # Set back to read-only

def main() -> None:
    """Main entry point for the application."""
    root = tk.Tk()
    app = PromptOptimizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()