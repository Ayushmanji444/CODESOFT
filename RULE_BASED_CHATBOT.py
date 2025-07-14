# chatbot_gui.py
# Rule-based chatbot with GUI (Tkinter)
# Author: AYUSHMAN DWIVEDI

import tkinter as tk
from tkinter import scrolledtext

def get_bot_response(user_input):
    msg = user_input.lower()

    # Simple rule-based patterns
    if "hello" in msg or "hi" in msg:
        return "Hello there! How can I help you?"
    elif "how are you" in msg:
        return "I'm just code, but I'm doing great!"
    elif "your name" in msg:
        return "I'm RuleBot. Just a simple chatbot."
    elif "bye" in msg or "exit" in msg:
        return "Goodbye! Have a nice day!"
    elif "help" in msg:
        return "You can ask me about greetings, name, mood, or type 'bye' to quit."
    else:
        return "Sorry, I didn’t understand that. Try asking something else."

# Event handler for sending message
def send_message(event=None):
    user_text = user_input.get()
    if user_text.strip() == "":
        return

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_text + "\n")
    bot_reply = get_bot_response(user_text)
    chat_window.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    chat_window.config(state=tk.DISABLED)

    user_input.delete(0, tk.END)
    chat_window.yview(tk.END)

# GUI Setup
root = tk.Tk()
root.title("Rule-Based ChatBot")
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
user_input = tk.Entry(root, font=("Arial", 12))
user_input.pack(padx=10, pady=(0,10), fill=tk.X)
user_input.bind("<Return>", send_message)
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=(0,10))
chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, "Bot: Hi! I’m RuleBot. Type something to chat.\n\n")
chat_window.config(state=tk.DISABLED)
root.mainloop()
