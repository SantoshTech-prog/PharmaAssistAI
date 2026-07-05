
import streamlit as st
from orchestrator.orchestrator import process_pharmacy_request

st.set_page_config(page_title="PharmaAssist AI", page_icon="🏥", layout="wide")

# ============================================================
# Sidebar
# ============================================================

with st.sidebar:
    st.title("🏥 PharmaAssist AI")
    st.markdown("---")

    st.subheader("ℹ️ About")
    st.write(
        "AI-powered Pharmacy Benefits Verification System built using a "
        "Multi-Agent AI Architecture."
    )

    st.markdown("---")

    st.subheader("🤖 Multi-Agent Architecture")
    st.markdown("""
1. ✅ Eligibility Agent
2. ✅ Coverage Agent
3. ✅ Recommendation Agent
4. 🤖 Explanation Agent (Google Gemini)
5. ✅ Evaluation Agent
""")

    st.markdown("---")

    st.subheader("🛠 Technologies")
    st.markdown("""
- Python 3.14
- Streamlit
- Google Gemini
- Multi-Agent Architecture
- Context Engineering
""")

    st.success("🏆 Kaggle AI Agents Capstone")
    st.caption("Built for the Kaggle AI Agents Intensive.")

# ============================================================
# Header
# ============================================================

st.title("🏥 PharmaAssist AI")

st.markdown("""
### AI-Powered Pharmacy Benefits Verification System

Verify pharmacy benefits using a **Multi-Agent AI Architecture**
that combines deterministic business rules with **Google Gemini**
to generate clear, natural language explanations.

This project demonstrates the **AI + Tools + Guardrails**
design pattern from the Kaggle AI Agents Intensive course.
""")

st.divider()

# ============================================================
# Member Information
# ============================================================

with st.container():
    st.header("📋 Member Information")

    col1, col2 = st.columns(2)

    with col1:
        member_id = st.text_input("Member ID", value="1001")

    with col2:
        date_of_service = st.text_input(
            "Date of Service",
            value="2026-05-01"
        )

    drug_name = st.text_input("Drug Name", value="Ozempic")

st.divider()

verify_button = st.button(
    "🚀 Verify Member Benefits",
    use_container_width=True
)

if verify_button:
    try:
        with st.spinner("Running PharmaAssist AI Workflow..."):
            result = process_pharmacy_request(
                member_id=int(member_id),
                date_of_service=date_of_service,
                drug_name=drug_name
            )

        st.success("✅ Workflow completed successfully!")

        st.info("""
### ⚙️ Multi-Agent Workflow Executed

✅ Eligibility Agent
✅ Coverage Agent
✅ Recommendation Agent
🤖 Explanation Agent (Google Gemini)
✅ Evaluation Agent
""")

        st.divider()

        st.header("📊 Decision Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Eligible",
                      "Yes" if result["eligibility"]["eligible"] else "No")
            st.metric("Covered",
                      "Yes" if result["coverage"]["covered"] else "No")

        with col2:
            st.metric(
                "Prior Authorization",
                "Required"
                if result["coverage"]["prior_authorization"]
                else "Not Required"
            )
            st.metric("Member ID", member_id)

        st.divider()

        st.header("📄 Recommendation")

        recommendation = result["recommendation"]["recommended_action"]

        if "not covered" in recommendation.lower():
            st.error(recommendation)
        elif "prior authorization" in recommendation.lower():
            st.warning(recommendation)
        else:
            st.success(recommendation)

        st.divider()

        st.header("💬 Benefit Explanation")
        st.info(result["explanation"])

        st.divider()

        st.header("📈 AI Evaluation")

        evaluation = result["evaluation"]

        if evaluation["passed"]:
            st.success("✅ Evaluation Passed")
        else:
            st.error("❌ Evaluation Failed")

        st.metric("Quality Score", f"{evaluation['score']}/100")

        st.markdown("### Summary")
        st.write(evaluation["summary"])

        if evaluation["issues"]:
            st.markdown("### Issues Found")
            for issue in evaluation["issues"]:
                st.write(f"• {issue}")

    except ValueError:
        st.error("Member ID must be a valid number.")

    except Exception as ex:
        st.error(f"Unexpected error: {ex}")

st.divider()

st.caption("""
Built with ❤️ using

• Google Gemini
• Streamlit
• Python 3.14
• Multi-Agent Architecture

Created as part of the Kaggle AI Agents Intensive Capstone Project.
""")
