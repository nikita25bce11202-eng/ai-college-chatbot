# ai-college-chatbot

## Project Overview

The **AI College Chatbot** is a Python-based chatbot designed to help students quickly get information about college-related topics such as exams, results, hostel rules, mess timings, attendance requirements, and campus facilities.

The chatbot uses **Natural Language Processing (NLP)** and a **machine learning intent classification model** to understand user questions and respond appropriately.

If the chatbot cannot find a suitable response in its knowledge base, it can optionally attempt to search the internet for relevant information.


## Features

* Conversational chatbot interface
* Machine learning based intent detection
* Predefined knowledge base using JSON (`intents.json`)
* Handles common college queries
* Fallback response if the query is unknown
* Simple command-line interface (can be extended to GUI)

## Technologies Used

* Python
* JSON for storing chatbot knowledge
* Machine Learning with `scikit-learn`
* NLP preprocessing
* Requests library for optional internet search

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nikita25bce11202-eng/ai-college-chatbot.git
cd ai-college-chatbot
```

### 2. Install Dependencies

Install required Python libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install scikit-learn requests
```

### 3. Train the Chatbot Model

Run the training script to train the intent classifier.

```bash
python train_model.py
```

This will create the trained model files used by the chatbot.

### 4. Run the Chatbot

Start the chatbot using:

```bash
python chatbot.py

You will see:

Bot: Hello! Ask me anything.

You can then start asking questions.

Example:
You: hi
Bot: Hello!

You: result
Bot: Results will be announced on VTOP.

You: mess timing
Bot: breakfast-7:30-9:30,lunch-12:30-2:30,snacks-5:00-6:30,dinner-7:30-9:15

## Example Questions You Can Ask

* hi / hello
* exam date
* result date
* hostel timing
* mess timing
* attendance criteria
* placement details
* library timing


## Future Improvements

* Add graphical chatbot interface (GUI)
* Improve NLP accuracy
* Connect chatbot to real college database
* Deploy chatbot as a web application
* Add voice interaction


