import pandas as pd


data = {'Names':['Ballroom1', 'Ballroom2', 'ballroom3'], 'Capacity':[25000,11000,5000]}
df = pd.DataFrame(data, columns=['Names', 'Capacity'])
print(df)