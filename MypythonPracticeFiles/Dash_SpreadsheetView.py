import dash
import dash_table
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df1 = pd.read_excel(r"C:\Users\Burudani\Documents\Finance_Trending\Checking_Jan1st2021_March10th2021.xlsx",
 header=None)  


df1.columns = ['Date','Amount','Xs','CheckNumber','Description']

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df1.columns],
    data=df1.to_dict('records'),
    filter_action="native", # Allows to
    sort_action="native" , # Allows us to sort the columns from highest to lowest value
    style_cell={
        'textAlign': 'left',
        #'backgroundColor':'rgb(50, 50, 50)',
        #'color': 'white'
        },
    style_header={
        #'backgroundColor': 'rgb(30, 30, 30)',
        'fontWeight': 'bold',
        'textAlign': 'center'
    },
    #editable=True,
    
)

if __name__ == '__main__':
    app.run_server(debug=True)


# Dash Colour