
import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
sleep_data = pd.read_csv("sleep_data_final.csv")
health_and_lifestyle_data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
rail_workers_data = pd.read_csv("rail_workers_sleep_data.csv")

# Set wide page layout
st.set_page_config(layout="wide")

# Page 1: Introduction
st.title("Sleep, Lifestyle, and Job Factors: A Data Analysis Journey")

st.header("Introduction: The Modern Sleep Problem")
st.write("""
Sleep quality is declining globally, influenced by numerous factors including lifestyle choices, consumption habits, and job-related stress.
In this analysis, we explore how caffeine and alcohol consumption, stress, physical activity, and job-related stress impact sleep efficiency, 
stress levels, and overall well-being. We are utilizing three datasets:
- General Sleep Data: Provides individual sleep behaviors (e.g., caffeine, alcohol consumption, and sleep efficiency).
- Health and Lifestyle Data: Examines how lifestyle attributes such as physical activity and stress affect sleep.
- Rail Workers' Sleep Data: Focuses on job-related stress and its impact on rail workers' sleep quality.
""")

# Page 2: Impact of Consumption Habits on Sleep Efficiency
st.header("Page 2: The Impact of Consumption Habits on Sleep Efficiency")

# Graph 1: Caffeine vs Sleep Efficiency
fig1 = px.scatter(sleep_data, x="Caffeine_consumption", y="Sleep_efficiency", trendline="ols", title="Caffeine Consumption vs Sleep Efficiency")
st.plotly_chart(fig1, use_container_width=True)

# Graph 2: Alcohol vs Sleep Efficiency
fig2 = px.scatter(sleep_data, x="Alcohol_consumption", y="Sleep_efficiency", trendline="ols", title="Alcohol Consumption vs Sleep Efficiency")
st.plotly_chart(fig2, use_container_width=True)

# Graph 3: Sleep Efficiency by Gender
fig3 = px.histogram(sleep_data, x="Sleep_efficiency", color="Gender", title="Sleep Efficiency Distribution by Gender")
st.plotly_chart(fig3, use_container_width=True)

# Page 3: Lifestyle Factors and Stress
st.header("Page 3: Lifestyle Factors and Stress")

# Graph 4: Stress vs Sleep Quality (Corrected to Quality_of_Sleep)
fig4 = px.scatter(health_and_lifestyle_data, x="Stress_Level", y="Quality_of_Sleep", trendline="ols", title="Stress Levels vs Quality of Sleep")
st.plotly_chart(fig4, use_container_width=True)

# Graph 5: Physical Activity vs Sleep Quality (Corrected to Quality_of_Sleep)
fig5 = px.scatter(health_and_lifestyle_data, x="Physical_Activity_Level", y="Quality_of_Sleep", trendline="ols", title="Physical Activity vs Quality of Sleep")
st.plotly_chart(fig5, use_container_width=True)

# Graph 6: Sleep Quality by Occupation (Corrected to Quality_of_Sleep)
fig6 = px.bar(health_and_lifestyle_data, x="Occupation", y="Quality_of_Sleep", title="Quality of Sleep by Occupation")
st.plotly_chart(fig6, use_container_width=True)

# Page 4: Work-Related Stress Impact on Sleep
st.header("Page 4: Work-Related Stress Impact on Sleep")

# Graph 7: Job Security vs Sleep Loss (Corrected to Sleep_loss for rail workers data)
fig7 = px.scatter(rail_workers_data, x="Job_Security", y="Sleep_loss", trendline="ols", title="Job Security vs Sleep Loss")
st.plotly_chart(fig7, use_container_width=True)

# Graph 8: Work Surges vs Sleep Loss (Corrected to Sleep_loss for rail workers data)
fig8 = px.scatter(rail_workers_data, x="Surges_in_work", y="Sleep_loss", trendline="ols", title="Work Surges vs Sleep Loss")
st.plotly_chart(fig8, use_container_width=True)

# Graph 9: Life Events vs Sleep Loss (Corrected to Sleep_loss for rail workers data)
fig9 = px.scatter(rail_workers_data, x="Total_life_events", y="Sleep_loss", trendline="ols", title="Life Events vs Sleep Loss")
st.plotly_chart(fig9, use_container_width=True)

# Page 5: Conclusion
st.header("Page 5: Conclusion")

st.write("""
Through this analysis, we have uncovered key insights about the various factors influencing sleep quality:
1. **Consumption habits** like caffeine and alcohol consumption have a notable impact on sleep efficiency, with alcohol showing a stronger negative correlation.
2. **Stress levels** and **physical activity** play a significant role in sleep quality, with higher physical activity linked to better sleep outcomes.
3. In the case of **rail workers**, job insecurity and work surges directly contribute to reduced sleep quality, highlighting the importance of addressing job-related stress.
By addressing these factors, individuals and organizations can take steps toward improving sleep health and overall well-being.
""")
