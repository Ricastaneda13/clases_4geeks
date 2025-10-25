import streamlit as st
from sklearn.datasets import load_iris

#Load Data
X_raw, y_raw = load_iris(return_X_y=True, as_frame=True)
df_raw = X_raw
df_raw["species"] = y_raw
df_raw.info()

#Preprocessing
df_baking = df_raw.copy()
df_baking.columns = df_baking.columns.str.lower().str.replace("(", "").str.replace(")", "").str.replace(" ", "_")
df_baking["species"] = df_baking["species"].map({0:"setosa", 1:"versicolor", 2:"virginica"})
df_baking["species"] = df_baking["species"].astype("category")
df = df_baking.copy()

#Web
st.title("Iris Dashboard")
st.write("Iris DataSet Table")

species = st.selectbox("Filter to:", ["versicolor", "setosa", "virginica"])
st.write(df[df["species"]== species])