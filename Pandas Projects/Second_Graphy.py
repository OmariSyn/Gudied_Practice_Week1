import matplotlib.pyplot as plt
import pandas as pd

print('omarijoh0314')

data = {'Names':['Ballroom1', 'Ballroom2', 'ballroom3'], 'Capacity':[25000,11000,5000]}
df = pd.DataFrame(data, columns=['Names', 'Capacity'])



df.plot(x="Names", y='Capacity', kind='bar')

plt.show()