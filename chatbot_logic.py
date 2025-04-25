def get_response(query, language):
    if "cough" in query.lower() or "खांसी" in query:
        if language == "English":
            return "You may have a Kapha disorder. Try Sitopaladi churna + honey."
        else:
            return "आपको कफ दोष हो सकता है। सितोपलादि चूर्ण + शहद लें।"
    elif "allergy" in query.lower() or "छीं" in query:
        if language == "English":
            return "Try Namshield Final – 5gm with ghee. Improves in 7–10 days."
        else:
            return "नमशील्ड फाइनल लें – 5 ग्राम घी के साथ। 7–10 दिन में लाभ होगा।"
    else:
        return "Please consult Vaidya Kael for further advice. / कृपया वैद्य कैल से संपर्क करें।"
