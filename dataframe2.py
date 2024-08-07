import numpy
import numpy as np
import pandas as pd

my_index = ['A', 'B', 'C']
my_columns = ['이름', '나이', '성별']
my_data = numpy.array([['Alice', 'Bob', '홍길동'],
                       [25, 30, 26],
                       ['여', '남', '남']]).transpose()
print(my_data)
df = pd.DataFrame(my_data, index=my_index, columns=my_columns)
#print(df[['이름','나이']], df.shape) # df.shape은 몇 행, 몇 열인지 알려준다

print(df, "\n", df.loc["A"])7