def run_basic_checks(doc_type, text):
    issues = []
    if "uae federal courts" in text.lower():
        issues.append({
            "document": doc_type,
            "issue": "Jurisdiction clause does not specify ADGM",
            "severity": "High",
            "suggestion": "Update jurisdiction to ADGM Courts."
        })
    if "signature" not in text.lower() and "signed" not in text.lower():
        issues.append({
            "document": doc_type,
            "issue": "Missing signatory section",
            "severity": "Medium",
            "suggestion": "Add signature and date block."
        })
    return issues
