
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




    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    import seaborn as sns
    import matplotlib.pyplot as plt
    import streamlit as st
    
    # Load the CSV file you uploaded (adjust the path if necessary)
    df = pd.read_csv("sleep_data_final.csv")  # Update the path
    
    # Define age ranges for filtering
    age_ranges = {
        "Teenagers": (9, 19),
        "20s": (20, 29),
        "30s": (30, 39),
        "40s": (40, 49),
        "50s": (50, 59),
        "60s": (60, 69)
    }
    
    # Add widgets for filtering the data
    st.sidebar.title("Filter Data")
    
    # Dropdown for Age Group
    age_group = st.sidebar.selectbox(
        'Age Group:', options=["All"] + list(age_ranges.keys()), index=0
    )
    
    # Dropdown for Gender
    gender = st.sidebar.selectbox(
        'Gender:', options=["All", "Male", "Female", "Other"], index=0
    )
    
    # Slider for Alcohol Consumption
    alcohol_range = st.sidebar.slider(
        'Alcohol Consumption:', min_value=0, max_value=int(df['Alcohol_consumption'].max()), value=(0, 5)
    )
    
    # Slider for Caffeine Consumption
    caffeine_range = st.sidebar.slider(
        'Caffeine Consumption:', min_value=0, max_value=int(df['Caffeine_consumption'].max()), value=(0, 200)
    )
    
    # Function to filter data based on the selections
    def filter_data(df, age_group, gender, alcohol_range, caffeine_range):
        filtered_df = df.copy()
    
        # Filter by age group
        if age_group != "All":
            age_min, age_max = age_ranges[age_group]
            filtered_df = filtered_df[(filtered_df["Age"] >= age_min) & (filtered_df["Age"] <= age_max)]
    
        # Filter by gender
        if gender != "All":
            filtered_df = filtered_df[filtered_df["Gender"] == gender]
    
        # Filter by alcohol consumption
        filtered_df = filtered_df[
            (filtered_df["Alcohol_consumption"] >= alcohol_range[0]) &
            (filtered_df["Alcohol_consumption"] <= alcohol_range[1])
        ]
    
        # Filter by caffeine consumption
        filtered_df = filtered_df[
            (filtered_df["Caffeine_consumption"] >= caffeine_range[0]) &
            (filtered_df["Caffeine_consumption"] <= caffeine_range[1])
        ]
    
        return filtered_df
    
    # Apply the filters to the dataset
    filtered_df = filter_data(df, age_group, gender, alcohol_range, caffeine_range)
    
    # Display the filtered data summary
    st.write(f"Filtered Data: {len(filtered_df)} Participants")
    st.dataframe(filtered_df)
    
    # Plot: Sleep Duration by Alcohol and Caffeine Levels (Bar Chart)
    fig_sleep_duration = px.bar(
        filtered_df, x="Alcohol_consumption", y="Sleep_Duration", color="Caffeine_consumption",
        title="Sleep Duration by Alcohol & Caffeine Levels"
    )
    st.plotly_chart(fig_sleep_duration)
    
    # Line Chart: Sleep Proportions (REM, Deep, Light) by Alcohol & Caffeine Intake
    fig_sleep_proportions = go.Figure()
    
    fig_sleep_proportions.add_trace(go.Scatter(
        x=filtered_df['Alcohol_consumption'], y=filtered_df['Rem_Sleep_Duration'],
        mode='lines+markers', name='REM Sleep Duration'
    ))
    
    fig_sleep_proportions.add_trace(go.Scatter(
        x=filtered_df['Alcohol_consumption'], y=filtered_df['Deep_Sleep_Duration'],
        mode='lines+markers', name='Deep Sleep Duration'
    ))
    
    fig_sleep_proportions.add_trace(go.Scatter(
        x=filtered_df['Alcohol_consumption'], y=filtered_df['Light_Sleep_Duration'],
        mode='lines+markers', name='Light Sleep Duration'
    ))
    
    fig_sleep_proportions.update_layout(
        title="REM, Deep, Light Sleep Durations by Alcohol Intake",
        xaxis_title="Alcohol Consumption",
        yaxis_title="Sleep Duration (hours)"
    )
    
    st.plotly_chart(fig_sleep_proportions)
    
    # Heatmap: Combined Effects of Age Group & Gender on Sleep Efficiency
    if "Age_Group" not in filtered_df.columns:
        filtered_df["Age_Group"] = pd.cut(filtered_df["Age"], bins=[0, 19, 29, 39, 49, 59, 69], labels=["Teenagers", "20s", "30s", "40s", "50s", "60s"])
    
    heatmap_data = filtered_df.pivot_table(
        values='Sleep_efficiency', index='Age_Group', columns='Gender', aggfunc='mean'
    )
    
    # Plot heatmap with seaborn
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", cbar=True)
    plt.title('Sleep Efficiency by Age Group and Gender')
    
    # Show the heatmap using Streamlit
    st.pyplot(plt)
    






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
        fig100 = px.scatter_3d(health_and_lifestyle_data, x='Physical_Activity_Level', y='Stress_Level', z='Sleep_Duration', 
            color='Physical_Activity_Level', title="Interaction of Physical Activity, Stress Level, and Sleep Duration with Age",
            labels={'Physical_Activity_Level': 'Physical Activity', 'Stress_Level': 'Stress Level', 'Sleep_Duration': 'Sleep Duration', 'Age': 'Age'})
        st.plotly_chart(fig100, use_container_width=True)
    
    # Graph 6: Sleep Quality by Occupation - Bar chart
    with col3:
        fig6 = px.bar(health_and_lifestyle_data, x="Occupation", y="Quality_of_Sleep", title="Quality of Sleep by Occupation", color_discrete_sequence=["#4682B4"])
        st.plotly_chart(fig6, use_container_width=True)








