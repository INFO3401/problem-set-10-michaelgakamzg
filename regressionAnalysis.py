import csv
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.logistic_model import LogisticRegression

#I worked with Aaron and he walked me through how to get the simpleanalysis part of the problem set
#I used mostly stackoverflow and found videos online
# I get this error --File "regressionAnalysis.py", line 23, in <module> parseData = AnalysisData('./candy-data.csv')TypeError: object() takes no parameters


class AnalysisData:
    
    def _init_(self,filename):
        self.variables = []
        self.filename = filename
    
    def parseFile(self):
        self.dataset = pd.read_csv(self.filename)
        self.variables = self.dataset.columns

parseData = AnalysisData('./candy-data.csv')
parseData.parseFile()



class LinearAnalysis:
    
    def _init_(self,targetY):
        
        self.bestX = ""
        self.targetY = targetY
        self.fit = ""
    
    
    def runSimpleAnalysis(self,parseData):
        
            dataset = parseData.dataset
            
            best_predictor = 0
            for column in parseData.variables:
                if column == self.targetY or column == 'competitorname':
                    continue
                
                x_values = parseData[column].values.reshape(-1,1)
                y_values = parseData[self.targetY].values
                
                regress = LinearRegression()
                regress.fit(x_values, y_values)
                predictors = regress.predict(x_values)
                score = r2_score(y_values, predictors)
             
#http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
             
                if score > best_predictor:
                    best_predictor = score
                    self.bestX = column
    
            self.fit = best_predictor
            print(self.bestX)
            print(self.fit)

linear_analysis = LinearAnalysis(targetY = 'sugarpercent')
linear_analysis.runSimpleAnalysis(parseData)




class LogisticAnalysis:

        def _init_(self,targetY)
            self.bestX = ""
            self.targetY = targetY
            self.fit = ""


        def runSimpleAnalysis(self,parseData):
    
            dataset = parseData.dataset
        
            best_predictor = 0
            for column in parseData.variables:
                  if column == self.targetY or column == 'competitorname':
                      continue
            
                    x_values = parseData[column].values.reshape(-1,1)
                    y_values = parseData[self.targetY].values
                
                    regress = LinearRegression()
                    regress.fit(x_values, y_values)
                    predictors = regress.predict(x_values)
                    score = r2_score(y_values, predictors)
                
               
                
                    if score > best_predictor:
                            best_predictor = score
                            self.bestX = column
    
                self.fit = best_predictor
                print(self.fit)
                print(self.bestX)
                print(regress.intercept_)
                print(regr.coef_)


        def runMultipleRegression(self, parseData):

                    dataset = parseData.dataset

                    x_values = parseData[column].values.reshape(-1,1)
                    y_values = parseData[self.targetY].values
        
                    regress = LogisticRegression()
                    regress.fit(x_values, y_values)
                    predictors = regress.predict(x_values)
                    score = r2_score(y_values, predictors)

                    print(new_dataset.columns)
                    print(score)
                    print(regress.coef_)
                    print(regress.intercept_)

    logistic_analysis = LogiticAnalysis(targetY = 'chocolate')
    logitic_analysis.runSimpleAnalysis(parseData)

    regression_analysis = runMultipleRegression(targetY = 'chocolate')
    regression_analysis.runMultipleRegression(parseData)

#4. Identify the independent variable(s) and its type (e.g., categorical, continuous, or discrete), the dependent variable and its type, and the null hypothesis for each of the following scenarios:

        #(a) What candies contain more sugar, those with caramel or those with chocolate?

# - Independent = (Categorical) Fruity

# - Independent = (Categorical) Fruity

# - Dependant = (Continuous) Sugarpercent


# - Null Hypothesis = Fruity and peanutyalmond have similar sugar percentages


        #(b) Are there more split ticket voters in blue states or red states?

# - Independent = (Discrete) Red states

# - Independent = (Discrete) Blue states

# - Dependant = (Discrete) Split ticket voters


# - Null Hypothesis = There are an equal amount in red and blue states


        #(c) Do phones with longer battery life sell at a higher or lower rate than other phones?

# - Independent = (Categorical) Phones with shorter battery lives

# - Independent = (Categorical) Phones with longer battery lives

# - Dependant = (Continuous) A phone can be $99.99

# - Null Hypothesis = Selling at different rates, higher for phones with long battery lives


