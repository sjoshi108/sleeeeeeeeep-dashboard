
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
st.plotly_chart(fig4)




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





# Average values (replace with actual data if needed)
average_caffeine = 22.345133  # Average caffeine consumption in mg
average_alcohol = 1.201327     # Average alcohol consumption in ounces

# Title of the scorecard
st.header("Average Consumption Metrics")

# Displaying average caffeine consumption
st.metric(label="Average Caffeine Consumption", value=f"{average_caffeine:.2f} mg")

# Displaying average alcohol consumption
st.metric(label="Average Alcohol Consumption", value=f"{average_alcohol:.2f} oz")

# Key explaining the conversions
st.subheader("Key:")
st.write("1 oz of alcohol is approximately equal to 30 milliliters.")
st.write("5 grams of caffeine is approximately equal to 30 mg of caffeine.")

# Additional note
st.subheader("Note: These values represent the average consumption levels in the dataset.")









data = {
    "Condition": ["Zero Alcohol & Caffeine", "Average Alcohol & Caffeine"],
    "Average Sleep Efficiency": [6.14, 5.89]
}

# Create a DataFrame
df5 = pd.DataFrame(data)

# Create heatmap using Plotly
# Create a pivot table for the heatmap
heatmap_data = df5.set_index("Condition").T  # Transpose for correct heatmap format

# Create heatmap using Plotly
fig5 = px.imshow(
    heatmap_data,
    color_continuous_scale="Viridis",
    labels=dict(x="Condition", y="Average Sleep Efficiency (hours)"),
    title="Average Sleep Efficiency Comparison",
)

# Title of the app
st.title("Sleep Efficiency Comparison")

# Display the heatmap
st.plotly_chart(fig5)

##############################################################


#############################################################




import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display
import streamlit as st

df = pd.read_csv("sleep_data_final.csv")  # Replace with the csv file i sent through slack please

# ---- Create Widgets for Filters ----

# Create dropdown for Age Group
age_options = ["All", "Teenagers", "20s", "30s", "40s", "50s", "60s"]
age_dropdown = widgets.Dropdown(
    options=age_options,
    description='Age Group:',
    value='All'
)

# Create dropdown for Gender
gender_options = ["All", "Male", "Female", "Other"]
gender_dropdown = widgets.Dropdown(
    options=gender_options,
    description='Gender:',
    value='All'
)

# Create sliders for Alcohol Consumption
alcohol_slider = widgets.IntRangeSlider(
    value=[0, 5],
    min=0,
    max=int(df['Alcohol_consumption'].max()),
    step=1,
    description='Alcohol Consumption:',
    continuous_update=False
)

# Create sliders for Caffeine Consumption
caffeine_slider = widgets.IntRangeSlider(
    value=[0, 5],
    min=0,
    max=int(df['Caffeine_consumption'].max()),
    step=1,
    description='Caffeine Consumption:',
    continuous_update=False
)

# ---- Display the Widgets ----
display(age_dropdown, gender_dropdown, alcohol_slider, caffeine_slider)

# ---- Function to Filter Data and Plot ----
def update_metrics(age_group, gender, alcohol_range, caffeine_range):
    # Define the age group ranges
    age_ranges = {
        "Teenagers": (9, 19),
        "20s": (20, 29),
        "30s": (30, 39),
        "40s": (40, 49),
        "50s": (50, 59),
        "60s": (60, 69)
    }

    # Copy original DataFrame to avoid modifying it directly
    filtered_df = df.copy()

    # Apply Age Filter
    if age_group != "All":
        age_min, age_max = age_ranges[age_group]
        filtered_df = filtered_df[(filtered_df["Age"] >= age_min) & (filtered_df["Age"] <= age_max)]

    # Apply Gender Filter
    if gender != "All":
        filtered_df = filtered_df[filtered_df["Gender"] == gender]

    # Apply Alcohol Consumption Filter
    filtered_df = filtered_df[(filtered_df["Alcohol_consumption"] >= alcohol_range[0]) &
                              (filtered_df["Alcohol_consumption"] <= alcohol_range[1])]

    # Apply Caffeine Consumption Filter
    filtered_df = filtered_df[(filtered_df["Caffeine_consumption"] >= caffeine_range[0]) &
                              (filtered_df["Caffeine_consumption"] <= caffeine_range[1])]

    # Optional: Display Filtered Data
    print(f"Filtered Data: {len(filtered_df)} Participants")
    display(filtered_df)

    # Optional: Add Plots Based on Filtered Data
    print("Sleep Metrics by Filters")

    # 1. Bar Plot for Sleep Duration
    fig_duration = px.bar(filtered_df, x="Age", y="Sleep_Duration", color="Gender",
                          title="Sleep Duration by Age & Gender")
    fig_duration.show()

    # 2. Bar Plot for Sleep Efficiency
    fig_efficiency = px.bar(filtered_df, x="Age", y="Sleep_efficiency", color="Gender",
                             title="Sleep Efficiency by Age & Gender")
    fig_efficiency.show()

    # 3. Bar Plot for Awakenings
    fig_awakenings = px.bar(filtered_df, x="Age", y="Awakenings", color="Gender",
                             title="Awakenings by Age & Gender")
    fig_awakenings.show()

    # 4. Bar Plot for Light Sleep
    fig_light_sleep = px.bar(filtered_df, x="Age", y="Light_Sleep_Duration", color="Gender",
                              title="Light Sleep by Age & Gender")
    fig_light_sleep.show()

    # 5. Bar Plot for Deep Sleep
    fig_deep_sleep = px.bar(filtered_df, x="Age", y="Deep_Sleep_Duration", color="Gender",
                             title="Deep Sleep by Age & Gender")
    fig_deep_sleep.show()

    # 6. Bar Plot for REM Sleep
    fig_rem_sleep = px.bar(filtered_df, x="Age", y="Rem_Sleep_Duration", color="Gender",
                            title="REM Sleep by Age & Gender")
    fig_rem_sleep.show()

