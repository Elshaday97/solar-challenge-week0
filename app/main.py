import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Dashboard", layout="wide")


def load_data():
    try:
        benin_df = pd.read_csv("data/benin_clean.csv")
        sl_df = pd.read_csv("data/sierraleone_clean.csv")
        togo_df = pd.read_csv("data/togo_clean.csv")

        benin_df["Country"] = "Benin"
        sl_df["Country"] = "Sierra Leone"
        togo_df["Country"] = "Togo"

        combined_df = pd.concat([benin_df, sl_df, togo_df])
        return combined_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()


df = load_data()


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
