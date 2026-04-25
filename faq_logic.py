import pandas as pd
from faq_engine import get_best_match, df 

HOT_WORDS = ["angry", "upset", "terrible", "manager", "lawsuit", "refund", "frustrated", "bad"]

# New: Basic "Manners" Dictionary
GREETINGS = {
    "hi": "Hello! I'm TechAssist. How can I help you with your electronics today?",
    "hello": "Hi there! What can I help you troubleshoot or find today?",
    "hey": "Hey! Need some help with your devices? Ask me anything!",
    "i need help": "I'm here to assist! You can ask me about smartphone resets, earbuds pairing, or order status.",
    "thanks": "You're very welcome! Is there anything else I can do for you?",
    "thank you": "Happy to help! Have a great day."
}

def process_user_input(user_input):
    clean_input = user_input.lower().strip()

    # 1. Check for Simple Manners/Greetings first
    if clean_input in GREETINGS:
        return {
            "status": "success",
            "answer": GREETINGS[clean_input],
            "category": "Greeting",
            "urgency": "Low",
            "score": 1.0
        }

    # 2. Check for Sentiment (Human Handoff Trigger)
    if any(word in clean_input for word in HOT_WORDS):
        return {
            "status": "handoff",
            "message": "I can see you're frustrated. I am transferring you to a Senior Support Specialist immediately to prioritize your request."
        }

    # 3. Get Match from the Semantic Engine
    idx, score = get_best_match(user_input)
    
    # 4. Check for Confidence
    if score < 0.45:
        return {
            "status": "handoff",
            "message": "I'm not quite sure I understand that specific request. Let me connect you with a live agent who can assist you better."
        }
    
    match = df.iloc[idx]
    return {
        "status": "success",
        "answer": match['answer'],
        "category": match['category'],
        "urgency": match['urgency'],
        "score": round(score, 2)
    }