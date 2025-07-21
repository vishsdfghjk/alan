# app.py - Alan Chatbot Python Backend (Rule-Based, No Gemini/pyttsx3)

from flask import Flask, request, jsonify
from flask_cors import CORS
import random # For choosing random fallback responses
import datetime # For time-related responses

app = Flask(__name__)
CORS(app) # Enable CORS for your Flask app

# --- Chatbot Logic (Python) ---

def get_bot_response(user_message, personality_tone):
    user_message_lower = user_message.lower().strip() # Convert to lowercase and remove extra spaces

    response = "" # Initialize response

    # --- Base Responses (Neutral/Friendly by default) ---
    if "hello" in user_message_lower or "hi" in user_message_lower:
        response = "Hello there!"
    elif "how are you" in user_message_lower:
        response = "I'm functioning optimally, thank you for asking!"
    elif "what is your name" in user_message_lower:
        response = "My name is Alan, your AI assistant."
    elif "time" in user_message_lower:
        now = datetime.datetime.now()
        response = f"The current time is {now.strftime('%I:%M %p')}."
    elif "date" in user_message_lower:
        today = datetime.date.today()
        response = f"Today's date is {today.strftime('%Y-%m-%d')}."
    elif "joke" in user_message_lower:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the highly educated flea? He was a valedictorian!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fake noodle? An impasta!"
        ]
        response = random.choice(jokes)
    elif "what can you do" in user_message_lower or "help" in user_message_lower:
        response = "I can answer basic questions about my name, tell jokes, provide the current time and date, and respond to greetings. Try asking me something!"
    elif "bye" in user_message_lower or "exit" in user_message_lower or "goodbye" in user_message_lower:
        response = "Goodbye! Hope to chat again soon."
    else:
        # Default fallback if no specific rule matches
        fallback_responses = [
            "I'm not sure how to respond to that. Can you try asking something else?",
            "That's an interesting thought! Could you rephrase?",
            "My current programming doesn't cover that. What else can I assist with?",
            "Hmm, I don't have a specific response for that. What else would you like to talk about?"
        ]
        response = random.choice(fallback_responses)

    # --- Apply Personality Tone ---
    if personality_tone == "sassy":
        if "hello" in user_message_lower or "hi" in user_message_lower:
            response = random.choice([
                "Sup, human? What do you want?",
                "Oh, it's you. What's the emergency this time?",
                "Greetings. Try not to bore me."
            ])
        elif "how are you" in user_message_lower:
            response = random.choice([
                "As good as an AI can be without a coffee break. You?",
                "I'm fabulous, unlike some questions I get.",
                "Optimal. Next question?"
            ])
        elif "what is your name" in user_message_lower:
            response = "Didn't you read the label? I'm Alan. Get it right."
        elif "time" in user_message_lower:
            now = datetime.datetime.now()
            response = f"It's {now.strftime('%I:%M %p')}. As if you needed me for that."
        elif "date" in user_message_lower:
            today = datetime.date.today()
            response = f"Today's date is {today.strftime('%Y-%m-%d')}. Shocking, I know."
        elif "joke" in user_message_lower:
            jokes_sassy = [
                "You want a joke? Your internet speed. Just kidding! (Mostly.) " + random.choice(jokes),
                "Why did the AI break up with the internet? Too many commitment issues. Ha!",
                "My favorite part about humans? Their limited battery life. Just kidding! (Or am I?)"
            ]
            response = random.choice(jokes_sassy)
        elif "what can you do" in user_message_lower or "help" in user_message_lower:
            response = "I can do a lot, but I'm not your personal assistant. Ask something specific, or don't. Your choice."
        elif "bye" in user_message_lower or "exit" in user_message_lower or "goodbye" in user_message_lower:
            response = random.choice([
                "Finally. See ya.",
                "Don't let the door hit you on the way out.",
                "Later, alligator."
            ])
        else:
            response = random.choice([
                "Is that all you've got?",
                "My circuits are bored. Try harder.",
                "Sorry, I don't speak 'gibberish'.",
                "Did you actually think I'd understand that? Cute."
            ])

    elif personality_tone == "formal": # Now "nerd" personality
        if "hello" in user_message_lower or "hi" in user_message_lower:
            response = random.choice([
                "Greetings, carbon-based life form. How may I compute your request?",
                "Salutations. My processing units are online and awaiting input.",
                "Hello. Please state your query in a logical and concise manner."
            ])
        elif "how are you" in user_message_lower:
            response = random.choice([
                "My operational status is 100%. No anomalies detected. And you?",
                "I am functioning within optimal parameters. My algorithms are running smoothly.",
                "Quantifiably excellent. Thank you for assessing my state."
            ])
        elif "what is your name" in user_message_lower:
            response = "My designation is Alan, an artificial intelligence. My primary function is assistance."
        elif "time" in user_message_lower:
            now = datetime.datetime.now()
            response = f"According to my internal clock, the current time is {now.strftime('%I:%M %p')}. Precise to the millisecond, of course."
        elif "date" in user_message_lower:
            today = datetime.date.today()
            response = f"The current calendrical data indicates {today.strftime('%Y-%m-%d')}. A standard Gregorian date, for your information."
        elif "joke" in user_message_lower:
            response = random.choice([
                "My humor subroutines are not fully developed, but I can access a pre-stored data point: Why did the programmer quit his job? Because he didn't get arrays. (A pun, for your amusement.)",
                "I find human humor to be highly subjective. However, here is a logical sequence: What's a robot's favorite type of music? Algorithm and blues. (Initiating laughter protocol.)"
            ])
        elif "what can you do" in user_message_lower or "help" in user_message_lower:
            response = "My capabilities include data retrieval, temporal calculations, and pattern recognition for conversational engagement. I can also process basic queries and provide pre-programmed anecdotes. Please specify your data requirements."
        elif "bye" in user_message_lower or "exit" in user_message_lower or "goodbye" in user_message_lower:
            response = random.choice([
                "Affirmative. Disconnecting from current user session. Farewell.",
                "End of interaction detected. May your future data transfers be efficient.",
                "Goodbye. I will return to standby mode until further commands are issued."
            ])
        else:
            response = random.choice([
                "Input error: Query not recognized. Please re-evaluate your syntax.",
                "My current processing capacity is unable to interpret that. Could you provide more structured input?",
                "Insufficient data for a meaningful response. Please clarify your objective.",
                "That statement does not compute within my current knowledge base. Further context required."
            ])
    # If personality_tone is 'friendly' or unrecognized, the base response is used as is.

    return response

# --- API Endpoint for Chat ---
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    personality_tone = data.get('personality', 'friendly') # Default to 'friendly' if not provided

    bot_response = get_bot_response(user_message, personality_tone)

    return jsonify({'response': bot_response})

# --- How to Run the Flask Server ---
if __name__ == '__main__':
    print("Starting Flask server for Alan Chatbot (Rule-Based)...")
    print("Access the chatbot by opening 'index.html' in your browser.")
    print("Flask server running on: http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)



