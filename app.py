import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Automating Financial Reporting", layout="wide")

st.title("💰 **Automating Financial Reporting Agent**")
st.markdown("""
Upload financial data to automatically generate a summary report, including total revenue, expenses, and profit.
""")

uploaded_file = st.file_uploader("Upload Financial Data (CSV/Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('csv') else pd.read_excel(uploaded_file)
    st.write("### 📊 **Data Preview**")
    st.dataframe(df.head())

    # --- Simple Financial Report ---
    total_revenue = df["Revenue"].sum()
    total_expenses = df["Expenses"].sum()
    total_profit = df["Profit"].sum()

    st.markdown("### 📑 **Financial Report Summary**")
    st.write(f"**Total Revenue:** ${total_revenue:,.2f}")
    st.write(f"**Total Expenses:** ${total_expenses:,.2f}")
    st.write(f"**Net Profit:** ${total_profit:,.2f}")

    # --- Visualization ---
    st.markdown("### 📈 **Revenue vs Expenses**")
    fig, ax = plt.subplots()
    df[["Revenue", "Expenses"]].plot(kind="bar", ax=ax)
    st.pyplot(fig)
