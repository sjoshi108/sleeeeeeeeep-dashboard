
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the datasets
sleep_data_final = pd.read_csv('sleep_data_final.csv')
sleep_health_and_lifestyle = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')

# Function for Scorecards
def display_scorecards(df):
    st.metric('Average Sleep Duration', round(df['Sleep_Duration'].mean(), 2))
    st.metric('Average Sleep Efficiency', round(df['Sleep_efficiency'].mean(), 2))
    st.metric('Average Stress Level', round(df['Stress_Level'].mean(), 2))

# Page for Sleep Data Final
def sleep_data_final_page():
    st.title('Sleep Data Analysis')
    
    st.sidebar.header("Filter Data")
    gender = st.sidebar.selectbox('Gender', options=['All', 'Male', 'Female'])
    if gender != 'All':
        df = sleep_data_final[sleep_data_final['Gender'] == gender]
    else:
        df = sleep_data_final
    
    st.write("## Overview of Sleep Data")
    display_scorecards(df)

    st.write("### Sleep Duration Distribution")
    fig1 = px.histogram(df, x='Sleep_Duration', nbins=20)
    st.plotly_chart(fig1)

    st.write("### Correlation between Sleep Efficiency and Caffeine Consumption")
    fig2 = px.scatter(df, x='Caffeine_consumption', y='Sleep_efficiency', trendline='ols')
    st.plotly_chart(fig2)

    # More visualizations can be added following similar structure
    st.write("### Awakenings vs Sleep Duration")
    fig3 = px.scatter(df, x='Awakenings', y='Sleep_Duration')
    st.plotly_chart(fig3)

# Page for Sleep Health and Lifestyle Data
def sleep_health_lifestyle_page():
    st.title('Sleep Health and Lifestyle Analysis')
    
    st.sidebar.header("Filter Data")
    occupation = st.sidebar.selectbox('Occupation', options=['All'] + sleep_health_and_lifestyle['Occupation'].unique().tolist())
    if occupation != 'All':
        df = sleep_health_and_lifestyle[sleep_health_and_lifestyle['Occupation'] == occupation]
    else:
        df = sleep_health_and_lifestyle

    st.write("## Overview of Lifestyle Data")
    display_scorecards(df)

    st.write("### Sleep Duration by Occupation")
    fig1 = px.box(df, x='Occupation', y='Sleep_Duration')
    st.plotly_chart(fig1)

    st.write("### Sleep Quality vs Stress Level")
    fig2 = px.scatter(df, x='Stress_Level', y='Quality_of_Sleep', trendline='ols')
    st.plotly_chart(fig2)

    # Additional visualizations for lifestyle factors
    st.write("### Physical Activity Level vs Sleep Duration")
    fig3 = px.scatter(df, x='Physical_Activity_Level', y='Sleep_Duration')
    st.plotly_chart(fig3)

# Main App Structure
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Sleep Data", "Health and Lifestyle Data"])
    
    if page == "Sleep Data":
        sleep_data_final_page()
    elif page == "Health and Lifestyle Data":
        sleep_health_lifestyle_page()

if __name__ == "__main__":
    main()


