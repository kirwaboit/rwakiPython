import dash
import dash_table
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df1 = pd.read_excel(r"C:\Users\Burudani\Documents\Finance_Trending\Checking_Jan1st2021_March10th2021.xlsx")  




#TODO Create a list of short descriptive words to help in aggregating the 
newDescriptionColumn = ['
#TODO Create df2  with new aggregate column

#Aggregating similar bank values
#aggregation_functions = {'Date': 'last', 'Amount': 'sum', 'CheckNumber': 'first', 'Description': 'last'}
#df1_new = df1.groupby(df1['Description']).aggregate(aggregation_functions)

print(df1.shape)

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