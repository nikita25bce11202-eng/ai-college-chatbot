import json
import pickle
import random
import re
import datetime
import requests
import tkinter as tk
from tkinter import scrolledtext


# Load files
data = json.load(open("intents.json"))
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


# Clean text
def clean_text(text):

    text = text.lower()

    text = re.sub(r"[^\w\s]", "", text)

    # convert plural words to singular
    words = text.split()

    normalized_words = []

    for word in words:
        if word.endswith("s"):
            word = word[:-1]
        normalized_words.append(word)

    text = " ".join(normalized_words)

    return text


# Internet search (DuckDuckGo)
def search_internet(query):
    try:
        url = "https://api.duckduckgo.com/?q=" + query + "&format=json"
        response = requests.get(url).json()

        if response["Abstract"]:
            return response["Abstract"]
        else:
            return "I couldn't find a good answer online."
    except:
        return "Internet search is not available."


# AI Response
def get_response(user_input):

    user_input_clean = clean_text(user_input)

    vec = vectorizer.transform([user_input_clean])

    prediction = model.predict(vec)[0]
    confidence = max(model.predict_proba(vec)[0])

    print("Predicted:", prediction, "Confidence:", confidence)

    if confidence < 0.10:
        return search_internet(user_input)

    for intent in data["intents"]:
        if intent["tag"] == prediction:
            return random.choice(intent["responses"])

# Send message
def send():

    user_message = entry.get()

    if user_message == "":
        return

    chat_area.insert(tk.END, "You: " + user_message + "\n")

    response = get_response(user_message)

    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)


# GUI
window = tk.Tk()
window.title("AI College Chatbot")
window.geometry("500x600")
window.configure(bg="#1e1e1e")


chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    width=60,
    height=25,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 12)
)

chat_area.pack(pady=10)
chat_area.insert(tk.END, "Bot: Hello! Ask me anything.\n\n")


entry = tk.Entry(
    window,
    width=40,
    font=("Arial", 14)
)

entry.pack(side=tk.LEFT, padx=10, pady=10)


send_button = tk.Button(
    window,
    text="Send",
    command=send,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12)
)

send_button.pack(side=tk.LEFT)


window.mainloop()