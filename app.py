
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fitness Dashboard", layout="wide")
st.title("🏃 Fitness Tracking Dashboard")

df = pd.read_csv("fitness_data.csv")
df["activity_date"] = pd.to_datetime(df["activity_date"], errors="coerce")

a, b, c, d = st.columns(4)
a.metric("Total Steps", f"{df['steps_count'].sum():,.0f}")
b.metric("Total Calories", f"{df['calories_burned'].sum():,.0f}")
c.metric("Average Heart Rate", f"{df['heart_rate_bpm'].mean():.1f} bpm")
d.metric("Average Sleep", f"{df['sleep_hours'].mean():.1f} hours")

st.subheader("Steps Over Time")
st.line_chart(df.groupby("activity_date")["steps_count"].sum())

st.subheader("Calories by Activity")
st.bar_chart(df.groupby("activity_type")["calories_burned"].sum())

st.subheader("Sleep vs Calories")
st.scatter_chart(df, x="sleep_hours", y="calories_burned")

st.subheader("Dataset")
st.dataframe(df, use_container_width=True)
