import pandas as pd
from CSVparser import CSVparser
from DataFrame import DataFrame
from PIL import Image
import matplotlib.pyplot as plt
import os




class KonsolUI:
    
    
    
    def __init__(self):
        
        self.DataFrame = DataFrame()
        self.columns = [
                        'calories',
                        'protein',
                        'fat',
                        'sodium',
                        'fiber',
                        'carbo',
                        'sugars',
                        'potass',
                        'vitamins',
                        'shelf',
                        'weight',
                        'cups'
                            ]
        
        self.startScreen()
        pass
    def startScreen(self):
        print('########## CEREAL DATA ########## \n')
        print('OPTIONS:\n')
        print('SEARCH     : s')
        print('VIEW IMAGES: v')
        print('PLOT DATA  : p')
        print('EDIT DATA  : e')
        print('INFO       : i')
        print('EXIT       : x')
        
        startChoice = input()
        
        if startChoice == 's':
            self.searchMenu()
        elif startChoice == 'v':
            self.imageMenu()
        elif startChoice == 'p':
            self.plotMenu()
        elif startChoice == 'e':
            self.editDataMenu()
        elif startChoice == 'i':
            self.dataInfo()
        elif startChoice == 'x'    :
            pass
        
        else:
            print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE OPTIONS.\n####\n')
            self.startScreen()
        
        #print('\n#################################')
    
    def dataInfo(self):
        
        print('\n\nThis is a dataset over nutritional info of various cereals')
        print('The Dataframe is structured with 15 columns and 77 rows, \neach row a different cereal.\n')
        print('COLUMNS - - - - - - - - - - UNITS - - - - - - - NOTES ')
        print('- - - - - - - - - - - - - - - - - - - - -')
        print('\nNAME  - - - - - - - - - - -  N/A')
        print('\nMANUFACTURER- - - - - - - -1 CHAR key')
        print('\nHOT/COLD  - - - - - - - - -1 CHAR key - - - - served hot or cold?')
        print('\nCALORIES  - - - - - - - - - -kCAL')
        print('\nPROTEIN  - - - - - - - - - - - g')
        print('\nFAT  - - - - - - - - - - - - - g')
        print('\nSODIUM - - - - - - - - - - -  mg')
        print('\nFIBER  - - - - - - - - - - -   g')
        print('\nCARBOHYDRATES  - - - - - - - - g')
        print('\nSUGARS  - - - - - - - - - - -  g')
        print('\nPOTASSIUM - - - - - - - - - - mg')
        print('\nVITAMINS  - - - - - - - - % of FDA rec')
        print('\nSHELF  - - - - - - - - - -  1./2./3. - - - - display shelf from the floor')
        print('\nWEIGHT OF SERVING  - - - - - ounces')
        print('\nCUPS/SERVING  - - - - - - - - cups')
        
        print('\n')
        print('\nPRESS ENTER TO GO TO START MENU')
        idle = input()
        self.startScreen()
 
    
    def searchMenu(self):
        print('########## CEREAL DATA ########## \n')
        print('SEARCH OPTIONS:\n')
        print('SEARCH BY NAME & MANUFACTURER       : 1')
        print('SEARCH BY VALUE (GREATER OR EQUALS) : 2')
        print('SEARCH BY VALUE (LESS OR EQUALS)    : 3')
        
        searchChoice = input()
        
        if searchChoice == '1':
            self.searchNameManu()
        elif searchChoice == '2':
            self.searchValGE()
        elif searchChoice == '3':
            self.searchValLE()
        else:
            print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE OPTIONS.\n####\n')
            self.searchMenu()
    
    def searchNameManu(self):
        print('########## CEREAL DATA ########## \n')
        print('SEARCH BY NAME & MANUFACTURER:\n')
        print('PLEASE WRITE YOUR SEARCH QUERY:')
        
        sNMquery = input('QUERY: ') 
        sNMresults = self.DataFrame.search(sNMquery)[0]
        if len(sNMresults) == 0:
            print('NO SEARCH RESULTS')
            self.searchMenu()
        else:
            print('\nRESULTS:\n')
            for i in range(len(sNMresults)):
                print(str(i+1)+': '+sNMresults[i].Name)
            print('\nFOR DETAILS ON SPECIFIC CEREAL, PRESS LISTED INDEX\nOR PRESS 0 TO GO TO START')
            resultChoice = input()
            try:
                resultChoiceINT = int(resultChoice)
                if resultChoiceINT == 0:
                    self.startScreen()
                else:
                    print('DETAILS:')
                    print(sNMresults[resultChoiceINT-1])
                    print('\nPRESS ENTER TO GO TO START MENU')
                    idle = input()
                    self.startScreen()
                
            except:
                print('\nINVALID INPUT\n')
                print('PRESS ENTER TO GO TO START MENU')
                idle = input()
                self.startScreen()
    def searchValGE(self):
        print('########## CEREAL DATA ########## \n')
        print('SEARCH BY VALUE (GREATER OR EQUALS):\n')
        print('PLEASE WRITE FIRST THE COLUMN TO SEARCH\nFOLLOWED BY THE DESIRED THRESHOLD VALUE')
        self.printColumns()
        
        sVGEcolumn = input('COLUMN: ')
        if sVGEcolumn.lower() in self.columns:
            sVGEval =    input('VALUE:  ')
            sVGEresults = self.DataFrame.searchGreaterThan(sVGEcolumn, float(sVGEval))[0]
            if len(sVGEresults) == 0:
                print('NO SEARCH RESULTS')
                self.searchValGE()
            else:
                print('\nRESULTS:\n')
                for i in range(len(sVGEresults)):
                    print(str(i+1)+': '+sVGEresults[i].Name)
                print('\nFOR DETAILS ON SPECIFIC CEREAL, PRESS LISTED INDEX\nOR PRESS 0 TO GO TO START')
                resultChoice = input()
                try:
                    resultChoiceINT = int(resultChoice)
                    if resultChoiceINT == 0:
                        self.startScreen()
                    else:
                        print('DETAILS:')
                        print(sVGEresults[resultChoiceINT-1])
                        print('\nPRESS ENTER TO GO TO START MENU')
                        idle = input()
                        self.startScreen()
                    
                except:
                    print('\nINVALID INPUT\n')
                    print('PRESS ENTER TO GO TO START MENU')
                    idle = input()
                    self.startScreen()
        else:
            print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE COLUMNS.\n####\n')
            self.searchValGE()
            
        
        
    def searchValLE(self):
        print('########## CEREAL DATA ########## \n')
        print('SEARCH BY VALUE (LESS OR EQUALS):\n')
        print('PLEASE WRITE FIRST THE COLUMN TO SEARCH\nFOLLOWED BY THE DESIRED THRESHOLD VALUE')
        self.printColumns()
        
        sVLEcolumn = input('COLUMN: ')
        if sVLEcolumn.lower() in self.columns:
            sVLEval =    input('VALUE:  ')
            sVLEresults = self.DataFrame.searchGreaterThan(sVLEcolumn, float(sVLEval))[0]
            if len(sVLEresults) == 0:
                print('NO SEARCH RESULTS')
                self.searchValLE()
            else:
                print('\nRESULTS:\n')
                for i in range(len(sVLEresults)):
                    print(str(i+1)+': '+sVLEresults[i].Name)
                print('\nFOR DETAILS ON SPECIFIC CEREAL, PRESS LISTED INDEX\nOR PRESS 0 TO GO TO START')
                resultChoice = input()
                try:
                    resultChoiceINT = int(resultChoice)
                    if resultChoiceINT == 0:
                        self.startScreen()
                    else:
                        print('DETAILS:')
                        print(sVLEresults[resultChoiceINT-1])
                        print('\nPRESS ENTER TO GO TO START MENU')
                        idle = input()
                        self.startScreen()
                    
                except:
                    print('\nINVALID INPUT\n')
                    print('PRESS ENTER TO GO TO START MENU')
                    idle = input()
                    self.startScreen()
        else:
            print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE COLUMNS.\n####\n')
            self.searchValGE()
    
    def imageMenu(self):
        print('########## CEREAL DATA ########## \n')
        print('IMAGE OPTIONS:\n')
        print('CHOOSE BY INDEX                    : 1')
        print('CHOOSE BY NAME SEARCH (FIRST MATCH): 2')
        
        imChoice = input()
        
        
        if imChoice == '1':
            print('PLEASE WRITE INDEX OF DESIRED CEREAL')
            
            imIndex = input('INDEX: ')
            try:
                self.DataFrame.showImage(int(imIndex))
                
                print('PRESS ENTER TO GO TO START MENU')
                idle = input()
                self.startScreen()
            except:
                print('\n####\nINDEX MUST BE AN INTEGER\n####\n')
                self.imageMenu()
        elif imChoice == '2':
            print('PLEASE WRITE NAME OF DESIRED CEREAL')
            
            imName = input()
            try:
                self.DataFrame.showImage(self.DataFrame.search(imName[0][0].name))
                
                print('PRESS ENTER TO GO TO START MENU')
                idle = input()
                self.startScreen()
            except:
                print('\n####\nBAD INPUT\n####\n')
                self.imageMenu()
                
        else:
            print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE OPTIONS.\n####\n')
            self.imageMenu()
        pass
    
    def plotMenu(self):
        print('########## CEREAL DATA ########## \n')
        print('PLOTTING OPTIONS:\n')
        print('PLOT HISTOGRAM OF SINGLE COLUMN             : 1')
        print('PLOT SCATTER PLOT OF TWO COLUMNS            : 2')
        print('PLOT HISTOGRAM OF SINGLE COLUMN FROM SEARCH : 3')
        print('PLOT SCATTER PLOT OF TWO COLUMNS FROM SEARCH: 4')
        
        
        plotChoice = input()
        
        if plotChoice == '1':
            print('PLEASE CHOOSE COLUMN TO PRINT HISTOGRAM OF')
            self.printColumns()
            
            pHcolumn = input('COLUMN: ')
            
            if pHcolumn.lower() in self.columns:
                self.DataFrame.visualiseData(pHcolumn.lower())
                
                print('PRESS ENTER TO GO TO START MENU')
                idle = input()
                self.startScreen()
            else:
                print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE COLUMNS.\n####\n')
                self.plotMenu()
            
            
        elif plotChoice == '2':
            print('PLEASE CHOOSE 2 COLUMNS (SEPERATELY, 2 INPUTS) TO MAKE SCATTERPLOT OF')
            self.printColumns()
            
            pScolumn1 = input('FIRST COLUMN:')
            pScolumn2 = input('SECOND COLUMN:')
            
            if pScolumn1.lower() in self.columns and pScolumn2.lower() in self.columns:
                self.DataFrame.visualiseData(pScolumn1.lower(),pScolumn2.lower())
                
                print('PRESS ENTER TO GO TO START MENU')
                idle = input()
                self.startScreen()
                
            else:
                print('\n####\nBAD INPUT, PLEASE CHOOSE TWO OF THE COLUMNS.\n####\n')
                self.plotMenu()
            
        elif plotChoice == '3':
            print('\nSEARCH BY\n:')
            print('NAME & MANUFACTURER     : 1')
            print('VALUE (GREATER OR EQUALS: 2')
            print('VALUE (LESS OR EQUALS   : 3')
            
            pHbsChoice = input()
            
            if pHbsChoice == '1':
                print('PLEASE WRITE YOUR SEARCH QUERY:')
                psHquery = input('QUERY: ')
                print('PLEASE CHOOSE COLUMN TO PRINT HISTOGRAM OF')
                self.printColumns()
                
                psHcolumn = input()
                if psHcolumn.lower() in self.columns:
                    psHsearch = self.DataFrame.search(psHquery)[0]
                    if len(psHsearch) == 0:
                        print('NO RESULTS FOR CHOSEN QUERY')
                        self.plotMenu()
                    else:
                        self.DataFrame.plotSearch(psHsearch, psHcolumn)
                        
                        print('PRESS ENTER TO GO TO START MENU')
                        idle = input()
                        self.startScreen()
                    
                else:
                    print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE COLUMNS.\n####\n')
                    self.plotMenu()
                
            elif pHbsChoice == '2':
                psHqcol, psHval = self.plotsearchValGE()
                print('PLEASE CHOOSE COLUMN TO PRINT HISTOGRAM OF')
                self.printColumns()
                
                psHcolumn = input('COLUMN: ')
                if psHcolumn.lower() in self.columns:
                    psHsearch = self.DataFrame.searchGreaterThan(psHqcol, float(psHval))[0]
                    
                    if len(psHsearch) == 0:
                        print('NO RESULTS FOR CHOSEN QUERY')
                        self.plotMenu()
                    else:
                        self.DataFrame.plotSearch(psHsearch, psHcolumn)
                        
                        print('PRESS ENTER TO GO TO START MENU')
                        idle = input()
                        self.startScreen()
                else:
                    print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE COLUMNS.\n####\n')
                    self.plotMenu()
            elif pHbsChoice == '3':
                psHqcol, psHval = self.plotsearchValLE()
                print('PLEASE CHOOSE COLUMN TO PRINT HISTOGRAM OF')
                self.printColumns()
                
                psHcolumn = input('COLUMN: ')
                if psHcolumn.lower() in self.columns:
                    psHsearch = self.DataFrame.searchLessThan(psHqcol, float(psHval))[0]
                    if len(psHsearch) == 0:
                        print('NO RESULTS FOR CHOSEN QUERY')
                        self.plotMenu()
                    else:
                        self.DataFrame.plotSearch(psHsearch, psHcolumn)
                        
                        print('PRESS ENTER TO GO TO START MENU')
                        idle = input()
                        self.startScreen()
            else:
                print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE OPTIONS.\n####\n')
                self.plotMenu()
            
        elif plotChoice == '4':
            print('\nSEARCH BY\n')
            print('NAME & MANUFACTURER     : 1')
            print('VALUE (GREATER OR EQUALS: 2')
            print('VALUE (LESS OR EQUALS   : 3')
            
            pSbsChoice = input()
            
            if pSbsChoice == '1':
                print('PLEASE WRITE YOUR SEARCH QUERY:')
                psSquery = input('QUERY: ')
                print('PLEASE CHOOSE 2 COLUMNS (SEPERATELY, 2 INPUTS) TO MAKE SCATTERPLOT OF')
                self.printColumns()
                
                psScolumn1 = input('COLUMN 1:')
                psScolumn2 = input('COLUMN 2:')
                if psScolumn1.lower() in self.columns and psScolumn2.lower() in self.columns:
                    psSsearch = self.DataFrame.search(psSquery)[0]
                    if len(psSsearch) == 0:
                        print('NO RESULTS FOR CHOSEN QUERY')
                        self.plotMenu()
                    else:
                        self.DataFrame.plotSearch(psSsearch, psScolumn1, psScolumn2)
                        
                        print('PRESS ENTER TO GO TO START MENU')
                        idle = input()
                        self.startScreen()
                else:
                    print('\n####\nBAD INPUT, PLEASE CHOOSE TWO OF THE COLUMNS.\n####\n')
                    self.plotMenu()
                
            elif pSbsChoice == '2':
                psSqcol, psSval = self.plotsearchValGE()
                print('PLEASE CHOOSE 2 COLUMNS (SEPERATELY, 2 INPUTS) TO MAKE SCATTERPLOT OF')
                self.printColumns()
                
                psScolumn1 = input('COLUMN 1: ')
                psScolumn2 = input('COLUMN 2: ')
                if psScolumn1.lower() in self.columns and psScolumn2.lower() in self.columns:
                    psSsearch = self.DataFrame.searchGreaterThan(psSqcol, float(psSval))[0]
                    if len(psSsearch) == 0:
                        print('NO RESULTS FOR CHOSEN QUERY')
                        self.plotMenu()
                    else:
                        self.DataFrame.plotSearch(psSsearch, psScolumn1, psScolumn2)
                        
                        print('PRESS ENTER TO GO TO START MENU')
                        idle = input()
                        self.startScreen()
                else:
                    print('\n####\nBAD INPUT, PLEASE CHOOSE TWO OF THE COLUMNS.\n####\n')
                    self.plotMenu()
                    
            elif pSbsChoice == '3':
                psSqcol, psSval = self.plotsearchValLE()
                print('PLEASE CHOOSE 2 COLUMNS (SEPERATELY, 2 INPUTS) TO MAKE SCATTERPLOT OF')
                self.printColumns()
                
                psScolumn1 = input()
                psScolumn2 = input()
                if psScolumn1.lower() in self.columns and psScolumn2.lower() in self.columns: 
                    psSsearch = self.DataFrame.searchLessThan(psSqcol, float(psSval))[0]
                    if len(psSsearch) == 0:
                        print('NO RESULTS FOR CHOSEN QUERY')
                        self.plotMenu()
                    else:
                        self.DataFrame.plotSearch(psSsearch, psScolumn1, psScolumn2)
                          
                        print('PRESS ENTER TO GO TO START MENU')
                        idle = input()
                        self.startScreen()
                else:
                    print('\n####\nBAD INPUT, PLEASE CHOOSE TWO OF THE COLUMNS.\n####\n')
                    self.plotMenu()
            else:
                print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE OPTIONS.\n####\n')
                self.plotMenu()
        else:
            print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE OPTIONS.\n####\n')
            self.plotMenu()
        
        pass
    
    def plotsearchValGE(self):

        print('PLEASE WRITE FIRST THE COLUMN TO SEARCH\nFOLLOWED BY THE DESIRED THRESHOLD VALUE')
        self.printColumns()
        
        psVGEcolumn = input()
        psVGEval = input()
        return psVGEcolumn, psVGEval
        
    def plotsearchValLE(self):

        print('PLEASE WRITE FIRST THE COLUMN TO SEARCH\nFOLLOWED BY THE DESIRED THRESHOLD VALUE')
        self.printColumns()
        
        psVLEcolumn = input()
        psVLEval = input()
        return psVLEcolumn, psVLEval
        
    def plotsearchNameManu(self):

        print('PLEASE WRITE YOUR SEARCH QUERY:')
        
        psNMquery = input() 
        return psNMquery
    
    def editDataMenu(self):
        print('########## CEREAL DATA ########## \n')
        print('DATA EDITING OPTIONS:\n')
        print('ADD ROW    : 1')
        print('DELETE ROW : 2')
        # print('EDIT ROW   : 3')
        
        eDMChoice = input()
        
        if eDMChoice == '2':
            self.deleteRow()
        elif eDMChoice == '1':
            self.addRow()
        # elif eDMChoice == '3':
        #     self.editRow()
        else:
            print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE OPTIONS.\n####\n')
            self.editDataMenu()
        
    def deleteRow(self):
        print('WARNING! YOU´RE ATTEMPTING TO DELETE DATA')
        print('CHOOSE ROW BY NAME OR INDEX?\n')
        print('NAME (1st SEARCH RESULT): 1')
        print('INDEX                   : 2\n')
        print('GO TO START MENU        : 0')
        delChoice = input()
        if delChoice == '1':
            print('\n')
            delName = input('NAME: ')
            delSearch = self.DataFrame.search(delName)[0]
            if len(delSearch) == 0:
                print('NO SEARCH RESULTS')
                self.deleteRow()
            else:
                print('\nDETAILS:')
                print(delSearch[0])
                print('DO YOU REALLY WANT TO DELETE THIS ELEMENT? (Y/N)')
                delConfirm = input('CONFIRM: ')
                if delConfirm == 'y':
                    try:
                        self.DataFrame.delete(delSearch[0].name)
                        print('ELEMENT DELETED')
                        self.deleteRow()
                    except:
                        print('ERROR! ELEMENT NOT DELETED!')
                        self.deleteRow()
                elif delConfirm == 'n':
                    print('\nDELETION ABORTED\n')
                    self.deleteRow()
                else:
                    print('\nINVALID INPUT,DELETION ABORTED\n')
                    self.deleteRow()
        elif delChoice == '2':
            print('\n')
            delIndex = input('INDEX: ')
            if int(delIndex) <= len(self.DataFrame.df):
                print('\nDETAILS:')
                print(self.DataFrame.df.iloc[int(delIndex)])
                print('DO YOU REALLY WANT TO DELETE THIS ELEMENT? (Y/N)')
                delConfirm = input('CONFIRM: ')
                if delConfirm == 'y':
                    try:
                        self.DataFrame.delete(delIndex)
                        print('ELEMENT DELETED')
                        self.deleteRow()
                    except:
                        print('ERROR! ELEMENT NOT DELETED!')
                        self.deleteRow()
                elif delConfirm == 'n':
                    print('\nDELETION ABORTED\n')
                    self.deleteRow()
                else:
                    print('\nINVALID INPUT,DELETION ABORTED\n')
                    self.deleteRow()
            else:
                print('INDEX OUT OF BOUNDS!')
                self.deleteRow()
        elif delChoice == '0':
            self.startScreen()
        else:
            print('\n####\nBAD INPUT, PLEASE CHOOSE ONE OF THE OPTIONS.\n####\n')
            self.deleteRow()
        
        
        pass
    def addRow(self):
        print('WARNING! ADDING NEW DATA!')
        print('\nTHE DATA FORMAT REQUIRES 15 PARAMETERS; 3 STRINGS & 12 FLOATS\n')
        print('ADD NEW ROW     : 1')
        print('GO TO START MENU: 2')
        
        aRchoice = input()
        if aRchoice == '1':
            aRrow = []
            print('INPUT DATA:')
            aRname = input('CEREAL NAME: ')
            aRmfr = input('MANUFACTURER: ')
            aRrow.append(aRmfr)
            aRHC = input('SERVED HOT(h) OR COLD(c): ')
            aRrow.append(aRHC)
            aRcal = input('CALORIES PER SERVING: ')
            try:
                aRrow.append(float(aRcal))
                aRprot = input('GRAMS OF PROTEIN/100g: ')
                try:
                    aRrow.append(float(aRprot))
                    aRfat = input('GRAMS OF FAT/100g: ')
                    try:
                        aRrow.append(float(aRfat))
                        aRsod = input('MILLIGRAMS OF SODIUM/100g: ')
                        try:
                            aRrow.append(float(aRsod))
                            aRfib = input('GRAMS OF FIBER/100g: ')
                            try:
                                aRrow.append(float(aRfib))
                                aRcarb = input('GRAMS OF CARBOHYDRATES/100g: ')
                                try:
                                    aRrow.append(float(aRcarb))
                                    aRsug = input('GRAMS OF SUGARS/100g: ')
                                    try:
                                        aRrow.append(float(aRsug))
                                        aRpot = input('MILLIGRAMS OF POTASSIUM/100g: ')
                                        try:
                                            aRrow.append(float(aRpot))
                                            aRvit = input('% OF FDA RECOMMENDED DAILY VITAMINS: ')
                                            try:
                                                aRrow.append(float(aRvit))
                                                aRshelf = input('DISPLAY LEVEL OF SHELF FROM FLOOR (1-2-3): ')
                                                try:
                                                    aRrow.append(float(aRshelf))
                                                    aRwei = input('OUNCES(28.3g) PER SERVING: ')
                                                    try:
                                                        aRrow.append(float(aRwei))
                                                        aRcup = input('CUPS(0.24l) PER SERVING: ')
                                                        try:
                                                            aRrow.append(float(aRcup))
                                                            print('\nADD THIS ROW?(y/n)\n')
                                                            print(aRname+': '+str(aRrow))
                                                            aRconfirm = input('CONFIRM: ')
                                                            
                                                            if aRconfirm == 'y':
                                                                try:
                                                                    self.DataFrame._add(aRname, aRrow)
                                                                    print('ROW ADDED!')
                                                                    self.addRow()
                                                                except:
                                                                    print('ERROR! ROW NOT ADDED!')
                                                                    self.addRow()
                                                               
                                                            elif aRconfirm == 'n':
                                                                print('\nROW NOT ADDED!\n')
                                                                self.addRow()
                                                            else:
                                                                print('\nINVALID INPUT! ROW NOT ADDED!\n')
                                                                self.addRow()
                                            
                                                        except:
                                                            print('LAST 12 INPUTS MUST BE FLOATS')
                                                            self.addRow()
                                                    except:
                                                        print('LAST 12 INPUTS MUST BE FLOATS')
                                                        self.addRow()
                                                except:
                                                    print('LAST 12 INPUTS MUST BE FLOATS')
                                                    self.addRow()
                                            except:
                                                print('LAST 12 INPUTS MUST BE FLOATS')
                                                self.addRow()
                                        except:
                                            print('LAST 12 INPUTS MUST BE FLOATS')
                                            self.addRow()
                                    except:
                                        print('LAST 12 INPUTS MUST BE FLOATS')
                                        self.addRow()
                                except:
                                    print('LAST 12 INPUTS MUST BE FLOATS')
                                    self.addRow()
                            except:
                                print('LAST 12 INPUTS MUST BE FLOATS')
                                self.addRow()
                        except:
                            print('LAST 12 INPUTS MUST BE FLOATS')
                            self.addRow()
                    except:
                        print('LAST 12 INPUTS MUST BE FLOATS')
                        self.addRow()
                except:
                    print('LAST 12 INPUTS MUST BE FLOATS')
                    self.addRow()
            except:
                print('LAST 12 INPUTS MUST BE FLOATS')
                self.addRow()
        
        elif aRchoice == '2':
            self.startScreen()
        else:
            print('INVALID INPUT!')
            self.addRow()
        

    def editRow(self):
        print('WARNING! EDITING DATA!\n')
        print('PLEASE CHOOSE THE INDEX OF THE CEREAL YOU WANT TO EDIT:')
        print('WRITE x TO GO TO START MENU')
        eRindex = input('INDEX: ')
        if eRindex == 'x':
            self.startScreen()
        else:
            try:
                eRindexINT = int(eRindex)
                eRrow = self.DataFrame.df.iloc[eRindexINT]
                print('DETAILS: ')
                print(eRrow)
                print('IS THIS THE CEREAL YOU WISH TO EDIT?(y/n)')
                eRconfirmrow = input('CONFIRM: ')
                if eRconfirmrow == 'y':
                    print('PLEASE WRITE THE COLUMN TO BE EDITED AND THE NEW VALUE: ')
                    self.printColumns()
                    eRcolumn = input('COLUMN: ')
                    if eRcolumn in self.columns:
                        eRval = input('VALUE: ')
                        try:
                            eRvalINT = int(eRval)
                            print('\nDO YOU REALLY WISH TO EDIT THIS ROW?(y/n)')
                            eRconfirmedit = input('CONFIRM: ')
                            if eRconfirmedit == 'y':
                                try:
                                    self.DataFrame.edit(eRcolumn, eRindexINT, eRvalINT)
                                    print('ROW EDITED!')
                                    self.startScreen()
                                except:
                                    print('ERROR! ROW NOT EDITED!')
                                    self.editRow()
                            elif eRconfirmedit == 'n':
                                print('ROW NOT EDITED!')
                                self.editRow()
                            else:
                                print('INVALID INPUT! ROW NOT EDITED!')
                                self.editRow()
                        except:
                            print('INVALID INPUT! NEW VALUE MUST BE A FLOAT!')
                            self.editRow()
                    else:
                        print('INVALID INPUT! PLEASE CHOOSE ONE OF THE COLUMNS LISTED')
                        self.editRow()
                elif eRconfirmrow == 'n':
                    self.editRow()
                else:
                    print('INVALID INPUT!')
                    self.editRow()
                
                
            except:
                print('ERROR! INDEX MUST BE AN INTEGER!')
                self.editRow()
        

        
    def printColumns(self):
        print('\nTHE NAMES OF THE NUMERICAL COLUMNS ARE:')
        print('CALORIES, PROTEIN, FAT, SODIUM, FIBER, CARBO, \nSUGARS, POTASS, VITAMINS, SHELF, WEIGHHT, CUPS\n')
    
    
KonsolUI()


