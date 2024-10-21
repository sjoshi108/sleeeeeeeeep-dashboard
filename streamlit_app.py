
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the datasets
sleep_data_final = pd.read_csv('sleep_data_final.csv')
sleep_health_and_lifestyle = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
rail_workers_sleep_data = pd.read_csv('rail_workers_sleep_data.csv')

# Set a background image for the app
page_bg_img = '''
<style>
body {
background-image: url("https://www.example.com/background-image.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Hypothesis 1: Caffeine and Alcohol impact on Sleep Efficiency
def page_one():
    st.title('Hypothesis 1: Caffeine and Alcohol Consumption vs Sleep Efficiency')
    
    st.sidebar.header("Filter Data")
    gender = st.sidebar.selectbox('Gender', options=['All', 'Male', 'Female'])
    if gender != 'All':
        df = sleep_data_final[sleep_data_final['Gender'] == gender]
    else:
        df = sleep_data_final
    
    st.write("### Sleep Efficiency vs Caffeine Consumption")
    fig1 = px.scatter(df, x='Caffeine_consumption', y='Sleep_efficiency', color='Gender', trendline='ols')
    st.plotly_chart(fig1)

    st.write("### Sleep Efficiency vs Alcohol Consumption")
    fig2 = px.scatter(df, x='Alcohol_consumption', y='Sleep_efficiency', color='Gender', trendline='ols')
    st.plotly_chart(fig2)

# Hypothesis 2: Physical Activity and Stress impact on Sleep Quality
def page_two():
    st.title('Hypothesis 2: Physical Activity and Stress Levels vs Sleep Quality')
    
    st.sidebar.header("Filter Data")
    occupation = st.sidebar.selectbox('Occupation', options=['All'] + sleep_health_and_lifestyle['Occupation'].unique().tolist())
    if occupation != 'All':
        df = sleep_health_and_lifestyle[sleep_health_and_lifestyle['Occupation'] == occupation]
    else:
        df = sleep_health_and_lifestyle
    
    st.write("### Sleep Quality vs Physical Activity Level")
    fig1 = px.scatter(df, x='Physical_Activity_Level', y='Quality_of_Sleep', color='Occupation', trendline='ols')
    st.plotly_chart(fig1)

    st.write("### Sleep Quality vs Stress Level")
    fig2 = px.scatter(df, x='Stress_Level', y='Quality_of_Sleep', color='Occupation', trendline='ols')
    st.plotly_chart(fig2)

# Hypothesis 3: Job-related Factors impact on Sleep and Stress (Rail Workers)
def page_three():
    st.title('Hypothesis 3: Job-Related Factors vs Sleep and Stress (Rail Workers)')
    
    st.sidebar.header("Filter Data")
    job_type = st.sidebar.selectbox('Job Type', options=['All'] + rail_workers_sleep_data['Job_type'].unique().tolist())
    if job_type != 'All':
        df = rail_workers_sleep_data[rail_workers_sleep_data['Job_type'] == job_type]
    else:
        df = rail_workers_sleep_data
    
    st.write("### Sleep Duration vs Job Security")
    fig1 = px.scatter(df, x='Job_Security', y='Total_years_present_job', color='Sex', trendline='ols')
    st.plotly_chart(fig1)

    st.write("### Stress Levels vs Surges in Work")
    fig2 = px.scatter(df, x='Surges_in_work', y='Total_life_events', color='Sex', trendline='ols')
    st.plotly_chart(fig2)

# Conclusion Page
def page_four():
    st.title('Conclusion: Insights on Sleep and Lifestyle Factors')
    st.write('''In conclusion, we explored the relationships between various lifestyle factors and sleep quality. 
                Caffeine and alcohol showed a noticeable impact on sleep efficiency, while physical activity and 
                stress levels influenced the quality of sleep. Job-related factors, especially in high-stress roles 
                such as rail workers, demonstrated correlations between job security, work surges, and stress. 
                These insights highlight the multifaceted nature of sleep health.''')

# Main App Structure
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Caffeine and Alcohol vs Sleep", "Activity and Stress vs Sleep", "Job Factors vs Sleep", "Conclusion"])
    
    if page == "Caffeine and Alcohol vs Sleep":
        page_one()
    elif page == "Activity and Stress vs Sleep":
        page_two()
    elif page == "Job Factors vs Sleep":
        page_three()
    elif page == "Conclusion":
        page_four()

if __name__ == "__main__":
    main()
