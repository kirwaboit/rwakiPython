import pandas as pd
import matplotlib

df1 = pd.read_excel(r"C:\Users\Burudani\Documents\Finance_Trending\Checking_Jan1st2021_March10th2021.xlsx",
 header=None)  
df1.columns = ['Date','Amount','Xs','CheckNumber','Description']
