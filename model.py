import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load data
with open("intents.json") as file:
    data = json.load(file)

texts = []
labels = []
responses = {}

for intent in data["intents"]:
    tag = intent["tag"]
    responses[tag] = intent["responses"]

    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(tag)

# Convert text to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    prediction = model.predict(user_vec)[0]

    return random.choice(responses[prediction])