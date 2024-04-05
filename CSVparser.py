import pandas as pd
import os


class CSVparser:

    def __init__(self):
        '''
        simple parser reading the CSV file 'cereal.csv'.
        A pandas dataframe is initiated, a superfluous row and column deleted
        and a column is renamed to avoid ambiguity.
        
        The 'rating' column doesn't seem to be part of the original dataset,
        but rather some parameter added in a student project at Télécom Paris,
        thus it is discarded.
        
        A new column is added, mapping a image name from the folder Cereal Pictures
        to each corresponding row.
        '''
        #try:
        self.df = pd.read_csv('cereal.csv', sep=';', engine = 'python')
        self.df = self.df.drop(0)
        self.df = self.df.drop('rating', axis=1)
        self.df['img'] = ''
        for i in range(len(self.df)):
            self.df.loc[i+1,('calories')] = float(self.df.iloc[i].calories)
            self.df.loc[i+1,('protein')] = float(self.df.iloc[i].protein)
            self.df.loc[i+1,('fat')] = float(self.df.iloc[i].fat)
            self.df.loc[i+1,('sodium')] = float(self.df.iloc[i].sodium)
            self.df.loc[i+1,('fiber')] = float(self.df.iloc[i].fiber)
            self.df.loc[i+1,('carbo')] = float(self.df.iloc[i].carbo)
            self.df.loc[i+1,('sugars')] = float(self.df.iloc[i].sugars)
            self.df.loc[i+1,('potass')] = float(self.df.iloc[i].potass)
            self.df.loc[i+1,('vitamins')] = float(self.df.iloc[i].vitamins)
            self.df.loc[i+1,('shelf')] = float(self.df.iloc[i].shelf)
            self.df.loc[i+1,('weight')] = float(self.df.iloc[i].weight)
            self.df.loc[i+1,('cups')] = float(self.df.iloc[i].cups)


        self.df.rename(columns = {'name':'Name'}, inplace = True)
        for img in os.listdir('Cereal Pictures'):
            for i in range(len(self.df)): 
                if img.lower().replace(" ", "")[:-4] == self.df.iloc[i].Name.lower().replace(" ", "").replace("  ", "").replace(".", ","):
                    self.df.loc[i+1,('img')] = img
                if img.lower().replace(" ", "")[:-6] == self.df.iloc[i].Name.lower().replace(" ", "").replace("  ", "").replace(".", ",")[:-3]:
                    self.df.loc[i+1,('img')] = img  
       # except:
          #  print('The file cereal.csv was not found, make sure it is in your working directory')

# df = CSVparser().df

# print(df.head())
