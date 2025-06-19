# Smart Campaign Dashboard – AI-Ready Marketing Analytics
This project is a fully functional AI-powered marketing analytics dashboard tailored for creative and digital marketing agencies like **Trifid Media**. It is built to **track campaign performance, compare multi-platform data, and interact with insights** via a streamlined user interface.

## 🔗 Live Demo
👉 [Access the Live App] 
(https://trifid-app-demo-nexrqdv48xzbpdnwthqplp.streamlit.app)

---

## 🚀 Features

- **Real-time KPI dashboard**: Visual display of impressions, clicks, CTR, CPC, and conversion rates  
- **Platform-wise filtering**: Compare performance across Instagram, Facebook, YouTube, Google  
- **Time-series trend analysis**: Impressions vs. Clicks over time using Altair charts  
- **Expandable raw data view**: See and filter the original dataset  
- **AI Assistant (Demo)**: Simulated OpenAI-based assistant to answer natural language queries  
- **Interactive UI**: Built using Streamlit for clean, responsive performance

---

## 📁 Files Included

| File/Folder                 | Description                                             |
|-----------------------------|----------------------------------------------------------|
| `app.py`                    | Main Streamlit application script                        |
| `Trifid_Campaign_Demo.csv`  | Sample campaign performance dataset                      |
| `requirements.txt`          | Required Python libraries for local setup                |
| `README.md`                 | Project overview and instructions                        |

---

## 🛠️ Built With

- **Python 3.9+**
- **Streamlit**
- **Pandas**
- **Altair**
-  `openai`, `langchain` for assistant logic extension

---

## 📦 Installation

To run this project locally:

# Clone the repository
git clone https://github.com/Jasmeet0810/trifid-portal-demo.git
cd trifid-portal-demo

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
📈 Sample Dataset Overview
The provided CSV contains sample metrics across 10 campaign days across 4 platforms:

Columns include: Date, Platform, Impressions, Clicks, Conversions, CTR (%), CPC ($), Conversion Rate (%)

💡 Future Improvements
Live OpenAI API integration for dynamic assistant responses
Role-based user authentication
Client-specific portal dashboards
Auto PDF/Excel report generation
Google Analytics/Meta Ads API integration

📬 Contact
For questions, feedback, or collaboration:
Jasmeet Kaur
Email: jasmeet08virdi@gmail.com
LinkedIn: linkedin.com/in/jasmeet-kaur-virdi

📝 License
This project is shared as a portfolio/demo. Please do not use for commercial purposes without permission.
Let me know if you'd like:
- A version with images (you can upload screenshots to your repo)
- Auto-generated badges (like Streamlit, Python version, etc.)
- README in PDF or DOCX format for sharing offline
