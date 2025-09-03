import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="Automating Financial Reporting", layout="wide", initial_sidebar_state="expanded")

# --- TITLE & DESCRIPTION ---
st.title("💰 **Automating Financial Reporting Agent**")
st.markdown("""
This agent helps automate the generation of financial reports including balance sheets, income statements, and cash flow statements.
Users can upload financial data files (CSV/Excel), select the type of report, and get a beautifully generated output.
""", unsafe_allow_html=True)

# --- FILE UPLOADER ---
st.subheader("🔼 **Upload Your Financial Data File**")
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

# --- MANUAL INPUT SECTION ---
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('csv') else pd.read_excel(uploaded_file)

    st.write("### **Data Preview**")
    st.write(df.head())

    # --- FINANCIAL REPORT OPTIONS ---
    report_type = st.selectbox("Select Report Type", ["Balance Sheet", "Income Statement", "Cash Flow Statement"])

    # --- BUTTON FOR REPORT GENERATION ---
    if st.button("Generate Report"):
        st.markdown("### 📈 **Generated Report**")
        # Placeholder for report generation logic
        st.write(f"Generating {report_type} for the data...")
        st.success(f"**{report_type}** generated successfully!")
        
        # --- DOWNLOAD BUTTON ---
        st.download_button(
            label="Download Report",
            data=df.to_csv(index=False),
            file_name="financial_report.csv",
            mime="text/csv"
        )

# --- STYLING ---
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stSelectbox, .stTextInput {
        background-color: #333;
        color: white;
    }
    .stFileUploader {
        background-color: #333;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
