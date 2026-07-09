import streamlit as st
import pandas as pd

# Page Settings
st.set_page_config(page_title="Student Performance Dashboard", page_icon="🎓", layout="wide")

# Title
st.title("🎓 Student Performance Analysis Dashboard")
st.markdown("### Analyze Student Marks, Grades & Performance")

# Read CSV
df = pd.read_csv("student_data.csv")

# Calculate Average
df["Average"] = (df["Maths"] + df["Science"] + df["English"]) / 3

# Grade
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

# Result
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Top Performer
topper = df.loc[df["Average"].idxmax()]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("👨‍🎓 Total Students", len(df))
col2.metric("📈 Average Marks", round(df["Average"].mean(), 2))
col3.metric("🏆 Topper", topper["Name"])
col4.metric("✅ Pass %", f"{(df['Result']=='Pass').mean()*100:.0f}%")

st.divider()

# Student Table
st.subheader("📋 Student Details")
st.dataframe(df, use_container_width=True)

# Charts
col5, col6 = st.columns(2)

with col5:
    st.subheader("📊 Average Marks")
    st.bar_chart(df.set_index("Name")["Average"])

with col6:
   st.subheader("🥧 Grade Distribution")
   st.write(df["Grade"].value_counts())

st.divider()

# Topper Details
st.success(f"""
🏆 **Top Performer**

**Name:** {topper['Name']}

**Average:** {topper['Average']:.2f}

**Grade:** {topper['Grade']}
""")