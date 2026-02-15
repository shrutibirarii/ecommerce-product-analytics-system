📊 Ecommerce Product Analytics System

An end-to-end analytics and forecasting pipeline built using MySQL, Python, Machine Learning, and Streamlit to analyze ecommerce sales, customer behavior, and revenue trends.

🚀 Overview

This project demonstrates a complete data workflow:

✔ Data ingestion into MySQL

✔ SQL aggregations & business KPIs

✔ Exploratory Data Analysis (EDA)

✔ Correlation analysis

✔ RFM customer segmentation

✔ KMeans clustering

✔ Revenue forecasting (Linear Regression)

✔ Interactive Streamlit dashboard

The objective is to simulate a production-style analytics system from database to predictive modeling.

🏗 Tech Stack

- Python
- MySQL (Workbench)
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Streamlit

📁 Project Structure
ecommerce-product-analytics-system/
│
├── dashboards/
|    
├── data/
│   └── ecommerce_data.csv
│
├── notebooks/
│   ├── analytics.ipynb
│   ├── app.ipynb
│   ├── forecast.ipynb
│   ├── load_to_mysql.ipynb
│
├── src/
|   ├── app.py
|
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-link>
cd ecommerce-product-analytics-system

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create MySQL Database

In MySQL Workbench:

CREATE DATABASE ecommerce_analytics;


Update your MySQL credentials inside:

notebooks/analytics.ipynb

notebooks/forecast.ipynb

notebooks/load_to_mysql.ipynb

4️⃣ Load Data into MySQL
jupyter notebooks/load_to_mysql.ipynb

5️⃣ Run Analytics Module
jupyter notebooks/analytics.ipynb


Includes:

Correlation matrix & heatmap

RFM calculation

KMeans clustering

6️⃣ Run Forecast Model
jupyter notebooks/forecast.ipynb


Outputs:

Train/Test split

Model evaluation (MAE)

6-month revenue forecast

Forecast visualization

7️⃣ Launch Dashboard
streamlit run app.py


Dashboard displays:

Revenue KPIs

Customer segmentation

Forecast insights

📊 Key Features
🔹 Revenue Analysis

Monthly revenue aggregation using SQL views

Business KPI computation

🔹 Correlation Analysis

Numeric feature correlation matrix

Heatmap visualization

🔹 RFM Segmentation

Recency

Frequency

Monetary value

Customer behavior profiling

🔹 Customer Clustering

KMeans segmentation

Behavior-based customer grouping

🔹 Revenue Forecasting

Linear Regression model

Train/Test split

MAE evaluation metric

6-month future revenue projection

📈 Business Value

Identifies high-value customer segments

Reveals feature relationships impacting revenue

Supports marketing & retention strategy

Enables revenue planning with forecasting

🎯 Skills Demonstrated

SQL + Python integration

Feature engineering

Machine learning workflow

Model evaluation

Data visualization

Dashboard development

🔮 Future Improvements

Implement ARIMA / time-series models

Add cohort & retention analysis

Deploy on cloud (AWS / GCP)

Add automated ETL pipeline

👤 About

I enjoy identifying patterns in data and translating them into structured, actionable insights. This project reflects my interest in building scalable analytics systems that bridge data engineering and machine learning.

Note: Full dataset (~43MB) excluded to keep repository lightweight.
A sample dataset is provided for demonstration.