# ---- Observe Widget Changes ----
widgets.interactive(update_metrics,
                    age_group=age_dropdown,
                    gender=gender_dropdown,
                    alcohol_range=alcohol_slider,
                    caffeine_range=caffeine_slider)











page_bg_img = '''
<style>
body {
    background-image: url("https://images.app.goo.gl/UMx5ysUiCgW6yGpr5");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
}
</style>
'''

# Apply the CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and other components
st.title("Sleep Dashboard")
st.write("Welcome to our sleep study dashboard. Explore the data and insights below.")

# Example chart or component
st.line_chart([1, 2, 3, 4])




# Average values (replace with actual data if needed)
average_caffeine = 22.345133  # Average caffeine consumption in mg
average_alcohol = 1.201327     # Average alcohol consumption in ounces

# Title of the scorecard
st.header("Average Consumption Metrics")

# Displaying average caffeine consumption
st.metric(label="Average Caffeine Consumption", value=f"{average_caffeine:.2f} mg")

# Displaying average alcohol consumption
st.metric(label="Average Alcohol Consumption", value=f"{average_alcohol:.2f} oz")

# Key explaining the conversions
st.subheader("Key:")
st.write("1 oz of alcohol is approximately equal to 30 milliliters.")
st.write("5 grams of caffeine is approximately equal to 30 mg of caffeine.")

# Additional note
st.subheader("Note: These values represent the average consumption levels in the dataset.")




number_of_participants = 452  # Total number of participants
age_range = "9 - 69 years"
genders = {
    "Male": 228,   # Example count of male participants
    "Female": 224, # Example count of female participants
    "Other": 0     # Example count of other genders
}

# Title of the scorecard
st.header("Participant Demographics")

# Displaying number of participants
st.metric(label="Number of Participants", value=number_of_participants)

# Displaying age range
st.metric(label="Age Range", value=age_range)

# Displaying gender distribution
st.subheader("Gender Distribution")
for gender, count in genders.items():
    st.metric(label=gender, value=count)

# Additional note
st.subheader("Note: Gender counts are based on participant responses.")



# Sample data
data13 = {
    "Condition": ["Zero Alcohol & Caffeine", "Average Alcohol & Caffeine"],
    "Average Sleep Efficiency": [6.14, 5.89]
}

# Create a DataFrame
df18 = pd.DataFrame(data13)

# Create heatmap using Plotly
# Create a pivot table for the heatmap
heatmap_data = df18.set_index("Condition").T  # Transpose for correct heatmap format

# Create heatmap using Plotly
fig18 = px.imshow(
    heatmap_data,
    color_continuous_scale="Viridis",
    labels=dict(x="Condition", y="Average Sleep Efficiency (hours)"),
    title="Average Sleep Efficiency Comparison",
)

# Title of the app
st.title("Sleep Efficiency Comparison")

# Display the heatmap
st.plotly_chart(fig18)

# Key for sleep efficiency definition
st.markdown("""
### Key:
- **Sleep Efficiency:** A measure of the proportion of time in bed spent asleep.
""")


import streamlit as st
import pandas as pd

# Data with sleep durations in decimal hours
data9 = {
    "Sleep_Duration": [7.378676],  # Sleep duration in hours
    "Awakenings": [136],
    "Light_Sleep_Duration": [2.716397],  # Light sleep duration in hours
    "Deep_Sleep_Duration": [4.271765],  # Deep sleep duration in hours
    "Rem_Sleep_Duration": [1.658235],  # REM sleep duration in hours
    "Sleep_efficiency_hours": [6.144044]  # Sleep efficiency in hours
}

# Create DataFrame
df9 = pd.DataFrame(data9)

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
st.metric(label="Average Sleep Duration", value=convert_hours_to_h_m(df9['Sleep_Duration'].mean()))
st.metric(label="Average Awakenings", value=f"{df9['Awakenings'].mean():.2f}")
st.metric(label="Average Light Sleep Duration", value=convert_hours_to_h_m(df9['Light_Sleep_Duration'].mean()))
st.metric(label="Average Deep Sleep Duration", value=convert_hours_to_h_m(df9['Deep_Sleep_Duration'].mean()))
st.metric(label="Average REM Sleep Duration", value=convert_hours_to_h_m(df9['Rem_Sleep_Duration'].mean()))
st.metric(label="Average Sleep Efficiency Hours", value=convert_hours_to_h_m(df9['Sleep_efficiency_hours'].mean()))

