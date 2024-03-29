import pandas as pd
import numpy as np
# Pass a 2D numpy array - each row is the corresponding row required in the dataframe
print(np.version)
data = np.array([[1,"toyota","corolla","TOYOTA","corolla"],
                 [2,"honda","civic","lamborghini","sinata"],
                 [1,"hyndai","accent car","hyndai","accent car"],
                 [1,"nissan","sentra","maserati","dishenco"],
                 [2,"honda","Odessey","porshe","cayane"],
                 [1,"Tesla","model","model","Tesla"]])   # testing reversal of data

#TODO try using contains and test for backward macthes

# pass column names in the columns parameter
df = pd.DataFrame(data, columns = ['year', 'make1','model1','make2','model2'])

print(df)

print('\n')


def errorDetector(row):
    if ((row.year == '2') or  # CHeck if the year is equal to 2
            (row.make1.upper() == row.make2.upper() and row.model1.upper() == row.model2.upper()) or (
                    row.make1.upper() == row.model2.upper() and row.model1.upper() == row.make2.upper())):  # check if columns match in reverse
        return "Match"

    else:
        return "No Match"




# if (row.year == '2' | (row.make1.str.upper() == row.make2.str.upper() & row.model1.isin(row.model2)))

# (row.make1.upper() == row.model2.upper() and row.model1.upper() == row.make2.upper())

df.loc[:, 'Match Tester'] = df.apply(errorDetector, axis=1)
# df['Discounted_Price'] = df.apply(fun)
print(df)