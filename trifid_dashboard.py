import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import openai
import os

# App title
st.set_page_config(page_title="Trifid Media - Smart Campaign Portal")
st.title("📊 Smart Campaign Dashboard with AI Assistant")

# Load Data
csv_file = "Trifid_Campaign_Demo.csv"
if not os.path.exists(csv_file):
    st.error("CSV file not found. Please upload the dataset.")
else:
    df = pd.read_csv(csv_file)
    st.sidebar.header("📂 Filter by Platform")
    platform_filter = st.sidebar.multiselect("Choose Platforms", df['Platform'].unique(), default=df['Platform'].unique())
    df_filtered = df[df['Platform'].isin(platform_filter)]

    # Show Dataframe
    with st.expander("🔍 View Raw Data"):
        st.dataframe(df_filtered)

    # KPI Metrics
    total_impressions = int(df_filtered['Impressions'].sum())
    total_clicks = int(df_filtered['Clicks'].sum())
    avg_ctr = round(df_filtered['CTR (%)'].mean(), 2)
    avg_cpc = round(df_filtered['CPC ($)'].mean(), 2)
    avg_conv_rate = round(df_filtered['Conversion Rate (%)'].mean(), 2)

    st.markdown("### 📈 Campaign KPIs")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Impressions", f"{total_impressions:,}")
    col2.metric("Total Clicks", f"{total_clicks:,}")
    col3.metric("Avg. CTR", f"{avg_ctr}%")
    
    col4, col5 = st.columns(2)
    col4.metric("Avg. CPC", f"${avg_cpc}")
    col5.metric("Conversion Rate", f"{avg_conv_rate}%")

    # Chart
    st.markdown("### 📊 Impressions vs Clicks Over Time")
    line_chart = alt.Chart(df_filtered).mark_line().encode(
        x='Date:T',
        y=alt.Y('Impressions', title='Count'),
        color=alt.value('steelblue')
    ).interactive()

    line_chart_clicks = alt.Chart(df_filtered).mark_line(color='orange').encode(
        x='Date:T',
        y='Clicks'
    )

    st.altair_chart(line_chart + line_chart_clicks, use_container_width=True)

    # AI Chat Assistant Simulation
    st.markdown("### 🤖 Ask Your Campaign Assistant")
    query = st.text_input("Type your question (e.g., What was the CTR on June 3?)")

    if query:
        with st.spinner("Thinking..."):
            # Simulated response logic for demo purposes
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

    st.markdown("---")
    st.markdown("Built by Jasmeet Kaur \U0001F469‍\U0001F4BB | MSc AI & Data Analytics")
