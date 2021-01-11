import csv
import numpy as np
import plotly.express as ps

def getDataSource(data_path):
    icecream_sales = []
    colddrink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            icecream_sales.append(float(row['Temperature']))
            colddrink_sales.append(float(row['Ice-cream Sales( ₹ )']))

    return {'x': icecream_sales, 'y': colddrink_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('correlation between temperature an ice cream sales:- ', correlation[0,1])

def setup():
    data_path = 'data.csv'
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()