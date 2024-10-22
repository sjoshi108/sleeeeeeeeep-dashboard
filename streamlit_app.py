
import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
sleep_data = pd.read_csv("sleep_data_final.csv")
health_and_lifestyle_data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
rail_workers_data = pd.read_csv("rail_workers_sleep_data.csv")

# Set wide page layout
st.set_page_config(layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Introduction", "Consumption Habits & Sleep Efficiency", "Lifestyle Factors & Stress", "Work-Related Stress & Sleep", "Conclusion"])

# Page 1: Introduction
if page == "Introduction":
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

# Page 2: Consumption Habits & Sleep Efficiency
elif page == "Consumption Habits & Sleep Efficiency":
    st.header("Page 2: The Impact of Consumption Habits on Sleep Efficiency")
    col1, col2, col3 = st.columns(3)
    
    # Graph 1: Caffeine vs Sleep Efficiency - Scatter plot with distinct color
    with col1:
        fig1 = px.scatter(sleep_data, x="Caffeine_consumption", y="Sleep_efficiency", trendline="ols", 
                          title="Caffeine Consumption vs Sleep Efficiency", color_discrete_sequence=["#FF6347"])
        st.plotly_chart(fig1, use_container_width=True)
    
    # Graph 2: Alcohol vs Sleep Efficiency - Box plot for better comparison
    with col2:
        fig2 = px.box(sleep_data, x="Alcohol_consumption", y="Sleep_efficiency", title="Alcohol Consumption vs Sleep Efficiency", color_discrete_sequence=["#20B2AA"])
        st.plotly_chart(fig2, use_container_width=True)
    
    # Graph 3: Sleep Efficiency by Gender - Histogram
    with col3:
        fig3 = px.histogram(sleep_data, x="Sleep_efficiency", color="Gender", title="Sleep Efficiency Distribution by Gender", color_discrete_sequence=["#FF1493", "#1E90FF"])
        st.plotly_chart(fig3, use_container_width=True)

# Page 3: Lifestyle Factors & Stress
elif page == "Lifestyle Factors & Stress":
    st.header("Page 3: Lifestyle Factors and Stress")
    col1, col2, col3 = st.columns(3)

    # Graph 4: Stress vs Sleep Quality - Scatter plot
    with col1:
        fig4 = px.scatter(health_and_lifestyle_data, x="Stress_Level", y="Quality_of_Sleep", trendline="ols", title="Stress Levels vs Quality of Sleep", color_discrete_sequence=["#32CD32"])
        st.plotly_chart(fig4, use_container_width=True)
    
    # Graph 5: Physical Activity vs Sleep Quality - Bar plot (changed from line plot)
    with col2:
        fig5 = px.bar(health_and_lifestyle_data, x="Physical_Activity_Level", y="Quality_of_Sleep", title="Physical Activity vs Quality of Sleep", color_discrete_sequence=["#FFD700"])
        st.plotly_chart(fig5, use_container_width=True)
    
    # Graph 6: Sleep Quality by Occupation - Bar chart
    with col3:
        fig6 = px.bar(health_and_lifestyle_data, x="Occupation", y="Quality_of_Sleep", title="Quality of Sleep by Occupation", color_discrete_sequence=["#4682B4"])
        st.plotly_chart(fig6, use_container_width=True)

# Page 4: Work-Related Stress & Sleep
elif page == "Work-Related Stress & Sleep":
    st.header("Page 4: Work-Related Stress Impact on Sleep")
    col1, col2, col3 = st.columns(3)

    # Graph 7: Job Security vs Sleep Loss - Scatter plot
    with col1:
        fig7 = px.scatter(rail_workers_data, x="Job_Security", y="Sleep_loss", trendline="ols", title="Job Security vs Sleep Loss", color_discrete_sequence=["#FF4500"])
        st.plotly_chart(fig7, use_container_width=True)
    
    # Graph 8: Work Surges vs Sleep Loss - Heatmap for correlation visualization
    with col2:
        fig8 = px.density_heatmap(rail_workers_data, x="Surges_in_work", y="Sleep_loss", title="Work Surges vs Sleep Loss", color_continuous_scale="Viridis")
        st.plotly_chart(fig8, use_container_width=True)
    
    # Graph 9: Life Events vs Sleep Loss - Scatter plot
    with col3:
        fig9 = px.scatter(rail_workers_data, x="Total_life_events", y="Sleep_loss", trendline="ols", title="Life Events vs Sleep Loss", color_discrete_sequence=["#8A2BE2"])
        st.plotly_chart(fig9, use_container_width=True)
##############################################

import plotly.express as px
import plotly.graph_objects as go

# Load your newly uploaded rail workers dataset
df_railworkers_clean = pd.read_csv("df_railworkers_clean(1).csv")

# Dictionary for more descriptive labels
variable_labels = {
    'Job_pressure': 'Job Pressure',
    'Emergencies': 'Emergencies',
    'Lack_of_control': 'Lack of Control',
    'Mgmt_policies': 'Management Policies',
    'Surges_in_work': 'Work Surges',
    'Communication': 'Communication',
    'Inadeq_Staff': 'Inadequate Staffing',
    'Resp_for_others_safety': 'Responsibility for Others\' Safety',
    'BreakTime': 'Break Time',
    'TimeOff': 'Time Off',
    'Sleep_loss': 'Sleep Loss'
}

# Correlation Analysis Function
def perform_correlation_analysis(df, stress_columns):
    # Ensure all columns in the list exist in the DataFrame before performing correlation
    missing_columns = [col for col in stress_columns + ['Sleep_loss'] if col not in df.columns]
    if missing_columns:
        raise KeyError(f"The following columns are missing from the DataFrame: {missing_columns}")

    correlation_matrix = df[stress_columns + ['Sleep_loss']].corr()
    return correlation_matrix['Sleep_loss'].sort_values(ascending=False)

# Full list of stress-related columns
stress_columns = [
    'Job_pressure', 'Emergencies', 'Lack_of_control', 'Mgmt_policies',
    'Surges_in_work', 'Communication', 'Inadeq_Staff', 'Resp_for_others_safety',
    'BreakTime', 'TimeOff'
]

# Run the correlation analysis
try:
    sleep_loss_corr = perform_correlation_analysis(df_railworkers_clean, stress_columns)
    
    # Rename the index in the Series and convert it to a DataFrame with 'Sleep Loss' as the column name
    sleep_loss_corr_renamed = sleep_loss_corr.rename(index=variable_labels).to_frame()
    sleep_loss_corr_renamed.columns = ['Sleep Loss']
    
    # Display the correlation results in the Streamlit app
    st.header("Correlation Analysis: Stress Factors and Sleep Loss")
    st.write("Here are the correlations between sleep loss and stress-related factors:")
    st.dataframe(sleep_loss_corr_renamed)

    # Plot the heatmap using Plotly
    st.subheader("Heatmap of Correlation with Sleep Loss")
    fig = go.Figure(data=go.Heatmap(
        z=sleep_loss_corr_renamed['Sleep Loss'].values.reshape(1, -1),  # reshape for heatmap
        x=sleep_loss_corr_renamed.index,
        y=['Sleep Loss'],
        colorscale='Viridis',
        showscale=True,
        zmin=-1,  # correlation ranges from -1 to 1
        zmax=1
    ))

    fig.update_layout(
        title="Correlation of Stress Factors with Sleep Loss",
        xaxis_title="Stress Factors",
        yaxis_title="",
        height=400
    )

    # Show the heatmap in Streamlit
    st.plotly_chart(fig)

except KeyError as e:
    st.error(f"Error: {e}")


    
##########################################
# Page 5: Conclusion
elif page == "Conclusion":
    st.header("Page 5: Conclusion")
    st.write("""
    Through this analysis, we have uncovered key insights about the various factors influencing sleep quality:
    1. **Consumption habits** like caffeine and alcohol consumption have a notable impact on sleep efficiency, with alcohol showing a stronger negative correlation.
    2. **Stress levels** and **physical activity** play a significant role in sleep quality, with higher physical activity linked to better sleep outcomes.
    3. In the case of **rail workers**, job insecurity and work surges directly contribute to reduced sleep quality, highlighting the importance of addressing job-related stress.
    By addressing these factors, individuals and organizations can take steps toward improving sleep health and overall well-being.
    """)





