import json
import pickle
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load JSON
with open("intents.json", "r") as file:
    data = json.load(file)

patterns = []
tags = []

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


# Extract patterns
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(clean_text(pattern))
        tags.append(intent["tag"])


print("Training patterns:", patterns)
print("Training tags:", tags)


# Convert text to numbers
vectorizer = TfidfVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(patterns)


# Train model
model = MultinomialNB()
model.fit(X, tags)


# Save files
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully!")
