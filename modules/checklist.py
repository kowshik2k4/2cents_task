# Example: ADGM Company Incorporation required docs
INCORPORATION_REQUIRED = [
    "Articles of Association",
    "Memorandum of Association",
    "Board Resolution",
    "UBO Declaration",
    "Register of Members and Directors"
]

def get_process_and_missing_docs(doc_types):
    # Simple process detection
    if any(dt in ["Articles of Association", "Memorandum of Association"] for dt in doc_types):
        process = "Company Incorporation"
        required_docs = INCORPORATION_REQUIRED
    else:
        process = "Unknown"
        required_docs = []
    
    missing = [doc for doc in required_docs if doc not in doc_types]
    return process, required_docs, missing
