from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout, Bar,Margin

import pandas as pd

df = pd.read_csv('data/recipeData.csv', index_col='BeerID', encoding='latin-1')
print(df.head())
print(df.info(verbose=False))
data = [
    Bar(
        x=df['Name'], # assign x as the dataframe column 'x'
        y=df['OG']
    )
]
#url = plot(data, filename='graph/plot.html')

top_n_types = 15
recipe_popularity_as_perc = 100 * df['Style'].value_counts()[:top_n_types] / len(df)

data = [
    Bar(
        x=recipe_popularity_as_perc.index,
        y=recipe_popularity_as_perc.values
    )
]

layout = Layout(
    title='Most popular beer styles',
    xaxis={'title': 'Style'},
    yaxis={'title': 'Proportion of recipes (%)'},
    margin=Margin(l=50, r=50, b=150, t=50, pad=4)
)

fig = Figure(data=data, layout=layout)
plot(fig, filename='graph/popular.html')