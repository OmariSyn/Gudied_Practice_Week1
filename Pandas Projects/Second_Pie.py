import pandas as pd
import matplotlib.pyplot as plt

print("omarijoh0314")


data = {"People":[18000,13000,10000]}
df = pd.DataFrame(data, index=["Children","Adults","Teens"])
df.plot.pie(y="People")
plt.show()