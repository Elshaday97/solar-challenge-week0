import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Dashboard", layout="wide")


st.sidebar.header("Upload Your Data")
col1, col2, col3 = st.sidebar.columns(3)

with col1:
    uploaded_file1 = st.file_uploader("Upload Benin CSV", type=["csv"], key="file1")

with col2:
    uploaded_file2 = st.file_uploader(
        "Upload Sierra Leone CSV", type=["csv"], key="file2"
    )

with col3:
    uploaded_file3 = st.file_uploader("Upload Togo CSV", type=["csv"], key="file3")

df = None

if (
    uploaded_file1 is not None
    and uploaded_file2 is not None
    and uploaded_file3 is not None
):
    try:
        df1 = pd.read_csv(uploaded_file1)
        df2 = pd.read_csv(uploaded_file2)
        df3 = pd.read_csv(uploaded_file3)

        df1["Country"] = "Benin"
        df2["Country"] = "Sierra Leone"
        df3["Country"] = "Togo"
        df = pd.concat([df1, df2, df3], ignore_index=True)

        st.success("Files loaded successfully!")
    except Exception as e:
        st.error(f"Error loading files: {e}")
        st.stop()
else:
    st.info("Please upload all three CSV files to proceed.")
    st.stop()

st.sidebar.header("Filters")
countries = df["Country"].unique()
selected_countries = st.sidebar.multiselect(
    "Select countries:", countries, default=countries
)

variables = ["GHI", "DNI", "DHI", "ModA", "ModB", "WS", "WSgust"]
selected_variable = st.sidebar.selectbox("Select variable:", variables)


df_filtered = df[df["Country"].isin(selected_countries)]

st.title("Solar Data Boxplot")
st.write(f"Boxplot of {selected_variable} for selected countries")


plt.figure(figsize=(8, 5))
sns.boxplot(
    x="Country",
    y=selected_variable,
    hue="Country",
    data=df_filtered,
    palette="pastel",
    legend=False,
)
plt.ylabel(selected_variable)
plt.xlabel("Country")
st.pyplot(plt)
