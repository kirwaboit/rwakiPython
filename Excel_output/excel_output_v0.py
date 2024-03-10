import pandas as pd
import numpy as np

# Create a DataFrame with 3 rows and 3 columns filled with random data
df = pd.DataFrame(np.random.rand(3, 3), columns=['Column1', 'Column2', 'Column3'])

print(df)

# Assuming df is your DataFrame
#df.to_excel("output.xlsx", index=False)
df.to_excel(r"Finances/fileTester_v0.xlsx", index = False)
