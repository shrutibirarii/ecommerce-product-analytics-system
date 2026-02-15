import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:1923%40Julsep@localhost/ecommerce_analytics")

st.title("Ecommerce Analytics Dashboard")

df = pd.read_sql("SELECT * FROM revenue_summary", engine)

st.line_chart(df.set_index("month")["revenue"])

st.write("Total Revenue:", df["revenue"].sum())