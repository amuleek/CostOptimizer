from dash import Dash, html, dash_table
from aws_client import get_ec2_instances
from analyzer import analyze_instances

app = Dash(__name__)

instances = get_ec2_instances()
analysis, total_cost = analyze_instances(instances)

app.layout = html.Div([
    html.H1("AWS Cost & Resource Analyzer"),

    html.H3(f"Total Estimated Cost Per Hour: ${round(total_cost,2)}"),

    dash_table.DataTable(
        data=analysis,
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'}
    )
])

if __name__ == "__main__":
    app.run(debug=True)

