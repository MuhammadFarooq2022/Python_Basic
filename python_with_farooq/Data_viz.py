#steps involved in data visualization
# Step-1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Step-2 set a theme
sns.set_them(style="ticks", color_codes=True)

# Step-3 import data set you can also import your own data
kashti = sns.load_dataset("titanic")
print(kashti)

# # Step-4 plot basic graph
# p = sns.countplot(x= " ", y= " ", data=kashti)
# plt.show()        