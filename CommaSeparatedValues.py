#Como crear dataframes con CSV files
import pandas as pd
pdnew_dogs = pd.read_csv("new_dogs.csv") # .to_csv para pasar de un dataframe a un csv file 
print(pdnew_dogs)
