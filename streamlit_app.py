import streamlit as st
from modules.parser import parse_docx
from modules.classifier import detect_doc_type
from modules.checklist import get_process_and_missing_docs
from modules.reviewer import run_basic_checks
from modules.docwriter import create_reviewed_doc
import json
import tempfile
import os

st.title("ADGM Corporate Agent (MVP)")
st.write("Upload your `.docx` documents for ADGM compliance review.")

uploaded_files = st.file_uploader("Upload one or more `.docx` files", type=["docx"], accept_multiple_files=True)

if uploaded_files:
    parsed_docs = []
    doc_types = []
    
    for file in uploaded_files:
        text = parse_docx(file)
        doc_type = detect_doc_type(text)
        parsed_docs.append({"filename": file.name, "text": text, "doc_type": doc_type})
        doc_types.append(doc_type)
    
    process, required_docs, missing_docs = get_process_and_missing_docs(doc_types)
    
    issues_found = []
    for doc in parsed_docs:
        issues = run_basic_checks(doc["doc_type"], doc["text"])
        issues_found.extend(issues)
        reviewed_doc_path = create_reviewed_doc(doc["filename"], doc["text"], issues)
        
        with open(reviewed_doc_path, "rb") as f:
            st.download_button(
                label=f"Download Reviewed {doc['filename']}",
                data=f,
                file_name=f"reviewed_{doc['filename']}",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    
    # Build JSON summary
    result = {
        "process": process,
        "documents_uploaded": len(doc_types),
        "required_documents": len(required_docs),
        "missing_documents": missing_docs,
        "issues_found": issues_found
    }
    
    st.json(result)
    
    # Offer JSON download
    tmp_json = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    with open(tmp_json.name, "w") as jf:
        json.dump(result, jf, indent=2)
    with open(tmp_json.name, "rb") as f:
        st.download_button(
            label="Download JSON Summary",
            data=f,
            file_name="adgm_review_summary.json",
            mime="application/json"
        )
