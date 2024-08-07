# import pandas as pd
# import matplotlib.pyplot as plt
#
# col_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
#                    names=col_names)
# plt.clf()
# plt.hist(data['class'])
# plt.show()
# plt.savefig("./age.png")



import pandas as pd
import matplotlib.pyplot as plt

col_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names=col_names)
data.describe().to_csv('./results/describe.csv')
