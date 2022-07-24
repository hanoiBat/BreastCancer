import streamlit as st
st.subheader("The code we used to derive an equation is below:")
st.code("""import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
BC = pd.read_csv('data.csv')
BC.head()
df = BC.copy()
df["deadly"] = "abc"
def tumorBinary(var):
    if var == 'M':
        return 1
    elif var == 'B':
        return 0
df["deadly"] = BC['diagnosis'].apply(tumorBinary)
target = 'deadly'
cor = df.corr()
cor_target = abs(cor[target])
notrelevant_features = cor_target[cor_target<0.1].index.to_list()
df.drop(['concave points_worst', 'perimeter_worst', 'Unnamed: 32', 'concavity_mean', 'concavity_worst', 'compactness_mean', 'radius_worst', 'area_worst', 'radius_mean', 'perimeter_mean', 'area_mean', 'texture_mean', 'perimeter_se', 'area_se'], axis=1, inplace=True)
df.drop(['diagnosis'], axis=1, inplace=True)
X = df[df.columns.drop(target)]
y = df[[target]]
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=.33)
linmod = LinearRegression()
linmod.fit(X_train, y_train)
view = pd.concat([X_train.head(10), y_train.head(10)],  axis=1)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
print(view)""", language='python')
st.write("")
st.markdown("With the use of this model we have acheived roughly 85 percent accuracy on the test set. This is a good model to use for this problem since it is able to detect whether the user has breast cancer or not with fairly high accuracy.")