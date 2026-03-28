import pandas as pd
import matplotlib.pyplot as plt

print('omarijoh0314')



classroom = [[ "Alice", "Bob", "Charlie", "Diana", "Ethan",
    "Fiona", "George", "Hannah", "Ian", "Jenna"], ['Math', 'Science', 'Math', 'Science',
'Math', 'Science', 'Math', "Science", 'Math', 'Science']]

index = pd.MultiIndex.from_arrays(classroom, names=('Classroom', 'Subject'))

df = pd.DataFrame({"Grade":[85, 90, 78, 92, 88, 76, 95, 89, 100, 82]}, index=index)

Class_Asign = df.groupby(by=['Subject']).mean()

Class_Asign['Grade'].plot(kind='bar')

plt.xlabel("Average Grade by Subject")
plt.xticks(rotation=0)
plt.title("School Subjectes Percentage")
plt.show()