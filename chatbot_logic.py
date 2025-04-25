
import json
import random

def get_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "namaste", "pranam"]
    if any(word in user_input for word in greetings):
        return random.choice([
            "Namaste! Kaise madad kar sakta hoon?",
            "Hello! How can I assist you with Ayurveda today?",
            "Pranam! Apka swagat hai Aryanam mein."
        ])

    try:
        with open("ayurveda_db.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except:
        return "Knowledge base not loaded. Please contact Kael."

    for disease, info in data.items():
        if disease.lower() in user_input:
            return (
                f"🩺 **{disease}**\n\n"
                f"📖 Description: {info.get('description')}\n\n"
                f"🌿 Suggested Herbs: {', '.join(info.get('herbs', []))}\n\n"
                f"🍽️ Diet Advice: {', '.join(info.get('diet', []))}\n\n"
                f"💊 Formulation: {info.get('recommended_formulation')}"
            )

    return "I'm still learning. Would you like to add this to my brain, Kael?"
