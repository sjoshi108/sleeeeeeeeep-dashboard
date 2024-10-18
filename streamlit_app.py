
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

fig4 = px.bar(df, x='Stress_Level', y='Quality_of_Sleep',
             title="Average Quality of Sleep by Stress Level",
             labels={'Stress_Level': 'Stress_Level', 'Quality_of_Sleep': 'Average Quality of Sleep'})
fig4.show()




data = {
    "Sleep_Duration": [7.378676],  # Sleep duration in hours
    "Awakenings": [136],
    "Light_Sleep_Duration": [2.716397],  # Light sleep duration in hours
    "Deep_Sleep_Duration": [4.271765],  # Deep sleep duration in hours
    "Rem_Sleep_Duration": [1.658235],  # REM sleep duration in hours
    "Sleep_efficiency_hours": [6.144044]  # Sleep efficiency in hours
}

# Create DataFrame
df = pd.DataFrame(data)

# Title of the app
st.title("Sleep Study Overview")

# Subtitle indicating alcohol and caffeine consumption
st.subheader("Note: Alcohol and Caffeine Consumption was at 0")

# Function to convert hours to hours and minutes
def convert_hours_to_h_m(hours):
    h = int(hours)
    m = int((hours - h) * 60)
    return f"{h} hours {m} minutes"

# Displaying key metrics using st.metric()
st.metric(label="Average Sleep Duration", value=convert_hours_to_h_m(df['Sleep_Duration'].mean()))
st.metric(label="Average Awakenings", value=f"{df['Awakenings'].mean():.2f}")
st.metric(label="Average Light Sleep Duration", value=convert_hours_to_h_m(df['Light_Sleep_Duration'].mean()))
st.metric(label="Average Deep Sleep Duration", value=convert_hours_to_h_m(df['Deep_Sleep_Duration'].mean()))
st.metric(label="Average REM Sleep Duration", value=convert_hours_to_h_m(df['Rem_Sleep_Duration'].mean()))
st.metric(label="Average Sleep Efficiency Hours", value=convert_hours_to_h_m(df['Sleep_efficiency_hours'].mean()))


