import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

# 1. Prepare data
labels = ['Web', 'ios', 'android','react native']
values = [40, 20, 25, 15]
colors = ['red', 'green', 'gold', 'purple']
explode = [0, 0.2, 0, 0]
#2. Plot
pyplot.pie(values,
labels=labels,
colors=colors,
explode=explode,
shadow=True)
pyplot.axis('equal')
#3. Show
pyplot.show()
