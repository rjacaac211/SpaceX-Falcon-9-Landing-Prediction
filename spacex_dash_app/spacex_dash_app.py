# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TAdd a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown', options=[
                                                                    {'label': 'All Sites', 'value': 'ALL'},
                                                                    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                                    {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                                                    {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                                    {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
                                                                ],
                                                                    value='ALL',
                                                                    placeholder="Select a Launch Site Here",
                                                                    searchable=True
                                ),
                                html.Br(),

                                # Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # Add a slider to select payload range
                                html.Div([
                                    dcc.RangeSlider(
                                        id='payload-slider',
                                        min=0,
                                        max=10000,
                                        step=1000,
                                        marks={0: '0', 2500:'2500', 5000:'5000', 7500:'7500', 10000: '10000'},
                                        value=[min_payload, max_payload]
                                    )
                                ], style={'width': '80%', 'padding': '0px 20px 20px 20px'}),

                                # Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Group data by launch site and calculate total success count for each site
        site_success_counts = spacex_df[spacex_df['class'] == 1].groupby('Launch Site').size().reset_index(name='Success Count')

        # Create pie chart figure
        fig = px.pie(site_success_counts, values='Success Count', names='Launch Site', title='Total Success Launches by Sites')
    else:
        # Filter dataframe for selected site
        selected_site_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # Get success count for selected site
        site_success_count = selected_site_df[selected_site_df['class'] == 1]['class'].count()

        # Create pie chart figure for selected site
        fig = px.pie(values=[site_success_count, len(selected_site_df) - site_success_count],
                     names=['Success', 'Failure'],
                     title=f'Total Success Launches for site {entered_site}')

    return fig

# Add a callback function for updating the scatter chart based on the selected launch site and payload range
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),  # Specify the output component (scatter chart)
    [Input(component_id='site-dropdown', component_property='value'),  # Specify the input components (site dropdown and payload slider)
     Input(component_id="payload-slider", component_property="value")]
)
def update_scatter_chart(selected_site, payload_range):
    # Check if all sites are selected
    if selected_site == 'ALL':
        # Filter the dataframe for payload within the selected range
        filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) & 
                                (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
        # Create scatter plot for all sites
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title='Payload vs. Outcome for All Sites',
                         labels={'class': 'Outcome', 'Payload Mass (kg)': 'Payload Mass (kg)', 'Booster Version Category': 'Booster Version'})
    else:
        # Filter the dataframe for the selected launch site and payload within the selected range
        filtered_df = spacex_df[(spacex_df['Launch Site'] == selected_site) & 
                                (spacex_df['Payload Mass (kg)'] >= payload_range[0]) & 
                                (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
        # Create scatter plot for the selected site
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title=f'Correlation between Payload and Success for {selected_site}',
                         labels={'class': 'Outcome', 'Payload Mass (kg)': 'Payload Mass (kg)', 'Booster Version Category': 'Booster Version'})
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server()