elif page == "Lifestyle Factors & Stress 2":
    st.header("Page 3.5: Lifestyle Factors and Stress")
    col1, col2, col3 = st.columns(3)



    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import streamlit as st
    
    # Load the CSV file (adjust the path as necessary)
    df = pd.read_csv("lifestylewellbeingdata.csv")
    
    # Filter out invalid DAILY_STRESS values and convert to integer
    df_clean = df[df["DAILY_STRESS"] != '36526']
    df_clean["DAILY_STRESS"] = df_clean["DAILY_STRESS"].astype(int)
    
    # Converting 'Timestamp' column to datetime format and extracting Date
    df_clean['Date'] = df['Timestamp'].str.split(' ').str[0]
    df_clean = df_clean.drop_duplicates()
    
    # Moving 'Date' to the first column
    first_column = df_clean.pop('Date')
    df_clean.insert(0, 'Date', first_column)
    
    # Correlation Analysis
    lifestyle_columns = ['SLEEP_HOURS', 'DAILY_STRESS', 'DAILY_STEPS', 'WORK_LIFE_BALANCE_SCORE', 'TIME_FOR_PASSION']
    correlation_matrix = df_clean[lifestyle_columns].corr()
    
    # Page 6: Lifestyle and Wellbeing Analysis
    st.header("Lifestyle and Wellbeing Analysis")
    
    # Display the correlation matrix
    st.subheader("Correlation Matrix")
    st.write("Correlation between Sleep Hours and Lifestyle Variables:")
    st.dataframe(correlation_matrix)
    
    # Plotting the Distribution of Sleep Categories
    def categorize_sleep(hours):
        if hours < 6:
            return 'Short Sleep'
        elif 6 <= hours <= 8:
            return 'Optimal Sleep'
        else:
            return 'Long Sleep'
    
    df_clean['SLEEP_CATEGORY'] = df_clean['SLEEP_HOURS'].apply(categorize_sleep)
    
    st.subheader("Distribution of Sleep Categories")
    fig, ax = plt.subplots()
    sns.countplot(x='SLEEP_CATEGORY', data=df_clean, palette='Set3', ax=ax)
    ax.set_title("Distribution of Sleep Categories", fontsize=16)
    ax.set_xlabel("Sleep Category", fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    st.pyplot(fig)
    
    # Average Sleep Hours by Age and Gender
    st.subheader("Average Sleep Hours by Age and Gender")
    avg_sleep_by_age_gender = df_clean.groupby(['AGE', 'GENDER'])['SLEEP_HOURS'].mean().unstack()
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_sleep_by_age_gender.plot(kind='bar', ax=ax)
    ax.set_title('Average Sleep Hours by Age and Gender', fontsize=14)
    ax.set_ylabel('Average Sleep Hours')
    ax.set_xlabel('Age Group')
    plt.xticks(rotation=0)
    st.pyplot(fig)
    
    # Regression Plot: Sleep Hours vs Work-Life Balance Score
    st.subheader("Sleep Hours vs Work-Life Balance Score")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.regplot(x=df_clean['SLEEP_HOURS'], y=df_clean['WORK_LIFE_BALANCE_SCORE'], scatter_kws={'s':50}, line_kws={'color':'red'}, ax=ax)
    ax.set_title('Sleep Hours vs Work-Life Balance', fontsize=14)
    ax.set_xlabel('Sleep Hours', fontsize=12)
    ax.set_ylabel('Work-Life Balance Score', fontsize=12)
    st.pyplot(fig)
    
    # Regression Plot: Sleep Hours vs Daily Stress
    st.subheader("Sleep Hours vs Daily Stress")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.regplot(x=df_clean['SLEEP_HOURS'], y=df_clean['DAILY_STRESS'], scatter_kws={'s':50}, line_kws={'color':'blue'}, ax=ax)
    ax.set_title('Sleep Hours vs Daily Stress', fontsize=14)
    ax.set_xlabel('Sleep Hours', fontsize=12)
    ax.set_ylabel('Daily Stress', fontsize=12)
    st.pyplot(fig)










# Page 4: Work-Related Stress & Sleep
elif page == "Work-Related Stress & Sleep":
    st.header("Page 4: Work-Related Stress Impact on Sleep")
    col1, col2 = st.columns(2)

    # Graph 7: Job Security vs Sleep Loss - Scatter plot
    with col1:
        
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
            
            
        
            # Plot the heatmap using Plotly
            st.subheader("Heatmap of Correlation with Sleep Loss")
            fig = go.Figure(data=go.Heatmap(
                z=sleep_loss_corr_renamed['Sleep Loss'].values.reshape(1, -1),  # reshape for heatmap
                x=sleep_loss_corr_renamed.index,
                y=['Sleep Loss'],
                colorscale='Viridis',
                showscale=True,
                zmin=0.2,  # correlation ranges from -1 to 1
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




        
    
    # Graph 8: Work Surges vs Sleep Loss - Heatmap for correlation visualization
    with col2:
        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split
        
        # Load the rail workers dataset
        
        
        # Define the stress-related columns and the target variable (Sleep_loss)
        stress_columns = [
            'Job_pressure', 'Emergencies', 'Lack_of_control', 'Mgmt_policies',
            'Surges_in_work', 'Communication', 'Inadeq_Staff', 'Resp_for_others_safety',
            'BreakTime', 'TimeOff'
        ]
        target_column = 'Sleep_loss'
        
        # Split the data into features (X) and target (y)
        X = df_railworkers_clean[stress_columns]
        y = df_railworkers_clean[target_column]
        
        # Train-test split for model training
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train a linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
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
            'TimeOff': 'Time Off'
        }
        
        # Display significant coefficients with readable labels
        significant_coeffs = pd.DataFrame({
            'Variable': stress_columns,
            'Coefficient': model.coef_
        }).sort_values(by='Coefficient', ascending=False)
        
        # Map the variables to more descriptive labels
        significant_coeffs['Variable'] = significant_coeffs['Variable'].map(variable_labels)
        
        # Plot the bar chart with the updated labels
        fig = px.bar(significant_coeffs.head(5), x='Coefficient', y='Variable', orientation='h', 
                     title='Top 5 Predictors of Sleep Loss')
        
        # Show the updated plot in Streamlit
        st.plotly_chart(fig)






        








    
    
        



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





