import streamlit as st
from orchestrator.orchestrator import process_pharmacy_request

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="PharmaAssist AI",
    page_icon="🏥",
    layout="wide"
)

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.title("🏥 PharmaAssist AI")

st.subheader(
    "AI-Powered Pharmacy Benefits Verification System"
)

st.markdown(
    """
This application demonstrates a **multi-agent AI architecture**
for pharmacy benefit verification using deterministic business
logic and Google Gemini for natural language explanations.
"""
)

st.divider()

# ---------------------------------------------------
# Member Information
# ---------------------------------------------------

st.header("📋 Member Information")

col1, col2 = st.columns(2)

with col1:
    member_id = st.text_input(
        "Member ID",
        value="1001"
    )

with col2:
    date_of_service = st.text_input(
        "Date of Service",
        value="2026-05-01"
    )

drug_name = st.text_input(
    "Drug Name",
    value="Ozempic"
)

st.divider()

# ---------------------------------------------------
# Verify Button
# ---------------------------------------------------

verify_button = st.button(
    "🔍 Verify Pharmacy Benefits",
    use_container_width=True
)

# ---------------------------------------------------
# Placeholder
# ---------------------------------------------------

if verify_button:

    with st.spinner("Running AI Workflow..."):

        result = process_pharmacy_request(
            member_id=int(member_id),
            date_of_service=date_of_service,
            drug_name=drug_name
        )

    st.success("Workflow completed successfully!")

    st.divider()

    st.header("📊 Decision Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Eligible",
            "Yes" if result["eligibility"]["eligible"] else "No"
        )

        st.metric(
            "Covered",
            "Yes" if result["coverage"]["covered"] else "No"
        )

    with col2:
        st.metric(
            "Prior Authorization",
            "Required"
            if result["coverage"]["prior_authorization"]
            else "Not Required"
        )

        st.metric(
            "Evaluation Score",
            result["evaluation"]["score"]
        )

    st.divider()

    st.header("📄 Recommendation")

    st.success(
        result["recommendation"]["recommended_action"]
    )

    st.divider()

    st.header("💬 AI Explanation")

    st.info(
        result["explanation"]
    )

    st.divider()

    st.header("✅ Evaluation")

    st.write(result["evaluation"])