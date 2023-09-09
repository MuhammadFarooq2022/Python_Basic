import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import max_error, mean_squared_error, mean_absolute_error, r2_score

# make containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("kashti ki app")
    st.text("In the projrct we will work on kashti data")

with data_sets:
    st.header("Kashti doob gaye, Hawww!")
    st.text("We will work on Titanic dataset")
    # import data
    df = sns.load_dataset('titanic')
    df = df.dropna()
    st.write(df.head(10))
    st.bar_chart(df['sex'].value_counts())

    # other plot
    st.subheader('Class k hisab say faruq')
    st.bar_chart(df['class'].value_counts())
    # barplot
    st.bar_chart(df['age'].sample(10)) # or .head(10)


with features:
    st.header("These are our app features:")
    st.text("Awen bht saray features add kartay hain, asan hi hy")
    st.markdown('1. **Feature 1:** This will tell us pata nahi')
    st.markdown('1. **Feature 2:** This will tell us about data')
    

with model_training:
    st.header("Kashti walon ka kia bana?.Model Training")
    st.text("اس میں ہم اپنے پیرامیٹرز کو بڑھا یا گھٹائیں گے۔")
    # Making columns
    input, display = st.columns(2)

    # Pehlay column main ap k selection points hun
    max_depth = input.slider('how many people do you know?', min_value=10, max_value=100, value=20, step=5)

# n_estimators
n_estimators = input.selectbox('How many tree should be there in RF?', options=[50,100,200,300,'No limit'])

# adding list of features
input.write(df.columns)

# input features from user
input_features = input.text_input('Which feature we should use?')

# Machine learning model
model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
# yahan per hum aik condition lagayen gay
if n_estimators == 'No limit':
    model = RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

# Define X and y
X = df[[input_features]]
y = df[['fare']]

# fit model
model.fit(X, y)
pred = model.predict(y)

# Display Metrices
display.subheader('Mean absolute error of the model is:')
display.write(mean_absolute_error(y, pred))
display.subheader('Mean squard error of the model is:')
display.write(mean_squared_error(y, pred))
display.subheader('R squared score of the model is:')
display.write(r2_score(y, pred))