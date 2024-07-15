from dash import Dash, dash_table
import pandas as pd
import os

# Configure Dash to recognize the URL of the container
user = os.environ.get("DOMINO_PROJECT_OWNER")
project = os.environ.get("DOMINO_PROJECT_NAME")
runid = os.environ.get("DOMINO_RUN_ID")
jupyter = os.environ.get("JUPYTER_SERVER_ROOT")

# If this variable exists, we're running a Workspace
if jupyter == '/':
    debug=False
    port=8889
    runurl = '/' + user + '/' + project + '/notebookSession/' + runid + '/proxy/8889/'
else:
    debug=True
    port=8888
    runurl = '/' + user + '/' + project + '/r/notebookSession/' + runid + '/'

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = Dash(__name__, routes_pathname_prefix='/', requests_pathname_prefix=runurl)
app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
if __name__ == '__main__':
    print(f'app is running at https://sup5101ab.support-team-sandbox.domino.tech{runurl}')
    app.run_server(port=port, host='0.0.0.0', debug=debug)