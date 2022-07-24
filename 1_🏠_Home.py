import streamlit as st
import pandas as pd
st.title("Effects of Breast Cancer")
st.markdown("""Breast Cancer is a disease that affects about 200k people in the U.S. each year. The disease is caused by a tumor that grows in the breast. The tumor can be benign or malignant.
Scientists are trying to understand the causes of breast cancer. The goal is to predict whether a tumor is benign or malignant. The data we have is about the characteristics of the tumors. We trained a model to predict whether a tumor is benign or malignant.
The data we take in to predict whether a tumor is benign or malignant is called the **features**. The features are the characteristics of the tumors. The features are: smoothness, concave points, symmetry, radius, perimeter, area, concavity, texture, and compactness.
""")
st.image("https://th.bing.com/th/id/OIP.TzO6wi3ONuCtknWumzOjGwHaE0?pid=ImgDet&rs=1", width=600)

BC = pd.read_csv('data.csv')
df = BC.copy()
df.drop(['concave points_worst', 'perimeter_worst', 'Unnamed: 32', 'concavity_mean', 'concavity_worst', 'compactness_mean', 'radius_worst', 'area_worst', 'radius_mean', 'perimeter_mean', 'area_mean', 'texture_mean', 'perimeter_se', 'area_se'], axis=1, inplace=True)
st.subheader("The data we used to train the model:")
st.dataframe(df)