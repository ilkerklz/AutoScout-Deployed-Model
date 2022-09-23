
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# header
html_temp = """
<div style="background-color:purple;padding:1.5px">
<h1 style="color:white;text-align:center;">Welcome to my first deployed Machine Learning model!</h1>
</div><br>"""
st.markdown(html_temp, unsafe_allow_html=True)

st.markdown("Please check out the section on the left-hand side. Enter the characteristics of your car and get the market value! :+1:")

#dataframe
df = pd.read_csv('final_scout_deployment.csv', nrows=(100))
st.markdown("You may check the dataframe below.")
st.write(df.head())

# model
import pickle
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))

#sidebar
st.sidebar.title("Enter the values:")

# getting inputs
hp_kW = st.sidebar.number_input("hp_kW:",min_value=df["hp_kW"].min(), max_value=df["hp_kW"].max())
age = st.sidebar.number_input("age:",min_value=df.age.min(), max_value=df.age.max())
km = st.sidebar.number_input("km:",min_value=df.km.min(), max_value=df.km.max())
Gears = st.sidebar.number_input("Gears:",min_value=df.Gears.min(), max_value=df.Gears.max())
make_model = st.sidebar.selectbox("make_model:", [  "Audi A1", 
                                                    "Audi A3", 
                                                    "Opel Astra", 
                                                    "Opel Corsa", 
                                                    "Opel Insignia", 
                                                    "Renault Clio", 
                                                    "Renault Duster", 
                                                    "Renault Espace"])
Gearing_Type = st.sidebar.selectbox("Gearing_Type:", ["Automatic", "Manual"])


new_dict = {"hp_kW": hp_kW,
            "age": age,
            "km": km,
            "Gears": Gears,
            "make_model": make_model,
            "Gearing_Type": Gearing_Type,
            }

# displaying inputs
df=pd.DataFrame.from_dict([new_dict])
st.markdown("Here are the inputs you provided:")
st.table(df)

# prediction button
pred_button = st.button("Predict")

#showing results
if pred_button:
    pred = model.predict(df)
    st.write(pred[0])

#closing
html_temp = """
<div style="background-color:purple;padding:1.5px">
<h1 style="color:white;text-align:center;">See you next time!</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)


