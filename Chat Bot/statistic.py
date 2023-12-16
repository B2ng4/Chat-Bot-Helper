# -*- coding: utf-8 -*-
import psycopg2
from collections import Counter
from config import host, user, db_pass, db_name, port
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
from collections import Counter
import pandas as pd
# Подключение к базе данны
connection = psycopg2.connect(dbname="History", user='root', password=db_pass, host=host, port=port)
connection.autocommit = True
cursor = connection.cursor()

# Запрос данных
cursor.execute(f'''SELECT theme FROM History WHERE username='ТимофейСидорин' ''')
all_history = cursor.fetchall()
tuples = all_history
counter = Counter(t.strip() for t, in tuples if t.strip())

# Обработка данных
data_dict = {item: count for item, count in counter.items()}

df = pd.DataFrame(list(data_dict.items()), columns=['Категория', 'Значение'])


app = dash.Dash(__name__)

fig = px.histogram(df, x="Значение", y="Категория", orientation="h")
app.layout = html.Div(children=[
   html.H1(children='Статистика'),  # Create a title with H1 tag

   dcc.Graph(
       id='example-graph',
       figure=fig
   )  # Display the Plotly figure
])

if __name__ == '__main__':
   app.run_server(debug=True) # Run the Dash app