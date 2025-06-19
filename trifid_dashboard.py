import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import os

# =========================
# Page Config and Branding
# =========================
st.set_page_config(
    page_title="Trifid Media - Smart Campaign Portal",
    layout="wide",
)

# Optional logo
# st.image("assets/trifid_logo.png", width=100)

st.markdown("""
# 🚀 Trifid Smart Campaign Dashboard
Welcome to your **AI-ready marketing analytics portal**. Track performance, compare platforms, and interact with your data.
---
""")

# =========================
# Load CSV Data
# =========================
csv_file = "Trifid_Campaign_Demo.csv"
if not os.path.exists(csv_file):
    st.error("CSV file not found. Please upload the dataset.")
else:
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

    # Sidebar Filters
    st.sidebar.header("🔍 Filter Options")
    platform_filter = st.sidebar.multiselect("Choose Platforms", df['Platform'].unique(), default=df['Platform'].unique())
    df_filtered = df[df['Platform'].isin(platform_filter)]

    # =========================
    # KPIs Display
    # =========================
    total_impressions = int(df_filtered['Impressions'].sum())
    total_clicks = int(df_filtered['Clicks'].sum())
    avg_ctr = round(df_filtered['CTR (%)'].mean(), 2)
    avg_cpc = round(df_filtered['CPC ($)'].mean(), 2)
    avg_conv_rate = round(df_filtered['Conversion Rate (%)'].mean(), 2)

    st.markdown("## 📊 Key Campaign Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("🧲 Total Impressions", f"{total_impressions:,}")
    col2.metric("📥 Total Clicks", f"{total_clicks:,}")
    col3.metric("🎯 Avg. CTR", f"{avg_ctr}%")

    col4, col5 = st.columns(2)
    col4.metric("💰 Avg. CPC", f"${avg_cpc:.2f}")
    col5.metric("🚀 Conversion Rate", f"{avg_conv_rate}%")

    # =========================
    # Trend Line Charts
    # =========================
    st.markdown("## 📈 Trends Over Time")
    chart1 = alt.Chart(df_filtered).mark_line().encode(
        x='Date:T',
        y=alt.Y('Impressions', title='Impressions'),
        color=alt.value('#1f77b4')
    ).properties(title="Impressions Over Time")

    chart2 = alt.Chart(df_filtered).mark_line(color='orange').encode(
        x='Date:T',
        y='Clicks'
    ).properties(title="Clicks Over Time")

    st.altair_chart(chart1 + chart2, use_container_width=True)

    # =========================
    # Bar Chart by Platform
    # =========================
    st.markdown("## 🧮 Platform Performance Comparison")
    bar_chart = alt.Chart(df_filtered).mark_bar().encode(
        x=alt.X('Platform:N', sort='-y'),
        y='Clicks',
        color='Platform:N'
    ).properties(height=400)
    st.altair_chart(bar_chart, use_container_width=True)

    # =========================
    # Data Table
    # =========================
    with st.expander("📂 View Raw Data"):
        st.dataframe(df_filtered, use_container_width=True)

    # =========================
    # AI Assistant (Simulated)
    # =========================
    st.markdown("## 🤖 Ask Your Campaign Assistant")
    query = st.text_input("Type your question (e.g., What was the CTR on June 3?)")

    if query:
        with st.spinner("Thinking..."):
            # Simulated logic (replace with GPT later)
            sample_responses = {
                "CTR on June 3": "The CTR on June 3 was 2.46%, slightly above your average.",
                "Impressions trend": "Impressions increased steadily over the 10-day period.",
                "Which platform performed best": "Instagram had the highest engagement across all KPIs.",
                "Conversion rate": f"Your average conversion rate was {avg_conv_rate}%."
            }
            matched = False
            for key in sample_responses:
                if key.lower() in query.lower():
                    st.success(sample_responses[key])
                    matched = True
                    break
            if not matched:
                st.info("I'm a demo assistant. Try asking about CTR, impressions trend, or best platform.")

    # =========================
    # Footer/About Section
    # =========================
    st.markdown("""
---
### 👩‍💻 About the Developer
**Jasmeet Kaur**  
MSc Artificial Intelligence & Data Analytics  
GitHub: [jasmeet0810](https://github.com/Jasmeet0810)  
""")
