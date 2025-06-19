import streamlit as st
import pandas as pd
import altair as alt
import os

# Page settings
st.set_page_config(page_title="Trifid Media - Smart Campaign Portal", layout="wide")
st.title("🎯 Smart Campaign Dashboard with AI Assistant")

# Load CSV
csv_file = "Trifid_Campaign_Demo.csv"
if not os.path.exists(csv_file):
    st.error("CSV file not found. Please upload the dataset.")
else:
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

    # Sidebar filter
    st.sidebar.header("📌 Filter by Platform")
    platforms = st.sidebar.multiselect("Choose Platforms", df['Platform'].unique(), default=df['Platform'].unique())
    df_filtered = df[df['Platform'].isin(platforms)]

    # ============ SECTION 1: KPI TABLE ============
    st.markdown("## 📊 Key Campaign Metrics")

    total_impressions = int(df_filtered['Impressions'].sum())
    total_clicks = int(df_filtered['Clicks'].sum())
    avg_ctr = round(df_filtered['CTR (%)'].mean(), 2)
    avg_cpc = round(df_filtered['CPC ($)'].mean(), 2)
    avg_conv_rate = round(df_filtered['Conversion Rate (%)'].mean(), 2)

    kpi_table = pd.DataFrame({
        "Metric": [
            "🧲 Total Impressions",
            "📥 Total Clicks",
            "🎯 Avg. CTR",
            "💰 Avg. CPC",
            "🚀 Conversion Rate"
        ],
        "Value": [
            f"{total_impressions:,}",
            f"{total_clicks:,}",
            f"{avg_ctr}%",
            f"${avg_cpc:.2f}",
            f"{avg_conv_rate}%"
        ]
    })

    st.dataframe(
        kpi_table.style.set_table_styles(
            [{'selector': 'th', 'props': [('font-size', '16px'), ('text-align', 'center')]}]
        ).set_properties(**{'text-align': 'center'}),
        use_container_width=True,
        hide_index=True
    )

    # ============ SECTION 2: TRENDS OVER TIME ============
    st.markdown("## 📈 Trends Over Time")
    left_col, right_col = st.columns([1.2, 2.5])

    with left_col:
        st.markdown("""
        ### 📊 Impressions vs Clicks Analysis
        - **Impressions** steadily increased across the campaign.
        - A minor drop occurred on **June 3**, followed by consistent growth.
        - **Clicks** (orange line) show a correlated trend but at lower magnitude.
        - This suggests increasing reach and steady user interaction. 📈
        """)

    with right_col:
        chart_impr = alt.Chart(df_filtered).mark_line(strokeWidth=3).encode(
            x=alt.X('Date:T', title='Date'),
            y=alt.Y('Impressions:Q', title='Impressions'),
            tooltip=['Date:T', 'Impressions']
        ).properties(width=600, height=350).interactive()

        chart_clicks = alt.Chart(df_filtered).mark_line(color='orange', strokeWidth=2).encode(
            x='Date:T',
            y='Clicks:Q',
            tooltip=['Date:T', 'Clicks']
        )

        st.altair_chart(chart_impr + chart_clicks, use_container_width=True)

    # ============ SECTION 3: PLATFORM COMPARISON ============
    st.markdown("## 🧮 Platform Performance Comparison")

    platform_summary = df_filtered.groupby('Platform').agg({
        'Clicks': 'sum',
        'Impressions': 'sum',
        'Conversion Rate (%)': 'mean'
    }).reset_index()

    platform_summary.columns = ['Platform', 'Total Clicks', 'Total Impressions', 'Avg. Conversion Rate']
    platform_summary = platform_summary.sort_values(by='Total Clicks', ascending=False)

    bar_chart = alt.Chart(platform_summary).mark_bar(size=35, cornerRadiusTopLeft=8, cornerRadiusTopRight=8).encode(
        x=alt.X('Total Clicks:Q', title='Total Clicks'),
        y=alt.Y('Platform:N', sort='-x', title=''),
        color=alt.Color('Platform:N', legend=None),
        tooltip=['Platform', 'Total Clicks', 'Total Impressions', 'Avg. Conversion Rate']
    ).properties(
        height=300,
        width=700,
        title='📊 Total Clicks by Platform'
    )

    st.altair_chart(bar_chart, use_container_width=True)

    # ============ OPTIONAL: RAW DATA VIEW ============
    with st.expander("📂 View Raw Data"):
        st.dataframe(df_filtered, use_container_width=True)

    # ============ AI Assistant DEMO ============
    st.markdown("## 🤖 Ask Your Campaign Assistant")
    query = st.text_input("Type your question (e.g., What was the CTR on June 3?)")

    if query:
        with st.spinner("Analyzing..."):
            responses = {
                "CTR on June 3": "The CTR on June 3 was 2.46%, slightly above your average.",
                "Impressions trend": "Impressions increased steadily over the 10-day period.",
                "Which platform performed best": "Instagram had the highest engagement across all KPIs.",
                "Conversion rate": f"Your average conversion rate was {avg_conv_rate}%."
            }
            matched = False
            for key in responses:
                if key.lower() in query.lower():
                    st.success(responses[key])
                    matched = True
                    break
            if not matched:
                st.info("I'm a demo assistant. Try asking about CTR, impressions trend, or best platform.")

    st.markdown("---")
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
