
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Sleeeeeeeeep')
st.write('Analysis of how health and lifestyle affects sleep')
df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')

st.title('Hypothesis 1')
st.write(' Higher stress levels are associated with poorer sleep quality and shorter sleep duration')
st.write('The interaction between stress level and physical activity affects sleep duration and quality, moderated by age.')

fig1 = px.scatter_3d(df, x='Physical_Activity_Level', y='Stress_Level', z='Sleep_Duration', 
                     color='Age', title="Interaction of Physical Activity, Stress Level, and Sleep Duration with Age",
                     labels={'Physical_Activity_Level': 'Physical Activity', 'Stress_Level': 'Stress Level',
                             'Sleep_Duration': 'Sleep Duration', 'Age': 'Age'})

st.plotly_chart(fig1)

st.write('3D plot of 2 features')
fig2 = px.box(df, x='Stress_Level', y='Sleep_Duration',
             title="Box Plot: Stress Level vs Sleep Duration",
             labels={'Stress_Level': 'Stress_Level', 'Sleep_Duration': 'Sleep_Duration'})
st.plotly_chart(fig2)




data = {
    "Sleep_Duration": [7.465708],
    "Light_Sleep_Duration": [3.367367],
    "Deep_Sleep_Duration": [3.950111],
    "Rem_Sleep_Duration": [1.717633],
    "Sleep_efficiency_hours": [5.886604]
}

# Create DataFrame
df2 = pd.DataFrame(data)

# Title of the app
st.title("Sleep Study Overview")

# Displaying key metrics using st.metric()
st.metric(label="Average Sleep Duration", value=f"{df2['Sleep_Duration'].mean():.2f} hours")
st.metric(label="Average Light Sleep Duration", value=f"{df2['Light_Sleep_Duration'].mean():.2f} hours")
st.metric(label="Average Deep Sleep Duration", value=f"{df2['Deep_Sleep_Duration'].mean():.2f} hours")
st.metric(label="Average REM Sleep Duration", value=f"{df2['Rem_Sleep_Duration'].mean():.2f} hours")
st.metric(label="Average Sleep Efficiency Hours", value=f"{df2['Sleep_efficiency_hours'].mean():.2f} hours")
