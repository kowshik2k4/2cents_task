def detect_doc_type(text):
    text_lower = text.lower()
    if "articles of association" in text_lower:
        return "Articles of Association"
    elif "memorandum of association" in text_lower:
        return "Memorandum of Association"
    elif "board resolution" in text_lower:
        return "Board Resolution"
    elif "ubo" in text_lower or "ultimate beneficial owner" in text_lower:
        return "UBO Declaration"
    elif "register of members" in text_lower:
        return "Register of Members and Directors"
    else:
        return "Unknown"
