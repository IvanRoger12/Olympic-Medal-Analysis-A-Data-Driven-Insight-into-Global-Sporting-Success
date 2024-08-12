
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from google.colab import files

# Step 1: Upload the datasets in Google Colab
uploaded = files.upload()

# Load the datasets (make sure the filenames match the uploaded files)
medals = pd.read_csv('medals.csv')  # Ensure this matches the uploaded file
athletes = pd.read_csv('athletes.csv')
teams = pd.read_csv('teams.csv')

# Data cleaning
medals.dropna(inplace=True)
athletes.dropna(inplace=True)
teams.dropna(inplace=True)

# Insight 1: Gender Distribution Among Medalists
gender_distribution = medals['gender'].value_counts().reset_index()
gender_distribution.columns = ['gender', 'medal_count']

# Visualization 1: Pie Chart of Gender Distribution Among Medalists using Plotly
fig1 = px.pie(gender_distribution, names='gender', values='medal_count',
              title='Gender Distribution Among Medalists',
              color_discrete_sequence=['#ff9999', '#66b3ff'],
              hole=0.3)
fig1.update_traces(textinfo='percent+label')
fig1.show()

# Insight 2: Medals by Event Type
event_type_distribution = medals['event_type'].value_counts().reset_index()
event_type_distribution.columns = ['Event Type', 'Number of Medals']

# Visualization 2: Bar Plot of Medals by Event Type using Plotly
fig2 = px.bar(event_type_distribution, x='Event Type', y='Number of Medals',
              title='Distribution of Medals by Event Type',
              labels={'Event Type': 'Type of Event (Individual vs Team)', 'Number of Medals': 'Number of Medals Won'},
              color='Event Type', color_discrete_sequence=px.colors.qualitative.Set1,
              text='Number of Medals')

# Adding customizations
fig2.update_traces(texttemplate='%{text}', textposition='outside')  # Show the number of medals above the bars
fig2.update_layout(template="plotly_white", legend_title_text='Event Type', 
                   xaxis_title="Type of Event",
                   yaxis_title="Total Number of Medals",
                   showlegend=True)

# Display the updated plot
fig2.show()
