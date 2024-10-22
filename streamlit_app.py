
import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
sleep_data = pd.read_csv("sleep_data_final.csv")
health_and_lifestyle_data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
rail_workers_data = pd.read_csv("rail_workers_sleep_data.csv")

# Set wide page layout
st.set_page_config(layout="wide")

# Page navigation with buttons
page = 0

if 'page' not in st.session_state:
    st.session_state.page = 0

# Define button actions
def next_page():
    st.session_state.page += 1
    if st.session_state.page > 4:
        st.session_state.page = 0

def prev_page():
    st.session_state.page -= 1
    if st.session_state.page < 0:
        st.session_state.page = 4

# Display the current page based on session state
page = st.session_state.page

if page == 0:
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

elif page == 1:
    st.header("Page 2: The Impact of Consumption Habits on Sleep Efficiency")
    col1, col2, col3 = st.columns(3)
    
    # Graph 1: Caffeine vs Sleep Efficiency with distinct color
    with col1:
        fig1 = px.scatter(sleep_data, x="Caffeine_consumption", y="Sleep_efficiency", trendline="ols", title="Caffeine Consumption vs Sleep Efficiency", color_discrete_sequence=["#636EFA"])
        st.plotly_chart(fig1, use_container_width=True)
    
    # Graph 2: Alcohol vs Sleep Efficiency with distinct color
    with col2:
        fig2 = px.scatter(sleep_data, x="Alcohol_consumption", y="Sleep_efficiency", trendline="ols", title="Alcohol Consumption vs Sleep Efficiency", color_discrete_sequence=["#EF553B"])
        st.plotly_chart(fig2, use_container_width=True)
    
    # Graph 3: Sleep Efficiency by Gender with distinct color
    with col3:
        fig3 = px.histogram(sleep_data, x="Sleep_efficiency", color="Gender", title="Sleep Efficiency Distribution by Gender", color_discrete_sequence=["#00CC96", "#AB63FA"])
        st.plotly_chart(fig3, use_container_width=True)

elif page == 2:
    st.header("Page 3: Lifestyle Factors and Stress")
    col1, col2, col3 = st.columns(3)

    # Graph 4: Stress vs Sleep Quality with distinct color
    with col1:
        fig4 = px.scatter(health_and_lifestyle_data, x="Stress_Level", y="Quality_of_Sleep", trendline="ols", title="Stress Levels vs Quality of Sleep", color_discrete_sequence=["#FFA15A"])
        st.plotly_chart(fig4, use_container_width=True)
    
    # Graph 5: Physical Activity vs Sleep Quality with distinct color
    with col2:
        fig5 = px.scatter(health_and_lifestyle_data, x="Physical_Activity_Level", y="Quality_of_Sleep", trendline="ols", title="Physical Activity vs Quality of Sleep", color_discrete_sequence=["#19D3F3"])
        st.plotly_chart(fig5, use_container_width=True)
    
    # Graph 6: Sleep Quality by Occupation with distinct color
    with col3:
        fig6 = px.bar(health_and_lifestyle_data, x="Occupation", y="Quality_of_Sleep", title="Quality of Sleep by Occupation", color_discrete_sequence=["#FF6692"])
        st.plotly_chart(fig6, use_container_width=True)

elif page == 3:
    st.header("Page 4: Work-Related Stress Impact on Sleep")
    col1, col2, col3 = st.columns(3)

    # Graph 7: Job Security vs Sleep Loss with distinct color
    with col1:
        fig7 = px.scatter(rail_workers_data, x="Job_Security", y="Sleep_loss", trendline="ols", title="Job Security vs Sleep Loss", color_discrete_sequence=["#B6E880"])
        st.plotly_chart(fig7, use_container_width=True)
    
    # Graph 8: Work Surges vs Sleep Loss with distinct color
    with col2:
        fig8 = px.scatter(rail_workers_data, x="Surges_in_work", y="Sleep_loss", trendline="ols", title="Work Surges vs Sleep Loss", color_discrete_sequence=["#FF97FF"])
        st.plotly_chart(fig8, use_container_width=True)
    
    # Graph 9: Life Events vs Sleep Loss with distinct color
    with col3:
        fig9 = px.scatter(rail_workers_data, x="Total_life_events", y="Sleep_loss", trendline="ols", title="Life Events vs Sleep Loss", color_discrete_sequence=["#FECB52"])
        st.plotly_chart(fig9, use_container_width=True)

elif page == 4:
    st.header("Page 5: Conclusion")
    st.write("""
    Through this analysis, we have uncovered key insights about the various factors influencing sleep quality:
    1. **Consumption habits** like caffeine and alcohol consumption have a notable impact on sleep efficiency, with alcohol showing a stronger negative correlation.
    2. **Stress levels** and **physical activity** play a significant role in sleep quality, with higher physical activity linked to better sleep outcomes.
    3. In the case of **rail workers**, job insecurity and work surges directly contribute to reduced sleep quality, highlighting the importance of addressing job-related stress.
    By addressing these factors, individuals and organizations can take steps toward improving sleep health and overall well-being.
    """)

# Add navigation buttons
col1, col2 = st.columns([1,1])
with col1:
    if st.button("Previous"):
        prev_page()
with col2:
    if st.button("Next"):
        next_page()


