import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the dataset
file_path = 'all-ages.csv'
df = pd.read_csv(file_path)

# Data Cleaning
df = df.drop(columns=['index', 'Major_code'])
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Calculations
df['employment_rate'] = df['employed'] / df['total']
df['full_time_year_round_rate'] = df['employed_full_time_year_round'] / df['total']

# Insights
employment_rate_by_category = df.groupby('major_category')['employment_rate'].mean().sort_values(ascending=False)
average_salaries_by_category = df.groupby('major_category')[['median', 'p25th', 'p75th']].mean().sort_values(by='median', ascending=False)
full_time_year_round_rate_by_major = df.groupby('major')['full_time_year_round_rate'].mean().sort_values(ascending=False).head(10)

# Create the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div(children=[
    html.H1(children='Major Employment and Salary Analysis'),

    html.Div(children='''
        Select a major category to filter the data.
    '''),

    dcc.Dropdown(
        id='major-category-dropdown',
        options=[{'label': category, 'value': category} for category in df['major_category'].unique()],
        value=df['major_category'].unique()[0],
        style={'width': '50%'}
    ),

    dcc.Graph(
        id='employment-rate-chart'
    ),

    dcc.Graph(
        id='salary-distribution-chart'
    ),

    dcc.Graph(
        id='full-time-year-round-chart'
    )
])

# Callback to update charts based on selected major category
@app.callback(
    [Output('employment-rate-chart', 'figure'),
     Output('salary-distribution-chart', 'figure'),
     Output('full-time-year-round-chart', 'figure')],
    [Input('major-category-dropdown', 'value')]
)
def update_charts(selected_category):
    filtered_df = df[df['major_category'] == selected_category]

    employment_rate_fig = px.bar(
        filtered_df,
        x='major',
        y='employment_rate',
        title='Employment Rate by Major',
        labels={'employment_rate': 'Employment Rate'}
    )

    salary_distribution_fig = px.bar(
        filtered_df,
        x='major',
        y=['median', 'p25th', 'p75th'],
        title='Salary Distribution by Major',
        labels={'value': 'Salary ($)', 'variable': 'Salary Percentile'}
    )

    full_time_year_round_fig = px.bar(
        filtered_df,
        x='major',
        y='full_time_year_round_rate',
        title='Full-Time Year-Round Employment Rate by Major',
        labels={'full_time_year_round_rate': 'Full-Time Year-Round Employment Rate'}
    )

    return employment_rate_fig, salary_distribution_fig, full_time_year_round_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
