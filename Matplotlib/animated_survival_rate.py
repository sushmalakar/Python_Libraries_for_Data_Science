import plotly.express as px
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Data_Sets/Titanic-Dataset.csv')

# Animated Bar Chart: Survival Rate by PClass (with animation over time)
fig_animated_class = px.bar(df, x='Pclass', color='Survived',barmode='group', animation_frame='Pclass',
                           labels = {'Pclass':'Passenger Class', 'Survived': 'Survival'},
                           title='Animated Survial Rate by Passenger Class')
fig_animated_class.update_layout(title_x=0.5) # Center the title
fig_animated_class.show()