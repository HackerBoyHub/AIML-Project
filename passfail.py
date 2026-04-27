import streamlit as st
import numpy as np
from sklearn.tree import DecisionTreeClassifier
X = np.array([
    [1, 50],
    [2, 55],
    [3, 60],
    [4, 70],
    [5, 80],
    [6, 90]
])
y = np.array([0, 0, 0, 1, 1, 1])
model = DecisionTreeClassifier()
model.fit(X, y)
st.title("Pass/Fail Predictor")
hours = st.number_input("Study Hours")
attendance = st.number_input("Attendance (%)")
if st.button("Predict"):
    result = model.predict([[hours, attendance]])
    if result[0] == 1:
        st.success("Pass ✅")
    else:
        st.error("Fail ❌")