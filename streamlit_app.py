
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt



# Load the datasets
sleep_data_final = pd.read_csv('sleep_data_final.csv')
sleep_health_and_lifestyle = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
rail_workers_sleep_data = pd.read_csv('rail_workers_sleep_data.csv')

# Set page configuration for wide view
st.set_page_config(layout="wide", page_title="Sleep and Lifestyle Analysis", page_icon=":bar_chart:")


# Function for displaying scorecards in a separate row
def display_scorecards(df, scorecard_columns):
    col1, col2, col3 = st.columns(3)
    for i, col_name in enumerate(scorecard_columns):
        with [col1, col2, col3][i % 3]:
            st.metric(col_name, round(df[col_name].mean(), 2))


# Introduction Page
def introduction_page():
    st.title('Introduction to Sleep and Lifestyle Analysis')
    st.write('''This app explores the relationship between various lifestyle factors and sleep quality using three datasets:
                general sleep data, lifestyle data, and rail workers' sleep patterns. Each page focuses on a different hypothesis, 
                showcasing complex visualizations to highlight correlations and patterns in the data. Additionally, key metrics are 
                presented in scorecards to provide quick insights.''')

# Hypothesis 1: Caffeine and Alcohol impact on Sleep Efficiency
def page_one():
    st.title('Hypothesis 1: Caffeine and Alcohol Consumption vs Sleep Efficiency')
    
    st.sidebar.header("Filter Data")
    gender = st.sidebar.selectbox('Gender', options=['All', 'Male', 'Female'])
    if gender != 'All':
        df = sleep_data_final[sleep_data_final['Gender'] == gender]
    else:
        df = sleep_data_final

    st.write("### Key Metrics")
    display_scorecards(df, ['Caffeine_consumption', 'Alcohol_consumption', 'Sleep_efficiency'])

    # Arrange visualizations in 3 wide columns
    col1, col2, col3 = st.columns([2, 2, 2])

    # Pie chart
    with col1:
        st.write("### Gender Distribution")
        fig1 = px.pie(df, names='Gender', title='Gender Distribution', color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig1)

    # 3D Scatter plot
    with col2:
        st.write("### 3D Graph: Caffeine, Alcohol, and Sleep Efficiency")
        fig2 = px.scatter_3d(df, x='Caffeine_consumption', y='Alcohol_consumption', z='Sleep_efficiency', color='Gender',
                             color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(fig2)

    # Scatter plot for correlation
    with col3:
        st.write("### Sleep Efficiency vs Caffeine Consumption")
        fig3 = px.scatter(df, x='Caffeine_consumption', y='Sleep_efficiency', color='Gender', trendline='ols',
                          color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig3)

    # Heatmap at the bottom
    st.write("### Heatmap of Sleep Factors")
    plt.figure(figsize=(10,6))
    sns.heatmap(df[['Caffeine_consumption', 'Alcohol_consumption', 'Sleep_efficiency']].corr(), annot=True, cmap='coolwarm')
    st.pyplot(plt)

# Hypothesis 2: Physical Activity and Stress impact on Sleep Quality
def page_two():
    st.title('Hypothesis 2: Physical Activity and Stress Levels vs Sleep Quality')
    
    st.sidebar.header("Filter Data")
    occupation = st.sidebar.selectbox('Occupation', options=['All'] + sleep_health_and_lifestyle['Occupation'].unique().tolist())
    if occupation != 'All':
        df = sleep_health_and_lifestyle[sleep_health_and_lifestyle['Occupation'] == occupation]
    else:
        df = sleep_health_and_lifestyle

    st.write("### Key Metrics")
    display_scorecards(df, ['Physical_Activity_Level', 'Stress_Level', 'Quality_of_Sleep'])

    # Arrange visualizations in 3 wide columns
    col1, col2, col3 = st.columns([2, 2, 2])

    # Pie chart
    with col1:
        st.write("### Occupation Distribution")
        fig1 = px.pie(df, names='Occupation', title='Occupation Distribution', color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig1)

    # 3D Graph
    with col2:
        st.write("### 3D Graph: Physical Activity, Stress Level, and Sleep Quality")
        fig2 = px.scatter_3d(df, x='Physical_Activity_Level', y='Stress_Level', z='Quality_of_Sleep', color='Occupation',
                             color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig2)

    # Scatter plot
    with col3:
        st.write("### Stress Level vs Sleep Quality")
        fig3 = px.scatter(df, x='Stress_Level', y='Quality_of_Sleep', color='Occupation', trendline='ols',
                          color_discrete_sequence=px.colors.qualitative.Vivid)
        st.plotly_chart(fig3)

    # Heatmap at the bottom
    st.write("### Heatmap of Lifestyle Factors")
    plt.figure(figsize=(10,6))
    sns.heatmap(df[['Physical_Activity_Level', 'Stress_Level', 'Quality_of_Sleep']].corr(), annot=True, cmap='coolwarm')
    st.pyplot(plt)

# Hypothesis 3: Job-related Factors impact on Sleep and Stress (Rail Workers)
def page_three():
    st.title('Hypothesis 3: Job-Related Factors vs Sleep and Stress (Rail Workers)')
    
    st.sidebar.header("Filter Data")
    job_type = st.sidebar.selectbox('Job Type', options=['All'] + rail_workers_sleep_data['Job_type'].unique().tolist())
    if job_type != 'All':
        df = rail_workers_sleep_data[rail_workers_sleep_data['Job_type'] == job_type]
    else:
        df = rail_workers_sleep_data

    st.write("### Key Metrics")
    display_scorecards(df, ['Job_Security', 'Surges_in_work', 'Total_life_events'])

    # Arrange visualizations in 3 wide columns
    col1, col2, col3 = st.columns([2, 2, 2])

    # Pie chart
    with col1:
        st.write("### Job Type Distribution")
        fig1 = px.pie(df, names='Job_type', title='Job Type Distribution', color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig1)

    # 3D Graph
    with col2:
        st.write("### 3D Graph: Job Security, Surges in Work, and Sleep Duration")
        fig2 = px.scatter_3d(df, x='Job_Security', y='Surges_in_work', z='Total_years_present_job', color='Sex',
                             color_discrete_sequence=px.colors.qualitative.Alphabet)
        st.plotly_chart(fig2)

    # Scatter plot
    with col3:
        st.write("### Surges in Work vs Total Life Events")
        fig3 = px.scatter(df, x='Surges_in_work', y='Total_life_events', color='Sex', trendline='ols',
                          color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig3)

    # Heatmap at the bottom
    st.write("### Heatmap of Job-Related Factors")
    plt.figure(figsize=(10,6))
    sns.heatmap(df[['Job_Security', 'Surges_in_work', 'Total_years_present_job']].corr(), annot=True, cmap='coolwarm')
    st.pyplot(plt)

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
    page = st.sidebar.radio("Go to", ["Introduction", "Caffeine and Alcohol vs Sleep", "Activity and Stress vs Sleep", "Job Factors vs Sleep", "Conclusion"])
    
    if page == "Introduction":
        introduction_page()
    elif page == "Caffeine and Alcohol vs Sleep":
        page_one()
    elif page == "Activity and Stress vs Sleep":
        page_two()
    elif page == "Job Factors vs Sleep":
        page_three()
    elif page == "Conclusion":
        page_four()

if __name__ == "__main__":
    main()

