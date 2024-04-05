import pandas as pd
from CSVparser import CSVparser
from PIL import Image
import matplotlib.pyplot as plt

# df = CSVparser().df
# print(df.head())
# print(df.iloc[27])
# help(CSVparser())

class DataFrame:
    
    def __init__(self):
        
        try:
            self.df = CSVparser().df
        except:
            print('Error loading data! Check that all necessary files are in the working directory!')
        
        
        

    
    
    def delete(self, _index):
        """ Takes the index of a row and deletes the row """
        try:
            self.df = self.df.drop(_index)
        except:
            print('Error deleting row! Passed index may be out of bounds.')

    def edit(self, _key, _index, *_val):
        """" Sets the value of a cell in the dataframe, takes column name, index and the new value """
        try:
            print('hello')
            self.df.loc[_index,(_key)] = _val
            print(self.df.loc[_index,(_key)])
        except:
            print('Error setting new value for cell! Check that both index and column name are correct!')
    def _add(self, _name, _vals):
        """ 
        Creates a new row in the Dataframe.
        Takes a string of the name and a list of values of length 14.
        The types of the individual list elements should be:
        [str, str, float, float, float, float, float, float, float, float, float, float, float, float]
        (2 strings followed by 12 floats)
        
        the image path is set to None
        """
        try:
            tempdict = pd.DataFrame({'Name':_name, 'mfr':_vals[0],'type':_vals[1],'calories':_vals[2],'protein':_vals[3],'fat':_vals[4],'sodium':_vals[5],'fiber':_vals[6],'carbo':_vals[7],'sugars':_vals[8],'potass':_vals[9],'vitamins':_vals[10],'shelf':_vals[11],'weight':_vals[12],'cups':_vals[13],'img':None}, index=[0])
            self.df = pd.concat([self.df, tempdict], ignore_index = True)
        except:
            print('Error creating new row in Dataframe! Most likely culprit is wrong input for values, input should be a list of length 14, 2 i char strings followed by 12 floats.')

    def search(self, query):
        """
        Search functions that finds all matches from the query in the names and manufacturers 
        (mapping the mfr column to string of manufacturer) of all cereals in the Dataframe.
        Eliminates duplicate results to avoid cluttered output.
        
        Query should be a string.
        """
        mfrKey = {'A' :' American Home Food Products',
                  'G' :'General Mills',
                  'K' : 'Kelloggs',
                  'N' : 'Nabisco',
                  'P' : 'Post',
                  'Q' : 'Quaker Oats',
                  'R' : 'Ralston Purina' }
        resultList = []
        nameList = []
        if type(query) == str:
            
            for i in range(len(self.df)):
                
                    
                if query.lower() in self.df.iloc[i].Name.lower() and self.df.iloc[i].Name not in nameList:
                    resultList.append(self.df.iloc[i])
                    nameList.append(self.df.iloc[i].Name)
                if self.df.iloc[i].mfr in mfrKey.keys():
                    if query.lower() in mfrKey[self.df.iloc[i].mfr].lower() and self.df.iloc[i].Name not in nameList:
                        resultList.append(self.df.iloc[i])
                        nameList.append(self.df.iloc[i].Name)
                elif self.df.iloc[i].mfr not in mfrKey.keys():
                    if query.lower() in self.df.iloc[i].mfr.lower() and self.df.iloc[i].Name not in nameList:
                        resultList.append(self.df.iloc[i])
                        nameList.append(self.df.iloc[i].Name)
                    
            if len(resultList) == 0:
                print('No search results! Try adjusting your search query')
        else:
            print('Error! Type of query should be string!')
        return resultList, nameList
        

    def searchGreaterThan(self, _column, query):
        resultList = []
        nameList = []
        if type(query) == float or type(query) == int:
            for i in range(len(self.df)):
                if query <= self.df.loc[i+1,(_column)]:
                    resultList.append(self.df.iloc[i])
                    nameList.append(self.df.iloc[i].Name)
        else:
            print('The value queried should be either a float or integer.')
        return resultList, nameList
    
    def searchLessThan(self, _column, query):
        resultList = []
        nameList = []
        if type(query) == float or type(query) == int:
            for i in range(len(self.df)):
                if query >= self.df.loc[i+1,(_column)]:
                    resultList.append(self.df.iloc[i])
                    nameList.append(self.df.iloc[i].Name)
        else:
            print('The value queried should be either a float or integer.')
        return resultList, nameList

    def showImage(self,_index):
        """ Takes an index and opens the assosciated image """
        try:
            im = Image.open('Cereal Pictures/'+'str(self.df.iloc[_index].img))
            im.show()
        except:
            print('Error displaying image of cereal! Either provided index is wrong or requested row doesn´t have an image file assosciated with it.')
        
        

    def visualiseData(self,_column, _column2 = None):
        """ 
        Takes a data column and plots the cereals against each other.
        
        Can also take 2 columns as arguments and plot a scatterplot of the datapairs in the columns.
        """
        if _column2 == None:
            try:
                data = list(self.df[_column])
                cereals = list(self.df.index)
                #print(data,cereals)
                plt.figure()
                plt.plot(cereals,data,'.')
                plt.ylabel(_column[0].upper()+_column[1:])
                plt.xlabel('Cereal index')
                plt.show()
            except:
                print('Error plotting data! Either passed column is wrong or a none float value has been passed to one or more cells in the column.')
        else:  
            try:
                data = list(self.df[_column])
                data2 = list(self.df[_column2]) 
                cereals = list(self.df.index)
                #print(data,data2)
                plt.figure()
                plt.plot(data,data2,'.')
                plt.ylabel(_column2[0].upper()+_column2[1:])
                plt.xlabel(_column[0].upper()+_column[1:])
                plt.show()
            except:
                print('Error plotting data! Either passed column is wrong or a none float value has been passed to one or more cells in the column.')
       
    def plotSearch(self, _search, column1, column2 = None):
        """
        Takes a list of search result and 1-2 column names and plots the results
        """
        indexList = []
        data1 = []
        data2 = []
        
        if column2 == None:
            try:
                for i in range(len(_search)):
                    data1.append(self.df.loc[_search[i].name,(column1)])
                    indexList.append(_search[i].name)
                plt.figure()
                plt.plot(indexList,data1,'.')
                plt.ylabel(column1[0].upper()+column1[1:])
                plt.xlabel('Cereal index')   
                plt.show()
            except:
                print('Error plotting search results! Make sure you passed a list of search results (Note that the builtin search functions return more than one list, so you will need to pass something like ´search[0]) and that the passed column(s) are correct.´')
            
        else:
            try:
                for i in range(len(_search)):
                    data1.append(self.df.loc[_search[i].name,(column1)])
                    data2.append(self.df.loc[_search[i].name,(column2)])
                plt.figure()
                plt.plot(data1,data2,'.')
                plt.ylabel(column2[0].upper()+column2[1:])
                plt.xlabel(column1[0].upper()+column1[1:])
                plt.show()
            except:
                print('Error plotting search results! Make sure you passed a list of search results (Note that the builtin search functions return more than one list, so you will need to pass something like ´search[0]) and that the passed column(s) are correct.´')
            
 
    
############################################################################### 
################################ TESTING ######################################
###############################################################################
 

test = DataFrame()
# test._add('Cornflakes', ['K','C',1,1,1,1,1,1,1,1,1,1,1,1])
test._add('Havregryn', ['O','C',4,1,1,8,2,1,1,4,1,0,1111,1])
#print(list(test.df['Name']))
# test.showImage(27)
#test.visualiseData('cups','calories')
#print(test.search('xxx'))
s = test.search('kelloggs')[0]
test.plotSearch(s, 'sugars',)
#print(test.searchLessThan('calories', 60))

