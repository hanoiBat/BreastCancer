import streamlit as st
import math as m
import pandas as pd
with st.form("my_form"):
    st.write("Breast Cancer Prediction")
    sm = st.number_input('The mean of local variation in radius lengths', value=0.0, step=0.01)
    concm = st.number_input('The mean number of concave portions of the contour', value=0.0, step=0.01)
    symean = st.number_input('The mean symmetry of the tumour', value=0.0, step=0.01)
    rs = st.number_input('The standard error for the mean of distances from center to points on the perimeter', value=0.0, step=0.01)
    compse = st.number_input('The standard error for perimeter^2 / area - 1.0', value=0.0, step=0.01)
    concse = st.number_input('The standard error for severity of concave portions of the contour', value=0.0, step=0.01)
    cps = st.number_input('The standard error for number of concave portions of the contour', value=0.0, step=0.01)
    texw = st.number_input('The "worst" or largest mean value for standard deviation of gray-scale values', value=0.0, step=0.01)
    smow = st.number_input('The "worst" or largest mean value for local variation in radius lengths', value=0.0, step=0.01)
    compw = st.number_input('The "worst" or largest mean value for perimeter^2 / area - 1.0', value=0.0, step=0.01)
    symw = st.number_input('The "worst" or largest mean value for symmetry of the tumour', value=0.0, step=0.01)
    fdw = st.number_input('The "worst" or largest mean value for "coastline approximation" - 1', value=0.0, step=0.01)
    submitted = st.form_submit_button("Submit")
    if submitted:
        val=-8.25427891 + 0.25934413 * sm +  1.86810728 * concm +  0.29750163 * symean + 4.68625661 * rs - 0.0716165 * compse - 0.031984 * concse + 0.08120882 * cps + 0.15562404 * texw + 0.57776422* smow + 4.03547874 * compw + 1.75361088 * symw + 0.11486053 * fdw
        prob = m.exp(val)/(1+m.exp(val))
        st.write("The probability of having breast cancer is:", prob)
