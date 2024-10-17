
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Sleep streamlit Website')
st.write('Analysis of sleep')
df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')


st.write('3D plot of 4 features')

fig1 = px.scatter_3d(df, x='Physical_Activity_Level', y='Stress_Level', z='Sleep_Duration', 
                     color='Age', title="Interaction of Physical Activity, Stress Level, and Sleep Duration with Age",
                     labels={'Physical_Activity_Level': 'Physical Activity', 'Stress_Level': 'Stress Level',
                             'Sleep_Duration': 'Sleep Duration', 'Age': 'Age'})

st.plotly_chart(fig1)
