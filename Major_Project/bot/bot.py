import pyttsx3
import speech_recognition as sr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Training data for chatbot
data = {
    "greetings": ["hello", "hi", "hey"],
    "farewells": ["bye", "goodbye"],
    "bot_identity": ["what is your name", "who are you", "introduce yourself"],
    "inquiries_1": ["how are you", "how is it going", "what's up"],
    "inquiries_2": ["what are you doing", "what's happening", "what's new"],
    "inquiries_3": ["can you help me", "I need assistance", "can you assist me"],
    "inquiries_4": ["where are you from", "where do you come from", "what is your origin"],
    "inquiries_5": ["how do you work", "how are you built", "how were you created"],
    "inquiries_6": ["what can you do", "what are your features", "how can you help me"],
    "inquiries_7": ["what time is it", "do you know the time", "tell me the current time"],
    "inquiries_8": ["what's the weather like", "is it raining", "how's the weather today"],
    "inquiries_9": ["do you like music", "what's your favorite song", "can you sing"],
    "inquiries_10": ["what's your favorite color", "do you have a favorite color", "what color do you like"],
    "inquiries_11": ["tell me a joke", "do you know any jokes", "make me laugh"],
    "inquiries_12": ["tell me a fact", "do you know any facts", "share some trivia"],
    "inquiries_13": ["can you learn", "do you evolve", "how do you improve"],
    "inquiries_14": ["are you human", "do you have feelings", "are you alive"],
    "inquiries_15": ["how do I contact support", "can you provide support details", "help me with support"]
}

responses = {
    "greetings": "Hello!",
    "farewells": "Goodbye! Have a great day!",
    "bot_identity": "I'm Convo Bot, how can I assist you?",
    "inquiries_1": "I'm going great! Thanks for asking.",
    "inquiries_2": "Not much, just here to help you!",
    "inquiries_3": "Of course! Let me know how I can assist.",
    "inquiries_4": "I'm from the digital world, created to assist you.",
    "inquiries_5": "I work using advanced algorithms and AI technologies.",
    "inquiries_6": "I can help with answering questions, providing information, and much more!",
    "inquiries_7": "I don't have a clock, but you can check your device for the time.",
    "inquiries_8": "I can't check weather updates, but you can try a weather app!",
    "inquiries_9": "I don't listen to music, but I hear people love all kinds of genres!",
    "inquiries_10": "I don't have a favorite color, but I appreciate them all!",
    "inquiries_11": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "inquiries_12": "Did you know octopuses have three hearts?",
    "inquiries_13": "I learn and improve with updates and interactions!",
    "inquiries_14": "I'm not human, just a bot designed to assist you!",
    "inquiries_15": "You can contact support via the help center or by emailing support@convobot.com."
}

# Prepare training data
X_train = []
y_train = []
for intent, phrases in data.items():
    X_train.extend(phrases)
    y_train.extend([intent] * len(phrases))

# Build an NLP pipeline
model = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')), ('clf', MultinomialNB())])

# Train the model
model.fit(X_train, y_train)

# Initialize the speech engine for TTS
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chatbot(user_input):
    intent = model.predict([user_input])[0]
    return responses.get(intent, "I'm not sure how to respond to that. Can you try asking something else?")

# Voice Input (Speech-to-Text)
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that. Please try again.")
        return None
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech service.")
        return None
